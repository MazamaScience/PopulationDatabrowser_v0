/*
 * Mazama_databrowser.js
 *
 * Jonathan Callahan
 * http://mazamascience.com
 *
 * Default behavior for Mazama Science databrowsers.
 *
 * 1) Any change to an element in the form should trigger a plot request so that the
 *    current state of the UI always reflects the parameters used to generate the plot.
 *
 * 2) Each successful response contains a url for the plot and an array of values
 *    for potential use in this javascript code.
 *
 */

/**** GLOBAL VARIABLES ********************************************************/

// All global variables begin with 'G_'
var G_myGlobalVariable = 1;


/**** UTILITY FUNCTIONS *******************************************************/

// Display text as an error message
function displayError(errorText) {

  // Clean up error message
  errorText = errorText.trim();
  i = errorText.lastIndexOf("Error :");
  if (i >= 0 ) { errorText = errorText.substr(i+8) }
  i = errorText.lastIndexOf("Error:");
  if (i >= 0) { errorText = errorText.substr(i+7) }

  // If the error message is short enough, display it in the requestMessage 
  // area with the default 'alert' styling.  Otherwise put up an alert box.
  // NOTE:  Other styling options
  // NOTE:    .notice is yellow box
  // NOTE:    .info blue box
  // NOTE:    .success green box
  // NOTE:    .error pink box
  if (errorText.length < 80) {

    $('#requestMessage').show().addClass('error').text(errorText);
  } else {
    alert(errorText);
  }

}


/**** EVENT HANDLERS **********************************************************/

// One layer of abstraction before sending the request allows us to take UI
// specific actions, e.g. setting hidden parameters or disabling some elements,
// before sending the request.
function updatePlot() {
  // Set any hidden parameter values based on UI state.
  // ('#hiddenParameter').val(1.0);

  // for iphone
  if (window.innerWidth <= 481) {
     $('#plotWidth').val(320);
  }

  prePlotActions();

  sendRequest();
}

// Set styles, disable elements, etc.
function prePlotActions() {
  $('#spinner').fadeIn(500);
  $('#requestMessage').hide().removeClass('alert').text('');
}

// Reset styles, enable disabled elements, etc.
function postPlotActions(JSONResponse) {
  $('#spinner').hide(function(){
    $("#databrowser").fadeIn();
  });
  
}


/**** REQUEST HANDLERS ********************************************************/

// Serialize the form and send it to the CGI.
// NOTE:  Some UI elements have no bearing on the product generated and
// NOTE:  should be removed from the request to improve our cache hit rate.
function sendRequest() {
  var url = '/cgi-bin/__DATABROWSER__.cgi';
  var data = $('#controlsForm').serialize();
  var removeList = $('.doNotSerialize');
  for (i=0; i<removeList.length; i++) {
     removeString = '&' + $(removeList[i]).serialize();
     data = data.replace(removeString,'');
  }
  $.getJSON(url, data, handleJSONResponse);
}

function handleJSONResponse(JSONResponse) {
  if (JSONResponse.status == 'ERROR') {
    $('#plot').css({ opacity: 0.5 });
    displayError(JSONResponse.error_text);
  } else {
    $('#plot').css({ opacity: 1.0 });
    // NOTE:  If more than one result is generated, they should have names
    // NOTE:  derived from the basename.
    var img_url = JSONResponse.rel_base + ".png";
    $('#plot').attr('src',img_url);
    returnValues = JSONResponse.return_values; 
    // return_values have many potential uses but are not used in the example databrowser
  }
  postPlotActions();
}

/**** INITIALIZATION **********************************************************/

$(function() {

  // Initialization is wrapped inside of the getJSON function since it depends
  // on the JSON file to function

  $.getJSON( "data_local/language.json", function( data ) {

    dataset = data;

    // Changes the html and R text to a given language
    function newLanguage(language, country, group){
      var textList = dataset[language];

      $("#group").html(textList.html["group"]);
      $("#country").html(textList.html["country"]);

      // Empty chosen
      $(".chosen").empty();

      // Create a new select menu with translated country names
      var country_output = [];
      var group_output = [];

      // Populate group menu
      group_list = textList.region_names.sort(SortByName);
      $.each(group_list, function(){
        group_output.push('<option value="'+ this.code +'">'+ this.name +'</option>');
      });

      // Populate country menu
      country_list = textList.country_names.sort(SortByName);
      
      $.each(country_list, function(){
        country_output.push('<option value="'+ this.code +'">'+ this.name +'</option>');
      });

      $('#group_select').html(group_output.join(''));
      $('#country_select').html(country_output.join(''));

      // Update chosen menu with new countries
      $("#group_select").val(group);
      $("#country_select").val(country);
      $(".chosen").trigger("chosen:updated");

      // Set new language for plotting
      $("#language").val(language);

      // Set translated "name" attribute
      var chosen_id = "#" + $(".chosen-single.selected").parent().attr("id");
      var id = chosen_id.substring(0,chosen_id.length-7);
      var name = $(id + " option:selected").text();
      $("#countryName").val(name);

      // new plot
      updatePlot();
     
    };

    // Parameter initialization ---------------------------------

    //check query string for parameters
    var url = $.url();

    // initialize object with plotting parameters
    var plotParameters = new Object();
    plotParameters.country = url.param('country') ? (countryCheck(url.param('country').toUpperCase()) ? url.param('country').toUpperCase() : 'US') : 'US';
    plotParameters.language = url.param('language') ? (languageCheck(url.param('language').toLowerCase()) ? url.param('language').toLowerCase() : 'en') : 'en';

    plotParameters.toString = function() {
      return { country:plotParameters.country, language:plotParameters.language };
    };
    plotParameters.active = plotParameters.country.length == 2 ? 'country_names' : 'region_names';
    plotParameters.setQuery = function() {
      window.location.hash = "";
      window.history.replaceState({}, "", "?" + jQuery.param( plotParameters.toString() ));
    };

    plotParameters.setQuery();

    function countryCheck( code ) {
      console.log(code);
      if ( !(arrSearch(dataset.en.country_names, "code", code)) && !(arrSearch(dataset.en.region_names, "code", code)) ) {
        window.alert("Error: country code " + code + " not recognized.");
        return false;
      } else {
        return true;
      }
    }

    function languageCheck( language ) {
      if ( !(arrSearch(dataset, "language", language))) {
        window.alert("Error: language " + language + " not recognized.");
        return false;
      } else {
        return true;
      }
    }

    function arrSearch( arr, key, val ) {
      for (i in arr) {
        if (arr[i][key]== val) {
          return true
        }
      }
      return false
    }


    // update control variables
    $('#language').val(plotParameters.language);
    $('#countryCode').val(plotParameters.country);
    $('#countryName').val(dataset[plotParameters.language][plotParameters.active][plotParameters.country]);

    // Initialize chosen menu
    $(".chosen").chosen({disable_search_threshold: 15});

    // Select either country or group menu
    // Make initial plot
    if (plotParameters.active == 'country_names') { 
      $("#country_select_chosen .chosen-single").addClass("selected");
      $("#country_select_chosen .chosen-single div b").addClass("white");
      newLanguage(plotParameters.language, plotParameters.country, "default");
    } else {
      $("#group_select_chosen .chosen-single").addClass("selected");
      $("#group_select_chosen .chosen-single div b").addClass("white");
      newLanguage(plotParameters.language, "default", plotParameters.country);
    }

    // initialize language flag menu
    var language_output = [];
    $.each(dataset.flags, function(key, val){
        language_output.push('<li class="flagLi" id="' + key + '" title="' + val.language + '"><img class="flag" src="style/images/flags/' + val.flag + '.png"></li>');
    });
    $('#language_list').html(language_output.join(''));
    $("#" + plotParameters.language).addClass("selected") // initially select English

    // Function for sorting countries by name
    function SortByName(a, b){
      var aName = a.name.toLowerCase();
      var bName = b.name.toLowerCase(); 
      return ((aName < bName) ? -1 : ((aName > bName) ? 1 : 0));
    }
  
    // End parameter initialization -----------------------------


    // Hide the spinner
    $('#spinner').hide();


    // Attach behavior to UI elements --------------------------

    // Set behavior for country and group  menus
    $("#group_select_chosen .chosen-results").click(clickSwitch);
    $("#country_select_chosen .chosen-results").click(clickSwitch);

    // Set behavior for keyboard changes 
    $("#group_select").change(keySwitch);
    $("#country_select").change(keySwitch);

    // Allows menu to work if same value is selected
    function clickSwitch(){
      var chosen_id = "#" + $(this).parents().eq(1).attr("id");
      var id = chosen_id.substring(0,chosen_id.length-7);
      codeSwitch(id, chosen_id);
    }

    // Get menu ID's
    function keySwitch(){
      var id = "#" + ($(this).attr("id"));
      var chosen_id = (id + "_chosen");
      codeSwitch(id, chosen_id);
    }

    // Get country code and name from the menu and update plot
    function codeSwitch(id, chosen_id){

      var code = $(id).val();
      var name = $(id + " option:selected").text();

      $("#countryCode").val(code);
      $("#countryName").val(name);

      $(".chosen-single div b").removeClass("white");
      $(chosen_id + " .chosen-single div b").addClass("white");

      $(".chosen-single").removeClass("selected");
      $(chosen_id).children(".chosen-single").addClass("selected");

      plotParameters.country = code
      plotParameters.setQuery();

      updatePlot();
    }

    // Set behavior for language menu
    $(".flagLi").click(languageSwitch);

    function languageSwitch(){
      $(".flagLi.selected").removeClass("selected");
      var language = this.id;

      plotParameters.language = language
      plotParameters.setQuery();

      $("#databrowser").fadeOut(function(){
        newLanguage(language, $("#country_select").val(), $("#group_select").val());
      });
      $(this).addClass("selected");
    }

    // Initial plot with English, United States ------------------

    
    
});


  // Activate tooltips
  // $('span.tooltip').cluetip({width: '500px', attribute: 'id', hoverClass: 'highlight'});
  
  
});



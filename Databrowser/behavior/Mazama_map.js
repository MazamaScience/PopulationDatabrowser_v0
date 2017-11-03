/*   Creates a google map that allows the user to set location of clicked map or kml incident 
     and sets it as location for analysis and fills boxes. The behavior of the map is designed to 
     be familiar to anyone who uses Google Maps. 
*/

/**** GLOBAL VARIABLES ********************************************************/

// These are the generic map features most commonly used by databrowsers 

var G_marker;
var G_map;
var G_kml; 

/**** UTILITY FUNCTIONS *******************************************************/

function updateLocation(latLng) {
  var lat = latLng.lat();
  var lon = latLng.lng();
  // round the location to 3 decimal places 
  lat = Math.round(lat * 1000) / 1000
  lon = Math.round(lon * 1000) / 1000
  // populate the box/field with lat, lng
  $('#lat').val(lat)
  $('#lon').val(lon)
}


function toggleKML() {
  
	// Make the layer! 
	if (G_kml == null) {
	
		var kmlUrl = 'http://inciweb.org/feeds/maps/';
		var kmlOptions = {
			suppressInfoWindows: false,
			preserveViewport: true,
			clickable:true,
			map: map
		};
    // Create the kml layer 
		G_kml = new google.maps.KmlLayer(kmlUrl, kmlOptions);
		// place the kml layer on the map 
	  G_kml.setMap(G_map);
	  
	  $('#KMLButton').val("Hide kml")
		
	
	} else { // Layer exists, hide by setting to null 
		G_INCIkml.setMap(null);
		G_INCIkml = null;
		
		$('#KMLButton').val("Show kml");
	}
		
}


/**** lat/lon FUNCTIONS *******************************************************/

function latLonChange(event) {
  var lat = $('#lat').val();
  var lon = $('#lon').val();
  latLng = new google.maps.LatLng(lat,lon);
  G_map.setCenter(latLng);
  G_marker.setPosition(latLng);
  updateLocation(latLng);
}

/**** MAP FUNCTIONS ***********************************************************/

// marker drag event -----------------------------------------------------------
function markerDragEnd(event) {
  updateLocation(event.latLng);
}

// map click event -------------------------------------------------------------
function positionMarker(event) {
  G_marker.setPosition(event.latLng);
  updateLocation(event.latLng);
}


// Initialization --------------------------------------------------------------
function initializeMap() {
  
  // get initial lat/lon values from the lat lon fields in the UI
  var lat = $('#lat').val();
  var lon = $('#lon').val();

  // attach map behavior
  $('#lat').change(latLonChange);
  $('#lon').change(latLonChange);

  // create the map
  var mapOptions = {
    zoom: 5,
    center: new google.maps.LatLng(lat,lon),
    mapTypeId: google.maps.MapTypeId.TERRAIN
  };

  G_map = new google.maps.Map(document.getElementById('mapCanvas'), mapOptions);

  // attach map behavior
  google.maps.event.addListener(G_map, "click", positionMarker);
    
  // create a marker
  G_marker = new google.maps.Marker({
    position: G_map.getCenter(),
    map: G_map,
    draggable: true,
    title: 'Marker Location'
  });
  
  // attach marker behavior
  google.maps.event.addListener(G_marker, 'dragend', markerDragEnd);

  // put the spinner of the map by grabbing the spinner id 
  //G_map.controls[google.maps.ControlPosition.CENTER].push(document.getElementById('map_spinner_container'));
  
}



/*******************************************************************************
 * Image popout script 
 * powered by jQuery (http://www.jquery.com)
 * 
 * written by Alen Grakalic (http://cssglobe.com)
 * 
 * for more info visit http://cssglobe.com/post/1695/easiest-tooltip-and-image-popout-using-jquery
 *
 * Modified by Jonathan Callahan (http://mazamascience.com)
 */
 
this.imagePopout = function(){  
  // NOTE:  Configure the position of the popout image either
  // NOTE:  in absolute pixels or in pixels relative to the
  // NOTE:  mouse location when the hover event is fired.
  position = "absolute";
  xPos = $('#mapCanvas').position().left;
  yPos = $('#mapCanvas').position().top;

  $("img.popout").hover(function(e){
    w = this.width;
    h = this.height;
    this.t = this.title;
    this.title = "";  
    var c = (this.t != "") ? "<br/>" + this.t : "";
    $("body").append("<p id='imagePopout'><img src='"+ this.src +"' alt='Image popout' />"+ c +"</p>");                 
    if (position == "relative") {
      xPos = e.pageX + xPos;
      yPos = e.pageY + yPos;
    }
    $("#imagePopout")
      .css("position",position)
      .css("top",yPos + "px")
      .css("left",xPos + "px")
      .fadeIn("fast");            
  },
  function(){
    this.title = this.t;  
    $("#imagePopout").remove();
  });  
  // If you want the image to move around with the mouse
  // $("img.popout").mousemove(function(e){
  //   $("#imagePopout")
  //     .css("top",(e.pageY - xOffset) + "px")
  //     .css("left",(e.pageX + yOffset) + "px");
  // });      
};


// starting the script on page load
$(document).ready(function(){
  imagePopout();
});

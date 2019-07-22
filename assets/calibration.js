
/**
 * Clear the canvas and the calibration button.
 */
function ClearCanvas(){
  $(".Calibration").hide();
  var canvas = document.getElementById("plotting_canvas");
  canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
}

/**
 * Show the instruction of using calibration at the start up screen.
 */
function PopUpInstruction(){
  ClearCanvas();
  let webcamElem = document.getElementById('webcamElementId');
  let clone = document.getElementById('controlHeader').cloneNode(true);
  swal({
    content: webcamElem,
    closeOnClickOutside: false,
    text: "Smile! Make sure your face is in the center of the square and that it is detected",
    buttons:{
      confirm: true,
    }
  }).then(isConfirm =>{
    $('#webcamElementId').appendTo('#controlHeader');
    swal({
        icon: 'info',
        title:"Calibration",
        text: "Please keep your head very still and follow the Red Dot. Try not to blink during this process",
        buttons:{
          cancel: false,
          confirm: true
        }
  }).then(isConfirm =>{
    RunCalibration();
  });

});
}

/**
 * Load this function when the index page starts.
* This function listens for button clicks on the html page
* checks that all buttons have been clicked 5 times each, and then goes on to measuring the precision
*/
$(document).ready(function(){
  ClearCanvas();
  // $('#startReading').css('background-color','gray');
  // $('#startReading').css('pointer-events','none');
  // $('#startReading').prop('title','Please Run Calibration to Use this Feature');
});

let CalibrationSteps = [
  ()=>{cal.css('top','2px');},
  ()=>{cal.css('left',cal_left+'px');},
  ()=>{cal.css('left', 2*cal_left - cal_width + 'px');},
  ()=>{cal.css('top', cal_top+'px');},
  ()=>{cal.css('top', 2*cal_top - cal_height+'px');},
  ()=>{cal.css('left',cal_left+'px')},
  ()=>{cal.css('left','2px')},
  ()=>{cal.css('top',cal_top+'px')},
  ()=>{cal.css('left',cal_left/2+'px')},
  ()=>{cal.css('top',cal_top/2+'px')},
  ()=>{cal.css('left',cal_left+'px')},
  ()=>{cal.css('left',3*cal_left/2 +'px')},
  ()=>{cal.css('top',cal_top)},
  ()=>{cal.css('top',3*cal_top/2+'px')},
  ()=>{cal.css('left',cal_left)},
  ()=>{cal.css('left',cal_left/2)},
  ()=>{cal.css('top',cal_top)},
  ()=>{cal.css('left',cal_left)}
]

function RunCalibration(){
  cal = $('#Pt5');
  cal.css('opacity','1');
  cal.show();

  let transitionTime = '2s';

  cal_left = cal.offset().left;
  cal_top = cal.offset().top;
  cal_width = 20; //px
  cal_height = 20;//px
  calibration_interval_timer = setInterval(recordDotPos,2);
  cal.css('transition', `top ${transitionTime} linear, left ${transitionTime} linear`);
  cal.css('left','2px');

  let step = 0;
  calibration_is_running  = true;
  cal.on('transitionend webkitTransitionEnd oTransitionEnd otransitionend MSTransitionEnd', 
    function() {
      if(step < CalibrationSteps.length){
        CalibrationSteps[step++]();
      }
      else{
        step = 0;
        calibration_is_running = false;
        
        webgazer.addMouseEventListeners();
        cal.hide();
        swal({
          title:"Calibration Finished!",
          text: "Thank you for Calibrating. You can now go ahead and use Atten.Tech's Awesome Features!",
          icon: 'success',
          buttons:{
            confirm: true,
          }
        }).then(isConfirm =>{
          $('#startReading').css('pointer-events','auto');
          $('#startReading').css('background-color','rgba(34,139,34,0.6)  ')
        });

      }
    });
  

 
  
}

var calibration_interval_timer;
var calibration_is_running = false;

function recordDotPos(){
  // console.log("LOGGING CALIBRATION POINT");
  if (!calibration_is_running){
    // console.log("CLEARING INTERVAL");
    clearInterval(calibration_interval_timer);
  }
  let x = $('#Pt5').offset().left+10;
  let y = $('#Pt5').offset().top+10;
  webgazer.recordScreenPosition(x,y,'click');
}


/**
* This function clears the calibration buttons memory
*/
function ClearCalibration(){
  webgazer.resetData();
  window.localStorage.clear();
} 

// sleep function because java doesn't have one, sourced from http://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

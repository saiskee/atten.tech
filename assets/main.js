window.onload = function() {

    // start the webgazer tracker
    webgazer.setRegression('ridge') /* currently must set regression and tracker */
        .setTracker('clmtrackr')
        .setGazeListener(function(data, clock) {
            // console.log(data, clock); /* data is an object containing an x and y key which are the x and y prediction coordinates (no bounds limiting) */
            // console.log(clock); /* elapsed time in milliseconds since webgazer.begin() was called */
            addData(data);
        })
        .begin()
        .showPredictionPoints(true); /* shows a square every 100 milliseconds where current prediction is */


    //Set up the webgazer video feedback.
    var setup = function() {

        //Set up the main canvas. The main canvas is used to calibrate the webgazer.
        var canvas = document.getElementById("plotting_canvas");
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        canvas.style.position = 'fixed';
    };

    function checkIfReady() {
        if (webgazer.isReady()) {
            setup();
        } else {
            setTimeout(checkIfReady, 100);
        }
    }
    setTimeout(checkIfReady,100);
};

window.onbeforeunload = function() {
    //webgazer.end(); //Uncomment if you want to save the data even if you reload the page.
    window.localStorage.clear(); //Comment out if you want to save data across different sessions
}

/**
 * Restart the calibration process by clearing the local storage and reseting the calibration point
 */
function Restart(){
    // document.getElementById("Accuracy").innerHTML = "<a>Not yet Calibrated</a>";
    ClearCalibration();
    PopUpInstruction();
}

var eye_tracking_data = {}
var eye_tracking_data_recording = false;
function StartDataRecording(){
    eye_tracking_data_recording = true;
    eye_tracking_data = {}

}
function StopDataRecording(){
    eye_tracking_data_recording = false;
    const http = new XMLHttpRequest();
    const url = "http://localhost:5000/datapost"
    http.open('POST', url);
    http.setRequestHeader("Content-Type", "text");
    console.log(JSON.stringify(eye_tracking_data))
    http.send(JSON.stringify(eye_tracking_data))
    http.onload=function(res){
        var css = (res.currentTarget.response);
        console.log(css);
        head = document.head || document.getElementsByTagName('head')[0],
        style = document.createElement('style');
        head.appendChild(style);
        style.type = 'text/css';
        if (style.styleSheet){
        // This is required for IE8 and below.
        style.innerHTML = css;
        } else {
        style.appendChild(document.createTextNode(css));
        }
        // eye_tracking_data = [];
    };
}

function addData(eye_gaze_data){
    if (eye_tracking_data_recording && eye_gaze_data){
        ele = document.elementFromPoint(eye_gaze_data.x,eye_gaze_data.y)
        if (ele){
            if (ele.textContent.length < 3){
                return;
            }
            ele = ele.className
        }else{return;}
        if (eye_tracking_data[ele]){
            eye_tracking_data[ele] += 1;
        }
        else{
            eye_tracking_data[ele] = 1;
        }
    }
}
from bs4 import BeautifulSoup
# def edit_html(htmlpath):
#     soup = ''
#     with open(htmlpath, 'r') as content_file:
#         content = content_file.read()
#         soup = BeautifulSoup(content)
#     for meta in soup('META'):
#         meta.decompose()

def edit_html(htmlpath):
	f = open(htmlpath, "r",  encoding="utf8")
	contents = f.readlines()
	f.close()
	print("HELLO READING HTML", htmlpath)
	contents.insert(10, '<link rel="stylesheet" type="text/css" href="/assets/style.css">')
	contents.insert(11, '<script async type="text/javascript" src="/assets/webgazer.js"></script>')
	contents.insert(20,'''<canvas id="plotting_canvas" width="500" height="500" style="cursor:crosshair;"></canvas>
        <script src="/assets/jquery.min.js"></script>
        <script src="/assets/sweetalert.min.js"></script>

        <script src="/assets/main.js"></script>
        <script src="/assets/calibration.js"></script>
        <script src="/assets/precision_calculation.js"></script>
        <script src="/assets/precision_store_points.js"></script>

		 <!-- Calibration points -->
        <div class="calibrationDiv">
            <input type="button" class="Calibration" id="Pt1"></input>
            <input type="button" class="Calibration" id="Pt2"></input>
            <input type="button" class="Calibration" id="Pt3"></input>
            <input type="button" class="Calibration" id="Pt4"></input>
            <input type="button" class="Calibration" id="Pt5"></input>
            <input type="button" class="Calibration" id="Pt6"></input>
            <input type="button" class="Calibration" id="Pt7"></input>
            <input type="button" class="Calibration" id="Pt8"></input>
            <input type="button" class="Calibration" id="Pt9"></input>
        </div>
        <meta charset="UTF-8">
<link rel="shortcut icon" type="image/x-icon" href="https://static.codepen.io/assets/favicon/favicon-8ea04875e70c4b0bb41da869e81236e54394d63638a1ef12fa558a4a835f1164.ico" />
<link rel="mask-icon" type="" href="https://static.codepen.io/assets/favicon/logo-pin-f2d2b6d2c61838f7e76325261b7195c27224080bc099486ddd6dccb469b8e8e6.svg" color="#111" />
<title>Calibrate Button</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
<style>
      html, body {
  height: 100%;
}

body {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #FAFAFA;
}

button {
  padding: 20px 40px;
  background: none;
  border: none;
  position: relative;
  text-transform: uppercase;
  font-weight: bold;
  letter-spacing: 3px;
  cursor: pointer;
}
button:after, button:before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  border: 2px solid #000;
  transition: -webkit-transform 0.2s;
  transition: transform 0.2s;
  transition: transform 0.2s, -webkit-transform 0.2s;
}
button:after {
  -webkit-transform: translate(3px, 3px);
          transform: translate(3px, 3px);
}
button:before {
  -webkit-transform: translate(-3px, -3px);
          transform: translate(-3px, -3px);
}
button:hover:after, button:hover:before {
  -webkit-transform: translate(0);
          transform: translate(0);
}

    </style>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>
</head>
<body translate="no">
<script src="https://static.codepen.io/assets/editor/live/css_reload-5619dc0905a68b2e6298901de54f73cefe4e079f65a75406858d92924b4938bf.js"></script>
        <button type="button" class = "btn btn-primary" onclick="Restart()" style="z-index:100; position:fixed; bottom: 5%; left: 2vw">Calibrate</button>
        <button type="button" class = "btn btn-primary" onclick="StartDataRecording()" style="z-index:100; position:fixed; bottom: 30%; right:2vw; background-color: rgba(34,139,34,0.4);">Start Reading</button>
        <button type="button" class = "btn btn-primary" onclick="StopDataRecording()" style="z-index:100; position:fixed; bottom: 5%; right: 2vw; background-color: rgba(255,99,71,0.4);">Stop Reading</button>

        <!-- Latest compiled JavaScript -->
        <script src="/assets/resize_canvas.js"></script>''')
	f = open(htmlpath, "w",  encoding="utf8")
	contents = "".join(contents)
	f.write(contents)
	f.close()
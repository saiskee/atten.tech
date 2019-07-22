from bs4 import BeautifulSoup

def scrape(text):
    # soup = BeautifulSoup(text, "html.parser")
    # # elements = soup.find_all(" ")
    # i = 0
    # for elem in soup.contents:
    #     try:
    #         print(str(elem['class']))
    #     except:
    #         print("hello")
    #     # elem['class'] = str(elem['class']) + str(i)
    #     i += 1
    contents = []
    inject = open('inject.html','r', encoding='utf8')
    contents_inject= inject.readlines()
    contents.insert(0,"".join(contents_inject))
    contents= "".join(contents)
    contents = contents + '''<body>
    <iframe id="websiteembed" style="position:fixed; top: 0px; left: 0px; height:100vh; width:100vw;" src=http://localhost:5000/index.php?url='''+text+'''>
    </body>'''
    return contents

#     return ('''
#     <!doctype html>
#     <head>
#     <script>
    
#     var doc = document.getElementById('websiteframe').contentWindow.document;
#     doc.open();
#     console.log(doc.read());
#     doc.write(`<link rel="stylesheet" type="text/css" href="/assets/style.css">
    
# 	<canvas id="plotting_canvas" width="500" height="500" style="cursor:crosshair;"></canvas>
#         <script src="/assets/jquery.min.js"></script>
#         <script src="/assets/sweetalert.min.js"></script>
#         <script type="text/javascript" src="/assets/webgazer.js"></script>
#         <script src="/assets/main.js"></script>
#         <script src="/assets/calibration.js"></script>
#         <script src="/assets/precision_calculation.js"></script>
#         <script src="/assets/precision_store_points.js"></script>

# 		 <!-- Calibration points -->
#         <div class="calibrationDiv">
#             <input type="button" class="Calibration" id="Pt1"></input>
#             <input type="button" class="Calibration" id="Pt2"></input>
#             <input type="button" class="Calibration" id="Pt3"></input>
#             <input type="button" class="Calibration" id="Pt4"></input>
#             <input type="button" class="Calibration" id="Pt5"></input>
#             <input type="button" class="Calibration" id="Pt6"></input>
#             <input type="button" class="Calibration" id="Pt7"></input>
#             <input type="button" class="Calibration" id="Pt8"></input>
#             <input type="button" class="Calibration" id="Pt9"></input>
#         </div>
#         <meta charset="UTF-8">
# <link rel="shortcut icon" type="image/x-icon" href="https://static.codepen.io/assets/favicon/favicon-8ea04875e70c4b0bb41da869e81236e54394d63638a1ef12fa558a4a835f1164.ico" />
# <link rel="mask-icon" type="" href="https://static.codepen.io/assets/favicon/logo-pin-f2d2b6d2c61838f7e76325261b7195c27224080bc099486ddd6dccb469b8e8e6.svg" color="#111" />
# <title>Calibrate Button</title>
# <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/meyer-reset/2.0/reset.min.css">
# <style>
#       html, body {
#   height: 100%;
# }

# body {
#   display: flex;
#   justify-content: center;
#   align-items: center;
#   background: #FAFAFA;
# }

# button {
#   padding: 20px 40px;
#   background: none;
#   border: none;
#   position: relative;
#   text-transform: uppercase;
#   font-weight: bold;
#   letter-spacing: 3px;
#   cursor: pointer;
# }
# button:after, button:before {
#   content: "";
#   position: absolute;
#   top: 0;
#   left: 0;
#   bottom: 0;
#   right: 0;
#   border: 2px solid #000;
#   transition: -webkit-transform 0.2s;
#   transition: transform 0.2s;
#   transition: transform 0.2s, -webkit-transform 0.2s;
# }
# button:after {
#   -webkit-transform: translate(3px, 3px);
#           transform: translate(3px, 3px);
# }
# button:before {
#   -webkit-transform: translate(-3px, -3px);
#           transform: translate(-3px, -3px);
# }
# button:hover:after, button:hover:before {
#   -webkit-transform: translate(0);
#           transform: translate(0);
# }

#     </style>
# <script>
#   window.console = window.console || function(t) {};
# </script>
# <script>
#   if (document.location.search.match(/type=embed/gi)) {
#     window.parent.postMessage("resize", "*");
#   }
# </script>
# </head>
# <body translate="no">
# <script src="https://static.codepen.io/assets/editor/live/css_reload-5619dc0905a68b2e6298901de54f73cefe4e079f65a75406858d92924b4938bf.js"></script>
#         <button type="button" class = "btn btn-primary" onclick="Restart()" style="background-color:rgba(253,245,230,0.4);z-index:100; position:fixed; bottom: 5%; left: 2vw">Calibrate</button>
#         <button type="button" class = "btn btn-primary" onclick="StartDataRecording()" style="z-index:100; position:fixed; bottom: 30%; right:2vw; background-color: rgba(34,139,34,0.4);">Start Reading</button>
#         <button type="button" class = "btn btn-primary" onclick="StopDataRecording()" style="z-index:100; position:fixed; bottom: 5%; right: 2vw; background-color: rgba(255,99,71,0.4);">Stop Reading</button>

#         <!-- Latest compiled JavaScript -->
#         <script src="/assets/resize_canvas.js"></script></iframe>
#     doc.close();
#     })</script>
#     </head>
#     <body>
#     <embed style="position:fixed; top: 0px; left: 0px; height:100vh; width:100vw;" src='''+text+'''>
#     </body>
#     ''')

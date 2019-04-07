import requests
from requests.auth import HTTPBasicAuth
import time
import zipfile
import os, sys, getopt

#api_key = '471f3a97a4ccc0f2d417369db65599e635097856'
#target_format = "html5"
#target_file = "target.zip"

def add_tracking(css_file):
    src = open(css_file, 'r')
    fline = '''.btn-primary {
    color: bisque;
    background-color: rgba(0,151,183,0.4);
    border-radius: 5px;
    width:20em;
    height:10em;
  }
.btn-primary:hover {
  box-shadow: inset 0 0 0 20rem var(--darken-1);
}

.btn-primary:active {
  box-shadow: inset 0 0 0 20rem var(--darken-2),
    inset 0 3px 4px 0 var(--darken-3),
    0 0 1px var(--darken-2);
}

.btn-primary:disabled,
.btn-primary.is-disabled {
  opacity: .5;
}
.Calibration{
    z-index:10000;
    width: 20px;
    height: 20px;
    -webkit-border-radius: 25px;
    -moz-border-radius: 25px;
    border-radius: 25px;
    background-color: red;
    opacity: 0.2;
    border-color: black;
    border-style: solid;
    position:fixed;
}
.calibrationDiv {
    z-index:1000;
}'''
    fline=fline+"\n"    #Prepending string
    oline=src.readlines()
    #Here, we prepend the string we want to on first line
    oline.insert(0,fline)
    src.close()
    
    
    #We again open the file in WRITE mode 
    src=open(css_file,"w")
    src.writelines(oline)
    src.close()


def create_div_data_css(data):
	result = ""
	todel = []
	for attr, value in data.items():
		if ("x1 " in attr or "y1 " in attr or len(attr) < 4 or "btn" in attr or "w0" in attr or "h0" in attr):
			todel.append(attr)
	if (len(data.items()) == 0):
		return
	for attr in todel:
		del data[attr]
	max_val = data[max(data, key = data.get)]
	for attr, value in data.items():
		# strHex = "%0.2X" % 255
		result += str("."+attr.replace(" ", ".")+ " { background-color: #"+str(format((int((value/max_val)*255)),'02x'))+ "00008B;}")
	return result
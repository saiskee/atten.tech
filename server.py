from flask import Flask, request, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import pdftohtml, add_eye_tracking, edit_html, website_scrape
import os, json, requests

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'

app = Flask(__name__) #, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    debug = False
    text = request.form['input1']
    if len(text) is 0:
        if not debug:
            if request.method == 'POST' or request.method == 'GET':
                f = request.files['chosenFile']
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                pdftohtml.pdfToHTML(os.path.dirname(os.path.abspath(__file__)) + '/uploads/' + filename, filename)
                edit_html.edit_html("./static/"+filename[:-4]+'.html')
            # edit_html.edit_html('./static/Manan_Resume.html')
                #filelist = os.listdir('/home/spare/Documents/Projects/AttCheck/static')
            return app.send_static_file(filename[:-4] + '.html')
            # return app.send_static_file('Manan_Resume.html')
        else:
            edit_html.edit_html('./static/Manan_Resume.html')
            return app.send_static_file('Manan_Resume.html')
    else:
        return  website_scrape.scrape(text)
        # print(requests.get(text).text)
        
    



@app.route('/datapost', methods =['POST'])
def process_data():
	req_data = json.loads(request.data)
	result = add_eye_tracking.create_div_data_css(req_data)
	# print(req_data)
	# print("Returning: ", result)
	return result

@app.route('/assets/<path:subpath>')
def return_css_template(subpath):
    return send_from_directory('assets',subpath)

@app.route('/main.css')
def return_main_css():
    add_eye_tracking.add_tracking('./static/main.css')
    return send_from_directory('static','main.css')

@app.route('/<path:subpath>')
def return_file(subpath):
    print(subpath)
    return send_from_directory('static',subpath)



if __name__ == '__main__':
   app.run(debug = True)

from flask import Flask, request, render_template, request, redirect, url_for, send_from_directory, send_file
from flask_cors import CORS
from werkzeug import secure_filename
import pdftohtml, add_eye_tracking, edit_html, website_scrape
import os, json, requests

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'

app = Flask(__name__) #, static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    debug = False
    text = ""
    try:
        text = request.form['input1']
    except:
        print("oh well")
    if len(text) is 0:
        if not debug:
            if request.method == 'POST' or request.method == 'GET':
                f = request.files['chosenFile']
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                pdftohtml.pdfToHTML(os.path.dirname(os.path.abspath(__file__)) + '/uploads/' + filename, filename)
                edit_html.processHTML("./static/"+filename[:-4]+'.html')
            return app.send_static_file(filename[:-4] + '.html')
        else:
            edit_html.processHTML('./static/Manan_Resume.html')
            return send_file('./test.html')
    else:
        return website_scrape.scrape(text)
        
    

@app.route('/datapost', methods =['POST'])
def process_data():
	req_data = json.loads(request.data)
	add_eye_tracking.create_heat_map(req_data)
	# print(req_data)
	# print("Returning: ", result)
	result = ""
	return result

@app.route('/assets/<path:subpath>')
def return_css_template(subpath):
    return send_from_directory('assets',subpath)

# @app.route('/main.css')
# def return_main_css():
#     # add_eye_tracking.add_tracking('./static/main.css')
#     return send_from_directory('static','main.css')

@app.route('/index.php')
def return_php():
    return render_template('index.php')

@app.route('/<path:subpath>')
def return_file(subpath):
    print(subpath)
    return send_from_directory('static',subpath)



if __name__ == '__main__':
   app.run(debug = True)

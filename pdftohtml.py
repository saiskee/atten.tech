import requests
from requests.auth import HTTPBasicAuth
import time
import zipfile
import os, sys, getopt

#api_key = '471f3a97a4ccc0f2d417369db65599e635097856'
#target_format = "html5"
#target_file = "target.zip"

def upload_pdf(sourceFile):
    file_content = {'source_file': open(sourceFile, 'rb')}
    endpoint = "https://api.zamzar.com/v1/jobs"
    api_key = '471f3a97a4ccc0f2d417369db65599e635097856'
    target_format = "html5"
    data_content = {'target_format': target_format}
    res = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
    print(res.json())
    json_data = res.json()
    job_id = json_data['id']
    print("Job (",job_id,") is being uploaded")
    return job_id
    #{'id': 5485718, 'key': '471f3a97a4ccc0f2d417369db65599e635097856', 'status': 'initialising', 'sandbox': True, 'created_at': '2019-04-06T19:23:00Z', 'finished_at': None, 'source_file': {'id': 48528556, 'name': 'us_doi.pdf', 'size': 980921}, 'target_files': [], 'target_format': 'html5', 'credit_cost': 1}

def job_done(job_id):
    api_key = '471f3a97a4ccc0f2d417369db65599e635097856'
    endpoint = "https://api.zamzar.com/v1/jobs/{}".format(job_id)
    response = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
    print(response.json()['status'])
    return response.json()

def download_html(job_id):
    api_key = '471f3a97a4ccc0f2d417369db65599e635097856'
    target_file = "target.zip"
    endpoint = "https://api.zamzar.com/v1/files/{}/content".format(job_id)
    response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
    try:
        with open(target_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()

        return ("File downloaded")

    except IOError:
        return ("Error")

def deleteStatic():
    filelist = [ f for f in os.listdir('./static') ]
    for f in filelist:
        os.remove(os.path.join('./static', f))

def pdfToHTML(sourceFile, relDir):
    print(sourceFile)
    target_file = "target.zip"
    job_id = upload_pdf(sourceFile)
    job_status = job_done(job_id)
    while (job_status['status'] != 'successful'):
        time.sleep(2)
        job_status = job_done(job_id)
    target = job_status['target_files'][0]
    print(download_html(target['id']))
    
    deleteStatic()

    zip_ref = zipfile.ZipFile(target_file, 'r')
    zip_ref.extractall("static")
    zip_ref.close()

    os.remove(target_file)
    
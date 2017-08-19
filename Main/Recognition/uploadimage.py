#!/usr/bin/python3

import requests, json, base64, re, os, threading, datetime, io
from requests.auth import HTTPBasicAuth
from pathlib import PurePath
from PIL import Image

def encode_image_from_file(image_filename):
    image = 'sample images/'+image_filename
    with open(image, 'rb') as image_file:
        payload = base64.b64encode(image_file.read())
    return payload

def get_tags(encoded_image, service, logfile=None):
    url = 'http://smartvision.aiam-dh.com:8080/api/v1.0'
    authorization = HTTPBasicAuth('demo3','hackathon6483')

    # upload an {}m.format( through the API:)
    payload = encoded_image
    r_upload = requests.post(
        url+'/tasks',
        auth=authorization,
        data=json.dumps({'service':service, 'image':str(payload)[2:-1]}),
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    )
    print(r_upload, r_upload.text, file=logfile)


    #find the ID of this image
    im_id = re.search(r'\d+$', r_upload.json()['task']['uri']).group(0)

    #run the analysis on the image
    r_run = requests.put(
        url+'/tasks/run/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'},
        data=json.dumps({'scanned':True})
    )
    print(r_run, r_run.text, file=logfile)
    print(im_id)

    # get the information from the analysis
    r_complete = requests.get(
        url+'/tasks/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'},
    )
    print(r_complete, r_complete.text, file=logfile)

    # delete the image on the server
    r_delete = requests.delete(
        url+'/tasks/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    )
    print(r_delete, r_delete.text, im_id, file=logfile)

    # find the required tags from the analysis
    return r_run.json()['task']

class tag_retriever(threading.Thread):
    def __init__(self, image_byte_array, method, return_keywords):
        self.image_file = base64.b64encode(image_byte_array)
        self.method = method
        self.returnkw = return_keywords
    def run(self, logfile=None):
        url = 'http://smartvision.aiam-dh.com:8080/api/v1.0/tasks'
        authorization = HTTPBasicAuth('demo3', 'hackathon6483')
    def upload(self, url, auth):
        self.r_upload = requests.post(
                url,
                auth=auth,
                data=json.dumps({'service':self.method, 'image':str(self.image_file)[2:-1]}),
                headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        )
        
if __name__ == '__main__':
    image = 'fridge contents.jpg'
    with Image.open('sample images/'+image) as im:
        im_byte_arr = io.BytesIO()
        im.save(im_byte_arr, format='JPEG')
        im_byte_arr = im_byte_arr.getvalue()
        im_byte_arr = base64.b64encode(im_byte_arr)
        result = get_tags(im_byte_arr, 'tagging3')['description']
        print(result)
        for tag in result:
            im.crop(*list(map(lambda x : x[1], re.findall(r'(Left|Top|Right|Bottom)=(\d+)', tag))))






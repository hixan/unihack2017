#!/usr/bin/python3

import requests, json, base64, re, os, threading, datetime, io
from requests.auth import HTTPBasicAuth
from pathlib import PurePath
from PIL import Image

'''
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
    return r_run.json()['task']'''

class Tag_retriever(threading.Thread):

    def __init__(self, image_byte_array, method, return_keywords):
        super().__init__()
        self.image_file = base64.b64encode(image_byte_array)
        self.method = method
        self.returnkw = return_keywords
        self.headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        self.auth = HTTPBasicAuth('demo3', 'hackathon6483')
        self.url = 'http://smartvision.aiam-dh.com:8080/api/v1.0/tasks'

    def run(self, logfile=None):
        print("starting upload for method: {}\nkeywords: {}\n...".format(self.method, self.returnkw), file=logfile)
        self.upload()
        print(self.r_upload.text, file=logfile)
        print("starting analysis for method: {}\nkeywords: {}\n...".format(self.method, self.returnkw), file=logfile)
        self.start_analysis()
        print(self.r_analysis.text, file=logfile)
        print("cleaning data for method: {}\nkeywords: {}\n...".format(self.method, self.returnkw), file=logfile)
        self.clean_server()
        print(self.r_delete.text, file=logfile)
        json = self.r_analysis.json()['task']
        if self.returnkw is None:
            self.rval = json
            return json
        rval = dict((item, json[item]) for item in self.returnkw)
        self.rval = rval
        return rval

    def upload(self):
        self.r_upload = requests.post(
                self.url,
                auth=self.auth,
                data=json.dumps({'service':self.method, 'image':str(self.image_file)[2:-1]}),
                headers=self.headers
        )
        self.im_id = re.search(r'\d+$', self.r_upload.json()['task']['uri']).group(0)

    def start_analysis(self):
        self.r_analysis = requests.put(self.url+'/run/'+self.im_id, auth=self.auth, headers=self.headers, data=json.dumps({'scanned':True}))

    def clean_server(self):
        self.r_delete = requests.delete(self.url+'/'+self.im_id, auth=self.auth, headers=self.headers)
        
def get_tags_text(image, outputfile):
    im_byte_arr = io.BytesIO()
    image.save(im_byte_arr, format='JPEG')
    im_byte_arr = im_byte_arr.getvalue()
    tag_retriever = Tag_retriever(im_byte_arr, 'tagging3', ['description'])
    print('\nprocessing {}...:'.format(image), file=outputfile)
    result = tag_retriever.run(open('NUL', 'w'))
    print('\nfound tags:\n{}'.format(result['description']))
    rval = {}
    for tag in result['description']:
        values = map(lambda x : int(x[1]), re.findall(r'(Left|Top|Right|Bottom)=(\d+)', tag))
        tag = re.search(r'(\w+) Bounding Box:', tag).group(1)
        cropped_byte_array = io.BytesIO()
        cropped = image.crop(values)
        cropped.save(cropped_byte_array, format='JPEG')
        cropped_byte_array = cropped_byte_array.getvalue()
        cropped_retriever = Tag_retriever(cropped_byte_array, 'fridge', ['description'])
        textresult = cropped_retriever.run(open('NUL', 'w'))
        print('Tag "{}" at {} came up with this text:\n"{}"'.format(tag, ','.join(map(str, values)), textresult['description']), file=outputfile)
        rval[tag] = textresult['description']
    return rval

if __name__ == '__main__':
    with Image.open('sample images/pantry2.jpg', 'r') as image_file:
        for key, value in get_tags_text(image_file, open('NUL', 'w')).items():
            print(key, '"'+value+'"')

    '''
    image = 'pantry4.jpg'
    outputfile = None
    with Image.open('sample images/'+image) as im:
        im_byte_arr = io.BytesIO()
        im.save(im_byte_arr, format='JPEG')
        im_byte_arr = im_byte_arr.getvalue()
        tag_retriever = Tag_retriever(im_byte_arr, 'tagging3', ['description'])
        result = tag_retriever.run()
        for tag in result['description']:
            values = map(lambda x : int(x[1]), re.findall(r'(Left|Top|Right|Bottom)=(\d+)', tag))
            tag = re.search(r'(\w+) Bounding Box:', tag).group(1)
            cropped_byte_array = io.BytesIO()
            cropped = im.crop(values)
            cropped.save(cropped_byte_array, format='JPEG')
            cropped_byte_array = cropped_byte_array.getvalue()
            cropped_retriever = Tag_retriever(cropped_byte_array, 'text1', ['description'])
            textresult = cropped_retriever.run(open('NUL', 'w'))
            print('Tag "{}" at {} came up with this text:\n{}'.format(tag, ','.join(map(str, values)), textresult), file=outputfile)
'''

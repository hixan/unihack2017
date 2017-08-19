#!/usr/bin/python3

import requests, json, base64, re, os, threading, datetime
from requests.auth import HTTPBasicAuth
from pathlib import PurePath

print('test')
def get_tags(image_filename, service='tagging3'):
    url = 'http://smartvision.aiam-dh.com:8080/api/v1.0'
    authorization = HTTPBasicAuth('demo3','hackathon6483')

    # upload an image through the API:

    image = 'sample images/'+image_filename
    with open(image, 'rb') as image_file:
        payload = base64.b64encode(image_file.read())
    r_upload = requests.post(
        url+'/tasks',
        auth=authorization,
        data=json.dumps({'service':service, 'image':str(payload)[2:-1]}),
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    )
    print(r_upload, r_upload.text)


    #find the ID of this image
    im_id = re.search(r'\d+$', r_upload.json()['task']['uri']).group(0)

    #run the analysis on the image
    r_run = requests.put(
        url+'/tasks/run/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'},
        data=json.dumps({'scanned':True})
    )
    print(r_run, r_run.text)
    print(im_id)

    # get the information from the analysis
    r_complete = requests.get(
        url+'/tasks/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'},
    )
    print(r_complete, r_complete.text)

    # delete the image on the server
    r_delete = requests.delete(
        url+'/tasks/'+im_id,
        auth=authorization,
        headers={'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    )
    print(r_delete, r_delete.text, im_id)

    # find the required tags from the analysis
    return zip(r_run.json()['task']['description'], r_run.json()['task']['confidence'], r_run.text)

if __name__ == '__main__':
    service = 'tagging3'
    with open('output-'+service+'.txt', 'w') as resultsfile:
        threadlock = threading.Lock()
        def print_tags(image_file):
            tags = get_tags(item)
            print('locking thread for {}'.format(item))
            threadlock.acquire()
            print('\n'+image_file, file=resultsfile)
            for tag in tags:
                print('\t', *tag, file=resultsfile)
            threadlock.release()
            print('releasing thread for {}'.format(item))
        for item in os.listdir(PurePath(os.path.realpath(__name__), '..', 'sample images')):
            print('starting thread at {}'.format(datetime.datetime.time(datetime.datetime.now())), file=resultsfile)
            newthread = threading.Thread(target=print_tags,args=(item,))
            newthread.start()
            

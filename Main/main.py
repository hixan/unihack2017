#!/usr/bin/python3

import os, json, io, re
from PIL import Image

import Main.Recognition.uploadimage as up
def get_recipes():
    with open('Main/Recipes_parser/Tests/basic_test_data.txt', 'r', encoding='utf8') as json_file:
        recipes = json.load(json_file)['somthing']
        print(recipes)
    image = 'upload.jpg'
    with Image.open('Main/upload.jpg', 'r') as image:
        im_byte_arr = io.BytesIO()
        image = image.convert("RGB")
        image.save(im_byte_arr, format='JPEG')
        im_byte_arr = im_byte_arr.getvalue()
        tag_retriever = up.Tag_retriever(im_byte_arr, 'tagging3', ['description'])
        with open('console.log', 'a') as logging_file:
            tag_retriever.run(logging_file)
        ingredients = tag_retriever.rval['description']
        threads = []
        for index, i in enumerate(ingredients):
            byte_arr = io.BytesIO()
            l, t, r, b = map(lambda x : int(x[1]), re.findall(r'(Left|Top|Right|Bottom)=(\d+)', i))
            cropped = image.crop((round(.95*l), round(.95*t), min(round(1.05*r), image.width-1), min(image.height, round(1.05*b))))
            cropped.save(byte_arr, format='JPEG')
            byte_arr = byte_arr.getvalue()
            threads.append(up.Tag_retriever(byte_arr, 'fridge', ['description']))
            threads[-1].start()
        # syncronize threads
        for thread in threads:
            thread.join()
        ingredients = [t.rval['description'] for t in threads]
    print(ingredients)

    ingredients.append('salt')
    ingredients.append('pepper')
    ingredients.append('spices')
    ingredients.append('butter')
    ingredients = set(ingredients)
    print(ingredients)
    rval = {}
    for recipe in recipes:
        to_add = False
        notfound = 0
        for ingredient in recipe['ingr']:
            #find if a word in tags for the fridge matches ingredient sentance
            for i in ingredients:
                print(i in ingredient)
                if i in ingredient:
                    found = True
                    break
            else:
                notfound += 1
        rval[notfound] = recipe
    return rval
    #print('rval: {}'.format(str(rval)))

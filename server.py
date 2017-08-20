from bottle import route, run, template, static_file, request, redirect
import os
from Main.main import get_recipes

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='Templates/static')

@route('/')
def home():
    return template("Templates/landing.tpl")

@route('/uploading', method='POST')
def upload():
    ingredient = request.forms.getall('ingredient')
    return redirect("/recipes")

@route('/about')
def upload():
    return template("Templates/about.tpl")

@route('/recipes')
def recipes():
    test_data_ingr = ["milk", "eggs", "flour", "rice", "ham", "bacon", "oil", "chicken", "buns"]
    test_data, ingredients = get_recipes()
    test_data_ingr = ingredients
    f = lambda x : x[1]-x[0]*.1
    test_data_ingr = sorted(test_data_ingr)
    test_data = sorted(test_data, key=f)
    for line in test_data:
        print(line)
        print(f(line))
    return template("Templates/recipes.tpl", recipes=test_data, ingredients=test_data_ingr[1::2])

@route('/upload', method='POST')
def do_upload():
    print(request)
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'
    save_path = os.path.join("./Main", "upload.jpg")
    upload.save(save_path, overwrite="TRUE") # appends upload.filename automatically
    return redirect("/recipes")

run(host='localhost', port=8080, debug=True)

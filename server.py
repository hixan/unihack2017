from bottle import route, run, template, static_file, request, redirect
import os

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='Templates/static')

@route('/')
def home():
    return template("Templates/landing.tpl")

@route('/index')
def index():
    return template("Templates/index.tpl")

@route('/uploading', method='POST')
def upload():
    ingredient = request.forms.getall('ingredient')
    print(ingredient)
    return redirect("/recipes")

@route('/about')
def upload():
    return template("Templates/about.tpl")

@route('/recipes')
def recipes():
    test_data = [{"title":"testing", "title-link":"www.google.com", "yield":"12", "picture":"https://bottlepy.org/docs/dev/_static/banner_webland.png"}, {"title":"testing", "title-link":"www.google.com", "yield":"12", "picture":"https://bottlepy.org/docs/dev/_static/logo_nav.png"}, {"title":"testing", "title-link":"www.google.com", "yield":"12", "picture":"https://bottlepy.org/docs/dev/_static/logo_nav.png"}]
    test_data_ingr = ["testing", "12", "wein", "milk", "egg", "flour"]
    return template("Templates/recipes.tpl", recipes=test_data, ingredients=test_data_ingr)

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

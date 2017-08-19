from bottle import route, run, template, static_file, request, redirect
import os

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='Templates/static')

@route('/home')
def home():
    return template("Templates/home.tpl")

@route('/index')
def index():
    return template("Templates/index.tpl")

@route('/upload')
def upload():
    return template("Templates/upload.tpl")

@route('/recipes')
def recipes():
    return template("Templates/recipes.tpl")

@route('/upload', method='POST')
def do_upload():
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = os.path.join("./", upload.filename)
    upload.save(save_path, overwrite="TRUE") # appends upload.filename automatically
    return redirect("/home")

run(host='localhost', port=8080, debug=True)

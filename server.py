from bottle import route, run, template, static_file

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='Templates/static')

@route('/home')
def hello():
    return template("Templates/home.tpl")

@route('/index')
def hello():
    return template("Templates/index.tpl")

@route('/upload')
def hello():
    return template("Templates/upload.tpl")

@route('/recipes')
def hello():
    return template("Templates/recipes.tpl")

run(host='localhost', port=8080, debug=True)

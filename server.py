from bottle import route, run, template, static_file, request

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

@route('/uploading', method='POST')
def do_upload():
    data = request.files.data
    if data and data.file:
        raw = data.file.read() # This is dangerous for big files
        filename = data.filename
        return "Hello You uploaded %s (%d bytes)." % (filename, len(raw))
    return "You missed a field."

run(host='localhost', port=8080, debug=True)

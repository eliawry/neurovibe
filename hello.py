from flask import Flask
app = Flask(__name__)


@app.route('/intensity/set/<int:intensity>')
def put_post(intensity):
    intensity = str(intensity)
    with open("test.txt", "wb") as fo:
        fo.write(intensity)
    return 'intensity set to ' + intensity


@app.route('/intensity/get')
def show_post():
    with open("test.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/leap/set/<int:leap>')
def put_leap(leap):
    leap = str(leap)
    with open("leap.txt", "wb") as fo:
        fo.write(leap)
    return 'leap set to ' + leap


@app.route('/leap/get')
def show_leap():
    with open("leap.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/is_on')
def is_it_on():
    with open("go.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/start')
def start_it():
    with open("go.txt", "wb") as fo:
        fo.write('LEAP')
    return """<!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" type="text/css" href="static/style.css">
            </head>
            <body>
            <div class="wrapper">
            <a href="/">
            <button type="button" onclick="">I'm satisfied!</button>
            </div>
            <embed src="http://cs.utexas.edu/~elie/hot.mp3" hidden='true'>
            </a>
            </body>
            </html>
            """


@app.route('/brain')
def start_brain():
    with open("go.txt", "wb") as fo:
        fo.write('BRAIN')
    return """<!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" type="text/css" href="static/style.css">
            </head>
            <body>
            <div class="wrapper">
            <a href="/">
            <button type="button" onclick="">I'm satisfied!</button>
            </div>
            <embed src="http://cs.utexas.edu/~elie/hot.mp3" hidden='true'>
            </a>
            </body>
            </html>
            """


@app.route('/')
def hello():
    with open("go.txt", "wb") as fo:
        fo.write('NO')
    return """<!DOCTYPE html>
            <html>
            <head>
            <link rel="stylesheet" type="text/css" href="static/style.css">
            </head>
            <body>
            <div class="wrapper">
            <a href="/brain">
            <button type="button" onclick="">Think it!</button>
            </a>
            <a href="/start">
            <button type="button" onclick="">Show it!</button>
            </a>
            <a href="/start">
            <button type="button" onclick="">Train it!</button>
            </a>
            </div>
            </body>
            </html>
            """


if __name__ == '__main__':
    app.run()

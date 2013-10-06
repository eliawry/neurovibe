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

if __name__ == '__main__':
    app.run()

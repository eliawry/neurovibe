from flask import Flask
app = Flask(__name__)


class IntensityTracker(object):
    def __init__(self):
        self.intensity = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/intensity/set/<int:intensity>')
def put_post(intensity):
    intensity = str(intensity)
    # intensity.save('intensity')
    # show the post with the given id, the id is an integer
    with open("test.txt", "wb") as fo:
        fo.write(intensity)
    return 'intensity set to ' + intensity


@app.route('/intensity/get')
def show_post():
    with open("test.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/projects/')
def projects():
    return 'The project page'

if __name__ == '__main__':
    app.run()

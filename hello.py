from flask import Flask
app = Flask(__name__)


class IntensityTracker(object):
    def __init__(self):
        self.intensity = 0


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/intensity/set/<int:intensity>')
def show_post(intensity):
    intensity = str(intensity)
    # intensity.save('intensity')
    # show the post with the given id, the id is an integer
    return 'intensity set to ' + intensity


# @app.route('/intensity/get')
# def show_post():
#     i = load('intensity')
#     # show the post with the given id, the id is an integer
#     return i


@app.route('/projects/')
def projects():
    return 'The project page'

if __name__ == '__main__':
    app.run()

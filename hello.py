from flask import Flask
app = Flask(__name__)


class IntensityTracker(object):
    def __init__(self):
        self.intensity = 0


@app.route('/alpha/set/<int:alpha>')
def put_alpha(alpha):
    alpha = str(alpha)
    with open("alpha.txt", "wb") as fo:
        fo.write(alpha)
    return 'alpha set to ' + alpha


@app.route('/alpha/get')
def show_alpha():
    with open("alpha.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/beta/set/<int:beta>')
def put_beta(beta):
    beta = str(beta)
    with open("beta.txt", "wb") as fo:
        fo.write(beta)
    return 'beta set to ' + beta


@app.route('/beta/get')
def show_beta():
    with open("beta.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/gamma/set/<int:gamma>')
def put_gamma(gamma):
    gamma = str(gamma)
    with open("gamma.txt", "wb") as fo:
        fo.write(gamma)
    return 'gamma set to ' + gamma


@app.route('/gamma/get')
def show_gamma():
    with open("gamma.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/delta/set/<int:delta>')
def put_delta(delta):
    delta = str(delta)
    with open("delta.txt", "wb") as fo:
        fo.write(delta)
    return 'delta set to ' + delta


@app.route('/delta/get')
def show_delta():
    with open("delta.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/theta/set/<int:theta>')
def put_theta(theta):
    theta = str(theta)
    with open("theta.txt", "wb") as fo:
        fo.write(theta)
    return 'theta set to ' + theta


@app.route('/theta/get')
def show_theta():
    with open("theta.txt", "rb") as fo:
        for line in fo:
            return line


@app.route('/attention/set/<int:attention>')
def put_attention(attention):
    attention = str(attention)
    with open("attention.txt", "wb") as fo:
        fo.write(attention)
    return 'attention set to ' + attention


@app.route('/attention/get')
def show_attention():
    with open("attention.txt", "rb") as fo:
        for line in fo:
            return line


if __name__ == '__main__':
    app.run()

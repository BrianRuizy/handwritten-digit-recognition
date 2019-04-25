from flask import Flask
import numpy as np
from scipy.misc import imsave, imread, imresize

app = Flask(__name__)


#  routing decorator
@app.route('/')
def index():
    return '<h1>this is the Homepage</h1>'


if __name__ == "__main__":
    app.run()

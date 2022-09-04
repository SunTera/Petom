import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import config

app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = config.UPLOAD_FOLDER
RESULT_FOLDER = config.RESULT_FOLDER

@app.route('/')
def index():  # put application's code here
    return render_template("about.html")


@app.route('/about')
def about():  # put application's code here
    return render_template("about.html")

@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'File is missing', 404

        f = request.files['file']

        if f.filename == '':
            return 'File is missing', 404

        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))
        return 'file uploaded successfully'
        # return render_template("detect.html", file=file, msg=True)
    else:
        return render_template("detect.html", msg=False)

def uploadAjax():
    pass

@app.route("/result")
def result():
    return render_template("result.html")

@app.route('/search_vet')
def search_vet():
    return render_template("search_vet.html")

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        file = request.form['file']
        return f'<p>{file}</p>'
    else: return render_template('test.html')


if __name__ == '__main__':
    app.run()

import datetime
import os
import shutil

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename, redirect

import config

app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = config.UPLOAD_FOLDER
RESULT_FOLDER = config.RESULT_FOLDER
STATIC_RESULT_FOLDER = config.STATIC_RESULT_FOLDER


@app.route('/')
def index():
    return render_template("about.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'File is missing', 404

        file = request.files['file']

        if file.filename == '':
            return 'File is missing', 404

        filename = secure_filename(file.filename)
        file_route = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_route) # 업로드된 파일 저장
        # detect #
        start = datetime.datetime.now()
        detect_result = os.system(
            f'python ./yolov5/detect.py --weights ./a5a6_100.pt --img 416 --conf 0.4 --source "{file_route}"')
        end = datetime.datetime.now()
        if detect_result == 0:
            print(end - start)
            result_img = os.path.join(RESULT_FOLDER, filename)
            shutil.copyfile(result_img, os.path.join(STATIC_RESULT_FOLDER, filename))
            return redirect(url_for('result', filename=filename))
        else:
            print(detect_result)
            return 'Sorry, Detection was not handled properly',404
        # return 'file uploaded successfully'

    else:
        return render_template("detect.html")

@app.route("/result")
def result():
    filename = request.args.get('filename')
    return render_template("result.html", filename=filename)


@app.route('/search_vet')
def search_vet():
    return render_template("search_vet.html")


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        file = request.form['file']
        return f'<p>{file}</p>'
    else:
        return render_template('test.html')


if __name__ == '__main__':
    app.run()

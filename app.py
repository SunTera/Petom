import datetime
import os
import shutil

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename, redirect
import requests, json

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
        file.save(file_route)
        # detect #
        detect_result = os.system(
            f'python ./yolov5/detect.py --weights ./yolov5/petom_weights.pt --img 640 --conf 0.4 --source "{file_route}"')
        if detect_result == 0:
            result_img = os.path.join(RESULT_FOLDER, filename)
            shutil.copyfile(result_img, os.path.join(STATIC_RESULT_FOLDER, filename))
            # os.system(f'rm "{result_img}" "{file_route}"') # 자동화로 해결하면 삭제
            return redirect(url_for('result', filename=filename))
        else:
            return 'Sorry, Detection was not handled properly', 404

    else:
        return render_template("detect.html")


@app.route("/result")
def result():
    filename = request.args.get('filename')
    return render_template("result.html", filename=filename)


def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        return {'lat': None, 'lng': None}
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}

    return crd


@app.route('/hospital')
def hospital():
    location = current_location()
    return render_template("hospital.html", lat=location['lat'], lng=location['lng'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')

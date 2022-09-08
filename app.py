import base64
import io
import torch
from PIL import Image
from flask import Flask, render_template, request
import requests, json

app = Flask(__name__, static_url_path='/static')

model = torch.hub.load('yolov5', 'custom', path='yolov5/petom_weights.pt', source='local')  # local repo


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

        im_file = request.files['file']

        if im_file.filename == '':
            return 'File is missing', 404

        im_bytes = im_file.read()
        img = Image.open(io.BytesIO(im_bytes))

        results = model(img)  # inference

        results.ims  # array of original images (as np array) passed to model for inference
        results.render()  # updates results.imgs with boxes and labels
        for img in results.ims:  # 'JpegImageFile' -> bytes-like object
            buffered = io.BytesIO()
            img_base64 = Image.fromarray(img)
            img_base64.save(buffered, format="JPEG")
            encoded_img_data = base64.b64encode(buffered.getvalue()).decode(
                'utf-8')  # base64 encoded image with results
            return render_template('result.html', img_data=encoded_img_data)
        else:
            return 'Sorry, Detection was not handled properly', 404

    else:
        return render_template("detect.html")

############## 임시 ################
@app.route("/result")
def result():
    return render_template("result.html")


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
    app.run(host='0.0.0.0', port=5000)

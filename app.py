import base64
import io
import torch
from PIL import Image
from flask import Flask, render_template, request, abort
import requests, json

app = Flask(__name__, static_url_path='/static')

model = torch.hub.load('ultralytics/yolov5', 'custom', path='models_train/petom_weights.pt', force_reload=True)


@app.route('/')
def index():
    return render_template("about.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    if request.method == 'POST':

        im_file = request.files['file']
        if im_file != '':
            im_bytes = im_file.read()
            img = Image.open(io.BytesIO(im_bytes))

            results = model(img, size=640)  # inference

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
            abort(404)

    else:
        return render_template("detect.html")



@app.route('/hospital')
def hospital():
    return render_template("hospital.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)

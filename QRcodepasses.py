import cv2 as cv
import datetime
import os
from PIL import Image
import io
import qrcode
import json
import base64
from flask import Flask, render_template, send_file, request

app = Flask(__name__)

time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%a-%d-%b-%y,%X")


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        form_data = request.form
        Arrival = f"{time_now}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(json.dumps(form_data))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_byte = io.BytesIO()
        img.save(img_byte, format='PNG')
        img_byte.seek(0)
        return send_file(img_byte, mimetype='image/png')

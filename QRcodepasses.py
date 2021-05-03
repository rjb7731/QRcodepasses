import cv2 as cv
import datetime
import os
from PIL import Image
import io
import qrcode
import json
from flask import Flask, render_template, send_file

app = Flask(__name__)

time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%a-%d-%b-%y,%X")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
data = {'Name': 'Joe Bloggs',
        'Mobile': "07739669145",
        'Arrival': f"{time_now}",
        'Vaccinated': "1st dose"}

qr.add_data(json.dumps(data))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img_byte = io.BytesIO()
img.save(img_byte, format='PNG')
img_byte.seek(0)
image = Image.open(img_byte)
image_display = image.show
# image.show()


@ app.route('/')
def display_qr():
    # return send_file(img_byte, mimetype='image/PNG')
    img_byte.seek(0)
    # return send_file(img_byte, mimetype='image/PNG')
    return render_template("index.html", user_image=img_byte)

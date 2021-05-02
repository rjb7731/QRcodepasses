import cv2 as cv
import datetime
import os
from PIL import Image
import io
import qrcode
import json
time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%a-%d-%b-%y, %X")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
data = {'name': 'Joe Bloggs',
        'mobile': "07739669145",
        'Arrival': f"{time_now}"}
qr.add_data(json.dumps(data))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img_byte = io.BytesIO()
img.save(img_byte, format='PNG')
image = Image.open(img_byte)
image.show()

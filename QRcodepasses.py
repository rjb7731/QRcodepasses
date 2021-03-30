"""To do:
-'Save' to BytesIO instead of locally
-Implement with Flask/Django site
"""

import qrcode
import cv2 as CV
import datetime
import os

time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%a-%d-%b-%y, %X")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('Name =Joe Bloggs ')
qr.add_data('Address= 1 Downing street, London, SW1 ')
qr.add_data(f'DateTime= {time_now} ')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("Test_sample.jpg")

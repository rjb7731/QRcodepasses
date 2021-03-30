import qrcode
import cv2 as CV
import datetime
import os

time_obj = datetime.datetime.now()
time_now = time_obj.strftime("%a-%d-%b-%y, %X")

img = qrcode.make(f"Name: Joe Bloggs,  Address: 1 Downing Street DateTime:{time_now}")
img.save("Test_sample.jpg")
#display(img)

im = cv.imread("Test_sample.jpg")
det = cv.QRCodeDetector()

retval, points, straight_qrcode = det.detectAndDecode(im)

print(retval)

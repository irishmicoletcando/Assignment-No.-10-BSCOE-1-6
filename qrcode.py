# Contact Tracing App
#     - Create a python program that will read QRCode using your webcam
#     - You may use any online QRCode generator to create QRCode
#     - All personal data are in QRCode 
#     - You may decide which personal data to include
#     - All data read from QRCode should be stored in a text file including the date and time it was read

# Note: 
#     - Search how to generate QRCode
#     - Search how to read QRCode using webcam
#     - Search how to create and write to text file
#     - Your source code should be in github before Feb 19
#     - Create a demo of your program (1-2 min) and send it directly to my messenger.

# source: https://towardsdatascience.com/building-a-barcode-qr-code-reader-using-python-360e22dfb6e5

import cv2
from pyzbar import pyzbar

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        a, b , c, d = qrcode.rect

        qrcode_info = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, "COVID CONTRACT TRACING", (a, b),(a+c, b+d), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, qrcode_info, (a + 6, b - 6), font, 2.0, (255, 255, 255), 1)
    

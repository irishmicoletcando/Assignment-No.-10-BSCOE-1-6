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

from datetime import datetime
import cv2
from pyzbar import pyzbar

def read_qrcodes(frame):
    qrcodes = pyzbar.decode(frame)
    for qrcode in qrcodes:
        a, b , c, d = qrcode.rect

        now = datetime.now()
        timestamp = datetime.timestamp(now)

        qrcode_info = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (a, b), (a+c, b+d), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "CONTRACT TRACING", (a + 6, b - 6), font, 2.0, (255, 255, 255), 1)

        with open("contracttracinginformation.txt", mode ='w') as file:
            file.write(qrcode_info + (f"\n\n\n\n\nDate and Time: {timestamp}"))
    return frame
    
def main():
    camera = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_qrcodes(frame)
        cv2.imshow('QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    camera.release()
    cv2.destroyAllWindows()

main()
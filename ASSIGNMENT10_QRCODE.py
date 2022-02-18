from sqlite3 import Time
import cv2
import numpy as np
import datetime
from pyzbar.pyzbar import decode 

Capture = cv2.VideoCapture(0)
Capture.set(3, 640)
Capture.set(4, 480)
Scanner = cv2.QRCodeDetector()

while True:
    _,img=Capture.read()
    data,one, _=Scanner.detectAndDecode(img)
    success, border = Capture.read()
    if data:
        scan=data
        break

    cv2.imshow("SHOW YOUR QRCODE",img)

    if cv2.waitKey(1)==ord("w"):
        break

    for code in decode(border):
        StoredInfo = open("PersonalInfo.txt", "w")
        StoredInfo.write(f"{code.data.decode('utf-8')}\n" ) 
        DateAndTime = datetime.datetime.now()
        StoredInfo.write(DateAndTime.strftime("Date: %y-%m-%d | Time: %H:%M:%S"))  
        StoredInfo.close()

Capture.release(scan)
cv2.destroyAllWindows()
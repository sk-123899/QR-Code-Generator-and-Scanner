import cv2
import webbrowser
import qrcode
from tkinter import *
window = Tk()
window.configure(bg="#A9A9A9")

window.geometry('550x550')

window.title("*****QRCode Scanner*****")
lbl0 = Label(window, text="SCANNING QRCODE",font=('ARIAL BOLD',20),fg="#20639B",bg="#A9A9A9").place(x=100,y=20)

lbl1 = Label(window,text="To Access QRCode Click ",font=('ARIAL BOLD',15),bg="#A9A9A9").place(x=50,y=90)

def video_reader():
    cam = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cam.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            print("QR Code detected-->", data)
            #a=StringVar()
            #a.set(data)
            #lbl2 = Label(window, textvariable=a , font=("ARIAL BOLD",20)).place(x=50,y=230)
            lbl3 = Label(window, text="QR Code detected", font=("ARIAL BOLD", 15),bg="#A9A9A9").place(x=50, y=210)
            lbl4 = Label(window,text="To Open QRCode link Click",font=("ARIAL BOLD",15),bg="#A9A9A9").place(x=50,y=330)

            def onClick():
                webbrowser.open(data, new=2)

            btn2=Button(window,text="OPEN LINK",command=onClick,bg="#173F5F",fg="#ffffff",font=("ARIAL BOLD", 10)).place(x=380,y=330)

            break
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()


#video_reader()

btn1 = Button(window,text="OPEN",command=video_reader,bg="#173F5F",fg="#ffffff",font=("ARIAL BOLD", 10)).place(x=380,y=90)

window.mainloop()

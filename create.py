
import qrcode
from tkinter import *
window = Tk()

window.geometry('550x500')
window.configure(bg="#A9A9A9")

window.title("*****QRCode Generator*****")
lbl0 = Label(window, text="GENERATING QRCODE",font=('ARIAL BOLD',20),fg="#20639B",bg="#A9A9A9").place(x=100,y=20)

img_name='med.png'
lbl1 = Label(window,text="Enter data for QRCode:-",font=('ARIAL BOLD',12),bg="#A9A9A9")
lbl1.place(x=25,y=100)
lbl2 = Label(window,text="Enter name by which qr image to be saved:-",font=('ARIAL BOLD',12),bg="#A9A9A9")
lbl2.place(x=25,y=180)
e1=Entry(window)
e1.place(x=400,y=100)
e2=Entry(window)
e2.place(x=400,y=180)

def generate():
    img=qrcode.make(e1.get())
    img.save(e2.get())
    img.show()

btn1 = Button(window,text="CREATE QR",command=generate,bg="#173F5F",fg="#ffffff").place(x=230,y=280)

window.mainloop()

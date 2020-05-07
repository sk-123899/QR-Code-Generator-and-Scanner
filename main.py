import webbrowser
from tkinter import messagebox
from tkinter import *
window = Tk()

window.geometry('720x600')
window.configure(bg="#A9A9A9")
window.title("*****QRCode Generator And Scanner*****")

lbl = Label(window,text="QRCODE GENERATOR AND SCANNER",font=("Rockwell Extra Bold",25),fg="#233067",bg="#A9A9A9").place(x=10,y=30)
lbl0 = Label(window, text="WELCOME",font=('ARIAL BOLD',20),fg="#20639B",bg="#A9A9A9")

lbl0.place(x=300,y=100)

lbl1 = Label(window, text="1. CREATE",font=('ARIAL BOLD',15),bg="#A9A9A9")

lbl1.place(x=120,y=190)

lbl2 = Label(window, text="2. SCAN",font=('ARIAL BOLD',15),bg="#A9A9A9")

lbl2.place(x=120,y=240)

lbl3 = Label(window, text="3. EXIT",font=('ARIAL BOLD',15),bg="#A9A9A9")

lbl3.place(x=120,y=290)

lbl4 = Label(window, text="Enter Your Choice",font=('ARIAL BOLD',15),bg="#A9A9A9")

lbl4.place(x=270,y=370)

entry1 = Entry(window)

entry1.place(x=295,y=420)
def onClick():
    while(TRUE):

        if (int(entry1.get())==1):
            import createTrial
        if (int(entry1.get())==2):
            import scanTrial
        if (int(entry1.get())==3):
            root = Tk()
            root.geometry('500x500')
            root.configure(bg="#A9A9A9")
            root.title("*****QRCode Generator And Scanner*****")
            lbal1 = Label(root,text="THANK YOU",font=("Rockwell Extra Bold",45),bg="#A9A9A9").place(x=50,y=50)
            lbal2 = Label(root, text="DEVELOPED BY:", font=("ARIAL BOLD", 20),bg="#A9A9A9").place(x=50, y=220)
            lbal3 = Label(root, text="SHREYAS KOTKAR  34", font=("Lucida Handwriting", 15),bg="#A9A9A9",fg="#20639B").place(x=50, y=280)
            lbal4 = Label(root, text="CHIRAG KINGER   31", font=("Lucida Handwriting", 15),fg="#20639B",bg="#A9A9A9").place(x=50, y=320)
            lbal5 = Label(root, text="SAURAV KALASKAR  27", font=("Lucida Handwriting", 15),fg="#20639B",bg="#A9A9A9").place(x=50, y=360)

            root.mainloop()
        else:
            messagebox.showwarning("QRCode", "Enter Correct Choice")
            #window.quit()
            window.deiconify()
            window.destroy()


btn1= Button(window, text="ENTER",command=onClick,bg="#173F5F",fg="#ffffff",font=("ARIAL BOLD", 10),height=1,width=10).place(x=310,y=470)

window.mainloop()

from tkinter import *
from PIL import Image,ImageTk

win=Tk()
win.title("Gallery")
win.geometry("604x575")
win.config(bg="white")
win.iconbitmap('images/Galleryico.ico')

img=ImageTk.PhotoImage(Image.open('images/universe.jpg').resize((600,500),Image.ADAPTIVE))
img1=ImageTk.PhotoImage(Image.open('images/cross.jpg').resize((600,500),Image.ADAPTIVE))
img2=ImageTk.PhotoImage(Image.open('images/tik.jpg').resize((600,500),Image.ADAPTIVE))
img3=ImageTk.PhotoImage(Image.open('images/images.jpeg').resize((600,500),Image.ADAPTIVE))
img4=ImageTk.PhotoImage(Image.open('images/python.jpeg').resize((600,500),Image.ADAPTIVE))
img5=ImageTk.PhotoImage(Image.open('images/images (1).jpeg').resize((600,500),Image.ADAPTIVE))

img_left=ImageTk.PhotoImage(Image.open('images/Sleft_arrow.png').resize((50,50),Image.ADAPTIVE))
img_right=ImageTk.PhotoImage(Image.open('images/Sright_arrow.png').resize((50,50),Image.ADAPTIVE))
exit_img=ImageTk.PhotoImage(Image.open('images/Exit.png').resize((200,50),Image.ADAPTIVE))

img_list=[img,
        img1,
        img2, 
        img3,
        img4,
        img5]

img_label=Label(win,image=img)
img_label.grid(row=0,column=0,columnspan=3)
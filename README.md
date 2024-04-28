# Simple-Gallery-GUI

In this code I made a simple Gallery code which shows how many photos are there and they slide as per the buttons clicked.

> [!Tip]
> ENJOY THE CODE

# UI:

![image](https://github.com/Student-Abhishekkumar/Simple-Gallery-GUI/assets/158078358/e6120a1a-96cf-4a1d-83e1-75dcf8b841b3)

## Main GUI CODE:-

```python
from tkinter import *
from customtkinter import *
from image import *
import customtkinter as ck

def forward(image_number):
    global img_label
    global left_arrow_btn
    global right_arrow_btn

    img_label.grid_forget()
    img_label=Label(image=img_list[image_number])

    left_arrow_btn=Button(win,borderwidth=0,bg="white",image=img_left,command=lambda: backward(image_number-1))
    right_arrow_btn=Button(win,borderwidth=0,bg="white",image=img_right,command=lambda: forward(image_number+1))

    if image_number==5:
        right_arrow_btn=Button(win,borderwidth=0,bg="white",image=img_right,state=DISABLED)

    img_label.grid(row=0,column=0,columnspan=3)
    left_arrow_btn.grid(row=1,column=0)
    right_arrow_btn.grid(row=1,column=2)

    count=Label(win,text="Image "+str(image_number+1)+" of " +str(len(img_list)),
            borderwidth=1,relief=SUNKEN,anchor=E,
            font=("Times of Roman",10,"bold")).grid(row=2,column=0,columnspan=3,sticky=E+W)

def backward(image_number):
    global img_label
    global left_arrow_btn
    global right_arrow_btn

    img_label.grid_forget()
    img_label=Label(image=img_list[image_number]) 

    left_arrow_btn=Button(win,borderwidth=0,image=img_left,bg="white",command=lambda: backward(image_number-1))
    right_arrow_btn=Button(win,borderwidth=0,image=img_right,bg="white",command=lambda: forward(image_number+1))

    if image_number==0:
        left_arrow_btn=Button(win,borderwidth=0,image=img_left,state=DISABLED,bg="white")

    img_label.grid(row=0,column=0,columnspan=3)
    left_arrow_btn.grid(row=1,column=0)  
    right_arrow_btn.grid(row=1,column=2)

    count=Label(win,text="Image "+str(image_number+1)+" of " +str(len(img_list)),
            borderwidth=1,relief=SUNKEN,anchor=E,
            font=("Times of Roman",10,"bold")).grid(row=2,column=0,columnspan=3,sticky=E+W)


left_arrow_btn=Button(win,borderwidth=0,image=img_left,state=DISABLED,bg="white").grid(row=1,column=0)
exit_btn=ck.CTkButton(win,border_width=2,text="EXIT",text_color="black",
                      font=("Algerian",37,"bold"),
                      fg_color="red",height=50,width=170,command=win.quit,
                      border_color="black").grid(row=1,column=1)
right_arrow_btn=Button(win,borderwidth=0,image=img_right,command=lambda: forward(1),bg="white").grid(row=1,column=2)

count=Label(win,text="Image 1 of " +str(len(img_list)),borderwidth=1,relief=SUNKEN,anchor=E,
            font=("Times of Roman",10,"bold")).grid(row=2,column=0,columnspan=3,sticky=E+W)

win.mainloop()
```

## Import file for images:-

```python
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
```

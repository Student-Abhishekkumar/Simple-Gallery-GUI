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
from tkinter import *
canvas_width=300
canvas_height=300
top=Tk()
canvas=Canvas(top,width=canvas_width,height=canvas_height)
canvas.grid(row=0,column=5)
img=PhotoImage(file="bus\b1.jpg")
canvas.create_image(60,60,anchor=NW,image=img)
b=Button(top,text="click",image=img)
b.grid(row=1,column=1)
top.mainloop()

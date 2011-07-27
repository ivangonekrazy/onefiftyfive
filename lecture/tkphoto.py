import tkFileDialog
from Tkinter import *
import Image, ImageTk

try:
    root = Tk()
    frame = Frame(root, width=500, height=500)
    frame.pack(expand=1)
    im = Image.open(tkFileDialog.askopenfilename() ) 
    canvas = Canvas(frame, height=im.size[1], width=im.size[0])

    photo = ImageTk.PhotoImage(im)
    item = canvas.create_image(0,0, anchor=NW, image=photo)
    canvas.pack(expand=1)
    root.mainloop()
except Exception, e:
    print e

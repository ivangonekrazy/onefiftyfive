from Tkinter import *

def responder():
    print "stop hitting me!"

root = Tk()
button = Button(root, text="Hit me!", command=responder)
button.pack()

mainloop()

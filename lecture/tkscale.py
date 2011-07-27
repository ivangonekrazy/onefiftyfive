import Tkinter

root = Tkinter.Tk()

scaleVar = Tkinter.IntVar()
scale = Tkinter.Scale(root, from_=0, to=100, variable=scaleVar, orient=Tkinter.HORIZONTAL)
scale.pack()

entry = Tkinter.Entry()
entry.pack()
entry.insert(0, "default value")

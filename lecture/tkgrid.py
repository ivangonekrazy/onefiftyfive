import Tkinter

root = Tkinter.Tk()
root.title("BMI")
#root.geometry("200x200")

lbl1 = Tkinter.Label(text="Height")
lbl1.grid(column=0,row=0)

scaleVar = Tkinter.IntVar()
scale = Tkinter.Scale(root, from_=0, to=100, variable=scaleVar, orient=Tkinter.HORIZONTAL)
scale.grid(column=1, row=0)

lbl2 = Tkinter.Label(root,text="Weight")
lbl2.grid(column=0,row=1)

entry = Tkinter.Entry(root,text="hello")
entry.insert(0, "default value")
entry.grid(column=1, row=1,padx=10,pady=10)

frame = Tkinter.Frame(root,borderwidth=2, relief='sunken')
text = Tkinter.Text(frame)
text.insert(Tkinter.END,"boo")

text.pack()
frame.grid(column=0, row=2, columnspan=2)

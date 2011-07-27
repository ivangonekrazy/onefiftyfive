from Tkinter import *
def responder():
    # kilos for weight and m for height
    w = float(weight.get() )
    h = float(height.get() )
    bmi = (w / h**2) 
    bmitext.insert(0, bmi )

# create all my widgets
root = Tk()
weight = Entry(root)
height = Entry(root)
weightlbl = Label(text="Weight:")
heightlbl = Label(text="Height:")
button = Button(root, text="BMI!", command=responder)
bmitext = Entry(root)

# layout my widgets
weight.grid(row=0, column=1)
height.grid(row=1, column=1)
weightlbl.grid(row=0, column=0)
heightlbl.grid(row=1, column=0)
button.grid(row=2, column=0, columnspan=2)
bmitext.grid(row=3, column=0, columnspan=2)

# loop to construct widgets
somewidget = []
for i in range(6):
    button = Button(root, text=str(i))
    somewidget.append(button)
    button.grid(row=4+i, column=0)

# gettin' rollin'
mainloop()

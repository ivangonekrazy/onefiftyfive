import Tkinter

root = Tkinter.Tk()

scrollbar = Tkinter.Scrollbar(root)
scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

listbox = Tkinter.Listbox(root)
listbox.pack(expand=1, fill=Tkinter.BOTH)

for i in range(100):
    listbox.insert(Tkinter.END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

root.mainloop()

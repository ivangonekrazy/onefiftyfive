import Tkinter

root = Tkinter.Tk()
root.title("Keycoder")

def reportEvent(event):
    print "keysym=%s, keysym_num=%s" % (event.keysym, event.keysym_num)

	
text = Tkinter.Text(root, width=20, height=5, highlightthickness=2)
text.bind('<KeyPress>', reportEvent)

text.pack(expand=1)
text.focus_set()

root.mainloop()

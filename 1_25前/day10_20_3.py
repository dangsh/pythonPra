from tkinter import *
root = Tk()
root.title("hello world")
root.geometry()


    
var = StringVar()
lb = Listbox(root,  listvariable = var)
list_item = [1, 2, 3, 4]         #控件的内容为1 2 3 4
for item in list_item:
    lb.insert(END, item)
lb.delete(2, 4)                  #此时控件的内容为1 3

lb.pack()
    
root.mainloop()
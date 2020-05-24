from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Files")
root.iconbitmap("C:/Users/borbe/Pictures/code.ico")


def open():
    global image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/borbe/Documents/", title="open a file", filetypes=(("png/jpg files", ("*.png", "*.jpg")),("all files", "*.*")))
    label = Label(root, text=root.filename).pack()
    image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(image=image).pack()


button = Button(root, text="open file", command=open).pack()

mainloop()

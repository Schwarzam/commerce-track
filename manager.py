from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from content import Client, StartPage

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side="top", fill='both', expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, Client):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()



app = App()
app.mainloop()

# image = Image.open("/Users/oliveira/IFinterface/3tree.png")

# my_img = ImageTk.PhotoImage(image)
# my_label = Label(image=my_img, text="tei")
# my_label.image = my_img
# my_label.pack()

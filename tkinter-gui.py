import tkinter
top = tkinter.Tk()
B1 = tkinter.Button(top, text ="error", bitmap="error", background="#00ffff", height="6c", width="6c")
B2 = tkinter.Button(top, text="hourglass", bitmap="hourglass", foreground="#ff0000",activeforeground="#ff00ff")
B1.pack()
B2.pack()
top.mainloop()
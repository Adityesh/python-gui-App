import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root,height = 700,width = 400,bg = "#243d45")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

button = tk.Button(root,text="Open App",padx=10,pady=5, fg="white", bg="#243d45")
button.pack()


runApp = tk.Button(root,text="Run App",padx=10,pady=5, fg="white", bg="#243d45")
runApp.pack()

root.mainloop()
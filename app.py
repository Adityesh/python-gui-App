import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(",")
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_chidlren():
        widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("executables","*.exe"),("all files","*.*")))

        apps.append(filename)

        for app in apps:
            label = tk.Label(frame,text="app",bg="gray")
            label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root,height = 700,width = 400,bg = "#243d45")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

button = tk.Button(root,text="Open App",padx=10,pady=5, fg="white", bg="#243d45",command = addApp)
button.pack()


runApp = tk.Button(root,text="Run App",padx=12,pady=5, fg="white", bg="#243d45",command = runApps)
runApp.pack()

for app in apps:
    label = tk.Label(frame,text=app)
    label.pack()

root.mainloop()

with open("save.txt",'w') as f:
    for app in apps:
        f.write(app + ',')
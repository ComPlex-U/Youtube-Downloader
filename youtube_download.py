import os
import tkinter import *
root = Tk()
root.geometry('400x200')
def runit():
    os.startfile('link.bat')

def downloadytv():
    with open('link.bat', 'w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
        down_load.close()
    runit()
f = tkinter.Frame(root)
f.grid()
Lable(f, text='===youtube video downloader====', font=15, padx=6).pack()
f1 = tkinter.Frame(root)
f1.grid()
Lable(f1, text='Enter link here',font=5).grid(row=1)
link = tkinter.StringVar()
tkinter.Entry(f1, font=5, textvariable=link).grid(row=1, column=1, pady=5, padx=10)
tkinter.Button(f1, text='Download', padx=50, relief=RAISED, font=10, borderwidth=5, command=downloadytv)
tkinter.Button.grid(column=1, paddy=5)

root.mainloop()
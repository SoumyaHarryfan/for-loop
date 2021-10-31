# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import*
root.Tk()
root.title("ASCII")
root.geometry("400x400")
enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label = Label(root,text="Name in ASCII",bg="light yellow",fg="black")
def ASCII_converter():
    input_word=enter_word.get()
    for letter in input_word:
        label["text"]+= str(ord(letter))+" "
        btn = Button(root,text="show name is ASCII",command=ASCII_converter,
                     bg='gold',fg='black')
        btn.place(relx=0.5,rely=0.5,anchor=CENTER)
        label.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
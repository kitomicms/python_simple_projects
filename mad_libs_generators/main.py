#!/usr/bin/env python3
# prompt user to input

from tkinter import *
root = Tk()
root.geometry('300x300')
root.title("Generator")
Label(root,text = 'have fun',font = 'calibre 20 bold').pack()
Label(root, text = 'Click any one:',font= 'calibre 15 bold').place(x=40,y=80)

def madlib():
	name = input("Enter your name:")
#print("Hello", name + "!")

	subject = input("what is your favourite class:")
	print("Hello", name, "my fav subject is ", subject)

Button(root, text = 'Click me', font = 'calibre 15', command=madlib, bg = 'ghost white').place(x=60, y=120)

root.mainloop()


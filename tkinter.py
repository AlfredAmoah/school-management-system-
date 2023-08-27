
from tkinter import *
root = Tk()
def ask():
    name = input('enter your name ')
    reference = input('please enter ur reference number')
    index = input('input your index number')

def search():
    search_key = input('enter student reference number to search')
mybutton1 = Button (root, text ='click', command = search)
mybutton2 = Button(root, text = 'click')
mybutton1.grid(row =0,column =1)
mybutton2.grid(row =0, column = 2)

root.mainloop()


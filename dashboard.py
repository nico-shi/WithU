from tkinter import *

window = Tk()
window.geometry('375x750')

window.title("Welcome to WithU")

searchBar = Entry(window, width = 20)

searchBar.grid(column = 1, row = 0)

def clicked():
    searchInput = searchBar.get()

searchBtn = Button(window, text = "Search", command=clicked)

searchBtn.grid(column=2, row=0)


window.mainloop()

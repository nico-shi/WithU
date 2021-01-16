from tkinter import *

window = Tk()
window.geometry('375x700')

window.title("WithU")
window.configure(background="#BEE7E8", bd=0)

heading = Label(window, text = "Discover new audios")
heading.configure(background="#BEE7E8", bd=0)
heading.place(x = 130, y=10)

searchBar = Entry(window, width = 20)

searchBar.place(x = 100, y=50)

def clicked():
    searchInput = searchBar.get()

searchBtn = Button(window, text = "Search", command=clicked)

searchBtn.place(x = 240, y=45)

#Buttons
photoLang = ""

#language 
languageBtn = Button(window, text="Language", bg="#A0D2DB", fg="#594157", font="Arial")
languageBtn.place(x=110.5, y=200)
languageBtn.config(height=3, width=13)

#person/relation
personBtn = Button(window, text="Relationship", bg="#A0D2DB", fg="#594157", font="Arial")
personBtn.place(x=110.5, y=300)
personBtn.config(height=3, width=13)

#location
locationBtn = Button(window, text="Location", bg="#A0D2DB", fg="#594157", font="Arial")
locationBtn.place(x=110.5, y=400)
locationBtn.config(height=3, width=13)

window.mainloop()
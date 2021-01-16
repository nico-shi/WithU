from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Frame, Label, Style

window = Tk()
window.configure(background="#BEE7E8", bd=0)

logo = Image.open("WithU_Logo.png")
logo1 = ImageTk.PhotoImage(logo.resize((300, 300)))
label = Label(image=logo1)

label.image = logo1
label.place(x=35, y=20)

#EXPLORE BUTTON
exploreButton = Button(window, text="Explore/Search", bg="#A0D2DB", fg="#594157", font="Arial")
exploreButton.grid(row=0, column=1)
exploreButton.place(x=95.5, y=390) #Change Placement
exploreButton.config(height=5, width=20)

#SAVED BUTTON
savedButton = Button(window, text="Saved/Favourites", bg="#A0D2DB", fg="#594157", font="Arial")
savedButton.grid(row=0, column=1)
savedButton.place(x=95.5, y=540) #Change Placement
savedButton.config(height=5, width=20)
window.geometry("375x700")
window.title("tinker test")

window.mainloop()

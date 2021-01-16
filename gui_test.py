from tkinter import *

main_window = Tk()

main_window.title("WithU")

main_window.geometry('375x812')

welcome_label = Label(main_window, text="Welcome to WithU", font=("Arial Bold", 35))

welcome_label.grid(column=0, row=0)

main_window.mainloop()
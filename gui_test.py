from tkinter import *

main_window = Tk()

main_window.title("WithU")

main_window.geometry('')

welcome_label = Label(main_window, text="Welcome to WithU", font=("Arial Bold", 50))

welcome_label.grid(column=0, row=0)

main_window.mainloop()
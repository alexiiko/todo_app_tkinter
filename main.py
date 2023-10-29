import tkinter as tk
from settings import WIDTH, HEIGHT, TITLE, ICON
from logic import add_todo

window = tk.Tk()

window.title(TITLE)
window.geometry(f"{WIDTH}x{HEIGHT}")
window.iconbitmap(ICON)

current_todo_label = tk.Label(master=window, text="Current TODOS")
current_todo_label.place(x=10, y=3)

add_todo(window)

window.mainloop()

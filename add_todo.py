import tkinter as tk


def add_todo(master):
    todo_counter = 0
    todo_list = []
    todo_area = tk.Frame(master=master)
    todo_area.place(x=5, y=35)

    def add_new_todo():
        nonlocal todo_counter
        if todo_counter < 18:

            def delete_todo():
                todo_frame.destroy()

                nonlocal todo_counter
                todo_counter -= 1
                todo_list.pop(todo_counter)

            def todo_done():
                todo_frame.destroy()

                nonlocal todo_counter
                todo_counter -= 1

            todo_counter += 1
            todo_frame = tk.Frame(master=todo_area)
            todo_list.append(todo_frame)

            todo_entry = tk.Entry(master=todo_frame)
            todo_entry.pack(side="left")

            todo_done_button = tk.Button(
                master=todo_frame, command=todo_done, text="Done"
            )
            todo_done_button.pack(side="left")

            todo_delete_button = tk.Button(
                master=todo_frame, command=delete_todo, text="Delete"
            )
            todo_delete_button.pack(side="left")

            todo_list[-1].pack()

    add_button = tk.Button(master=master, text="Add new todo", command=add_new_todo)
    add_button.place(x=110, y=0)

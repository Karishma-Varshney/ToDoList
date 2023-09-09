from tkinter import *
from tkinter import messagebox


# ----------------------ADDING MECHANISM--------------------------#
def add():
    tasks = task_input.get()
    if tasks == '':
        messagebox.showerror(title='Not Item Added', message='Please Add a task')
    else:
        task_list.insert(END, tasks)
        task_input.delete(0, END)


# ----------------------DELETION MECHANISM--------------------------#
def delete():
    d = task_list.curselection()
    if not d:
        messagebox.showerror(title='No Item Selected', message='Select task to delete.')
    else:
        task_list.delete(d)


# ----------------------EDITING MECHANISM--------------------------#
def edit():
    v = task_list.curselection()

    if not v:
        messagebox.showerror(title='No Item Selected', message='Select task to edit.')
    else:
        e = task_list.get(v)
        task_input.insert(0, string=e)
        task_input.focus()
        task_list.delete(v)


# ----------------------RESET MECHANISM--------------------------#
def reset():
    is_ok = messagebox.askyesno(title='Confirmation!!!!', message='Are you sure, you want to reset the list?')
    if is_ok:
        task_input.delete(0, END)
        task_list.delete(0, END)


# ----------------------UI SETUP--------------------------#
BACKGROUND_COLOR = '#7C73C0'

window = Tk()
window.title('To Do List')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# adding logo
canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=1, padx=10, pady=10)

# heading
heading = Label(text='To Do List', fg='#0b6ee6', font=('Times New Roman', 40, 'italic'), anchor=CENTER,
                bg=BACKGROUND_COLOR)
heading.grid(row=0, column=1)

# labels
add_label = Label(text='Write your Task:', font='20', bg=BACKGROUND_COLOR)
add_label.grid(row=2, column=0, padx=10, pady=10)

tasks_label = Label(text='Tasks :', font='20', bg=BACKGROUND_COLOR)
tasks_label.grid(row=3, column=0, padx=10, pady=10)

# entry
task_input = Entry(width=40)
task_input.grid(row=2, column=1)
task_input.focus()

task_list = Listbox()
task_list.grid(row=3, column=1)

# buttons
add_button = Button(text='ADD', fg='#2841e0', width=15, command=add)
add_button.grid(row=2, column=2, padx=10, pady=10)

del_button = Button(text='DELETE', fg='#2841e0', width=15, command=delete)
del_button.grid(row=4, column=0, padx=10, pady=10)

edit_button = Button(text='EDIT', fg='#2841e0', width=15, command=edit)
edit_button.grid(row=4, column=1, padx=15, pady=15)

reset_button = Button(text='RESET', fg='#2841e0', width=15, command=reset)
reset_button.grid(row=4, column=2, padx=15, pady=15)

window.mainloop()

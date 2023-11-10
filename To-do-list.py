import tkinter
import tkinter.messagebox
import pickle

root=tkinter.Tk()
default_font=("helvetica",10)
root.option_add("*font",default_font)
root.title("To do List")
root.geometry("400x400")
root.configure(bg="#BE3144")

#ADD TASK
def add_task():
    task = entry_task.get()
    placeholder_text = "Enter your task ---"

    if task != "" and task != placeholder_text:
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
        entry_task.insert(0, placeholder_text)  # Restore placeholder
        entry_task.configure(state='disabled', foreground='grey')  # Reset state and color

    else:
        tkinter.messagebox.showwarning(title="Warning!!!", message="You must enter a valid task")


#DELETE TASK
def delete_task():
    try:
        task=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task)
    except:
        tkinter.messagebox.showwarning(title="warning!!!",message="you must select a task")

    
#LOAD TASKS
def load_tasks():
    try:
        tasks=pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0,tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END,task)
    except:
        tkinter.messagebox.showwarning(title="warning!!!",message="cannot find tasks")

#SAVE TASKS
def save_tasks():
        tasks=listbox_tasks.get(0,listbox_tasks.size())
        pickle.dump(tasks,open("tasks.dat","wb"))

#EXIT WINDOW
def exit_window():
    root.destroy()


#create GUI

#header

header_label=tkinter.Label(root,text="To Do List",font=("times new roman",20,"bold"),bg="#1F1717",fg="white",height=1)
header_label.pack(fill="both",expand=True)

#frame1

frame_input=tkinter.Frame(root,bg="#BE3144")
frame_input.pack(pady=20)

def on_focus_in(entry):
    if entry.cget('state') == 'disabled':
        entry.configure(state='normal',foreground="black")
        entry.delete(0, 'end')


def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)
        entry.configure(state='disabled')
    
entry_task=tkinter.Entry(frame_input,width=40,bg="#F3EEEA",foreground="grey")
entry_task.insert(0,"Enter your task ---")
entry_task.configure(state='disabled')

x_focus_in = entry_task.bind('<Button-1>', lambda x: on_focus_in(entry_task))
x_focus_out = entry_task.bind('<FocusOut>', lambda x: on_focus_out(entry_task, 'Enter your task ---'))

entry_task.pack(side=tkinter.LEFT,padx=15)

button_add_task=tkinter.Button(frame_input,text="Add Task",command=add_task,bg="#1F1717",fg="white")
button_add_task.pack(side=tkinter.LEFT)

#frame2

frame_tasks=tkinter.Frame(root,bg="#BE3144")
frame_tasks.pack(pady=15)

listbox_tasks=tkinter.Listbox(frame_tasks,height=10,width=48,bg="#F3EEEA", selectbackground = "#B0A695", selectforeground = "black",selectmode="single" )
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks=tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT,fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

#frame3

frame_buttons=tkinter.Frame(root,bg="#BE3144")
frame_buttons.pack(pady=15)

button_delete_task=tkinter.Button(frame_buttons,text="Delete Task",command=delete_task,bg="#1F1717",fg="white")
button_delete_task.pack(side=tkinter.LEFT,padx=10)

button_load_tasks=tkinter.Button(frame_buttons,text="Load Tasks",command=load_tasks,bg="#1F1717",fg="white")
button_load_tasks.pack(side=tkinter.LEFT,padx=10)

button_save_tasks=tkinter.Button(frame_buttons,text="Save Tasks",command=save_tasks,bg="#1F1717",fg="white")
button_save_tasks.pack(side=tkinter.LEFT,padx=10)

button_save_tasks=tkinter.Button(frame_buttons,text="     Exit     ",command=exit_window,bg="#1F1717",fg="white")
button_save_tasks.pack(side=tkinter.LEFT,padx=10)


root.mainloop()




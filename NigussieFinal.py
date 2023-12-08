import tkinter as tk
import customtkinter as ctk
import random
import datetime
from tkinter import messagebox

def open_planner():
  '''creates the planner window'''
    global task_frame
    global task_frame2
    planner_window = ctk.CTk()
    planner_window.title = ('Planner app')
    planner_window.geometry("1366x768")
    planner_window.resizable(False, True)

    def your_name():
        '''returns users name as title of planner'''
        name = name_entry.get()
        title_label = ctk.CTkLabel(planner_window, text=f"{name}'s Daily Planner" , font=ctk.CTkFont(size=30, weight="bold"))
        title_label.place(relx=0.5, rely=0.0, anchor=ctk.N)

        name_entry.pack_forget()
        name_button.pack_forget()

    def daily_quotes(quote_list):
        '''reutrns a new quote daily'''
        day_of_year = datetime.datetime.now().timetuple().tm_yday
        quote_index = (day_of_year - 1) % len(quote_list)
        return quote_list[quote_index]

    quotes = [
            "The hardest choices require the strongest will.\n\tThanos",
            "Trust yourself, trust your power - that's how you stop it.\n\tDoctor Strange",
            "Just because something works, does not mean it can't be improved.\n\t Shuri\Black Panther",
            "The measure of a person, of a hero... is how well they succeed at being who they are.\n\tFrigga\End-game",
            "This story has been yours all along. You just didn't know it.\n\tLylla\Guardians of the galaxy",
            "No amount of money every bought a second of time.\n\tTony Stark",
            "Contrary to Popular Belief, I Know Exactly What I'm Doing.\n\tTony Stark",
            "What Is The Point Of Owning A Race Car If You Can’t Drive It?\n\tTony Stark",
            "With great power there must also come great responsibility!\n\tMarvel\Spider-man" ,
            "No matter how your day starts, always find time to make it great.\n\t Captain America",
            "Be strong you never know who you are inspiring.\n\tCaptain America",
            "The past is in the past but if you're over-analyzing or trying to repeat it. You are going to be stuck. \n\tCaptain America",
            "You can't always win but don't be afraid of making decisions.\n\t Tony Stark",
            "People without a vision for their future, always return to the past.\n\tBlack Widow",
            "Even if the whole world is telling you to move, it's your duty to plant yourself like a tree and say,'No, you move!'\n\tCaptain America"
            ]

    def add():
        '''creates a list of tasks from users input'''
        task = entry.get().strip()
        if task:
            tasks.append(task)
            entry.delete(0, tk.END)
            refresh_tasks()
        else:
            messagebox.showwarning("Task Manager", "Please enter a task.")

    def remove():
        '''removes selected tasks'''
        selected_tasks = [task for task, var in task_vars.items() if var.get()]
        if selected_tasks:
            for task in selected_tasks:
                tasks.remove(task)
                del task_vars[task]
            refresh_tasks()
            messagebox.showinfo("Task Manager", "Selected tasks removed successfully!")
        else:
            messagebox.showwarning("Task Manager", "Please select a task.")

    def completed():
        '''displays completed tasks'''
        selected_tasks = [task for task, var in task_vars.items() if var.get()]
        if selected_tasks:
            for task in selected_tasks:
                tasks.remove(task)
                tasks.append("[COMPLETED] " + task)
                del task_vars[task]
            refresh_tasks()
            messagebox.showinfo("Task Manager", "Task marked as completed successfully!")
        else:
            messagebox.showwarning("Task Manager", "Please select a task.")

    def refresh_tasks():
        '''updates the tasks according to users input'''
        global task_frame
        task_frame.destroy()
        task_frame = ctk.CTkFrame(main_frame)  # Use CTkFrame from customtkinter
        task_frame.pack(fill = 'both', expand = 'true')

        if show_completed.get():
            completed_tasks = [task for task in tasks if task.startswith("[COMPLETED]")]
            for task in completed_tasks:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(task_frame, text=task, variable=var)
                checkbox.pack(anchor=tk.W)
                task_vars[task] = var
        else:
            for task in tasks:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(task_frame, text=task, variable=var)
                checkbox.pack(anchor=tk.W)
                task_vars[task] = var

    def toggle_completed():
        '''toggle showing completed tasks'''
        refresh_tasks()

    def add_emotion():
        '''adds the entered text to emotion list and displays it in task_frame2'''
        emotion = entry2.get("1.0", tk.END).strip()
        if emotion:
            emotions.append(emotion)
            label_text = f"{len(emotions)}. {emotion}"  # Add the number prefix to the emotion text
            label = ctk.CTkLabel(task_frame2, text=label_text, wraplength=500)  # Adjust the wraplength as needed
            label.pack(anchor=tk.W)

            entry2.delete("1.0", tk.END)  # Clear the content of entry2

            # Adjusts the height of entry2 based on the number of lines of text 
            entry2_height = min(10, entry2.get("1.0", tk.END).count("\n") + 2)
            entry2.configure(height=entry2_height)

    def view():
        '''displays all entered text'''
        if not emotions:
            messagebox.showwarning("Journal", "No text entered.")
            return

        global task_frame2
        task_frame2.destroy()
        task_frame2 = ctk.CTkFrame(main_frame2, corner_radius=0)
        task_frame2.pack(fill='both', expand=True)

        for index, emotion in enumerate(emotions, start=1):
            label_text = f"{index}. {emotion}"  # Add the number prefix to the emotion text
            label = ctk.CTkLabel(task_frame2, text=label_text, wraplength=500)  # Adjust the wraplength as needed
            label.pack(anchor=tk.W)

        entry2.delete("1.0", tk.END)  # Clear the content of entry2
    
    # Gets the current date
    current_date = datetime.date.today()
    # Format the current date as "Day, Month Day Year"
    formatted_date = current_date.strftime("%A, %b %d %Y")

    #1st frame
    first_frame = ctk.CTkFrame(planner_window)
    name_entry = ctk.CTkEntry(first_frame, placeholder_text= "Your name")
    name_button = ctk.CTkButton(first_frame, text = "Enter your name", width = 50, command = your_name)
    #1st frame layout
    name_entry.pack(expand = 'true', padx = 3, pady = 3, ipadx = 500)
    name_button.pack(expand = 'true', padx = 3, pady = 3, ipadx = 300)
    first_frame.pack(fill = 'x')

    #2nd frame
    second_frame = ctk.CTkFrame(planner_window)
    right_frame = ctk.CTkFrame(second_frame)
    left_frame = ctk.CTkFrame(second_frame)

    #2nd frame layout
    right_frame.pack(padx = 10, pady = 10,side = 'right', expand = 'true', fill = 'both')
    left_frame.pack(padx = 10, pady = 10, side = 'left',  expand = 'true', fill = 'both')
    second_frame.pack(padx = 10, pady = 10, expand = 'true' , fill = 'both')

    #left frame 
    quote_frame = ctk.CTkFrame(left_frame, corner_radius=0)
    quote_label2 = ctk.CTkLabel(quote_frame, text= " Quote of the day! ", font= ctk.CTkFont(slant = 'italic', weight = 'bold', size = 20), corner_radius= 20 )
    daily_quote = daily_quotes(quotes)
    quote_label = ctk.CTkLabel(quote_frame, text=daily_quote, font= ctk.CTkFont(family = 'italic', weight = 'normal', size = 14))
    emot_frame = ctk.CTkFrame(left_frame, corner_radius=0)
    emot_label = ctk.CTkLabel(emot_frame, text = " How do you feel? ", font= ctk.CTkFont(family = 'italic', weight = 'bold', size = 20))
    entry2 = ctk.CTkTextbox(emot_frame, font= ctk.CTkFont(slant = 'roman', weight = 'normal'), corner_radius=  0, height = 5)
    main_frame2 = ctk.CTkScrollableFrame(emot_frame, corner_radius=0)
    task_frame2 = ctk.CTkFrame(main_frame2)
    emot_buttons = ctk.CTkFrame(emot_frame, corner_radius= 0 )
    addemotB = ctk.CTkButton(emot_buttons, text='Add', command = add_emotion) 
    rememotB = ctk.CTkButton(emot_buttons, text='View', command = view)  

    #left frame layout
    quote_frame.pack(padx = 20, pady = 5, fill = 'both') 
    quote_label2.pack(fill = 'x')
    quote_label.pack(pady = 20)
    emot_frame.pack(padx = 3, pady = 20, fill = 'both', expand = 'true')
    emot_label.pack()
    entry2.pack(fill ='x', pady = 6, padx = 10)
    main_frame2.pack(expand = 'true', fill ='both', pady = 5, padx = 10)
    task_frame2.pack(expand = 'true', fill ='both', pady = 5, padx = 10)
    emot_buttons.pack(side ='bottom', fill ='x')
    addemotB.pack(side = 'left' , padx = 10, pady = 10, fill = 'both', expand = 'true')
    rememotB.pack(side = 'left', padx = 10, pady = 10, fill = 'both', expand = 'true')

    #right frame 
    cal_frame = ctk.CTkFrame(right_frame, corner_radius=0)
    date_label = ctk.CTkLabel(cal_frame, text=formatted_date, font=ctk.CTkFont(family='italic', weight='normal', size=14))    
    todo_frame = ctk.CTkFrame(right_frame, corner_radius=0) 
    todo_label = ctk.CTkLabel(todo_frame, text = "To - Do List", font= ctk.CTkFont(family = 'italic', weight = 'bold', size = 20))
    entry = ctk.CTkEntry(todo_frame, placeholder_text=  'Add TO-DO', font= ctk.CTkFont(slant = 'roman', weight = 'normal'), corner_radius=  0)
    main_frame = ctk.CTkScrollableFrame(todo_frame, corner_radius=0)
    task_frame = ctk.CTkFrame(main_frame)
    todo_buttons = ctk.CTkFrame(todo_frame, corner_radius= 0)
    addtaskB = ctk.CTkButton(todo_buttons, text='Add', command=add) 
    remtaskB = ctk.CTkButton(todo_buttons, text='Remove', command=remove)  
    comptaskB = ctk.CTkButton(todo_buttons, text='Completed', command=completed)


    #right frame layout 
    cal_frame.pack(side = 'top', padx = 20, pady = 5, fill = 'both')
    date_label.pack(pady=20)
    todo_frame.pack(side = 'top', fill = 'both', expand = 'true', padx = 5)
    todo_label.pack(pady = 5)
    entry.pack(fill ='x', pady = 6, padx = 10)
    main_frame.pack(expand = 'true', fill ='both', pady = 3, padx = 10)
    task_frame.pack(expand = 'true', fill ='both')
    todo_buttons.pack(side ='bottom', fill ='x')
    addtaskB.pack(side = 'left' , padx = 10, pady = 10, fill = 'both', expand = 'true')
    remtaskB.pack(side = 'left', padx = 10, pady = 10, fill = 'both', expand = 'true')
    comptaskB.pack(side = 'left', padx = 10, pady = 10, fill = 'both', expand = 'true')

    #associated with to do 
    tasks = []
    show_completed = tk.BooleanVar()
    show_completed.set(False)
    task_vars = {}

    #associated with emotions 
    emotions = []

    planner_window.mainloop()

root = ctk.CTk() 
root.title = ('Planner app')
root.geometry("1366x768")
root.resizable(False, True)

# welcome page frame
welcome_frame = ctk.CTkFrame(root)
welcome_label = ctk.CTkLabel(welcome_frame, text='Welcome!', font=ctk.CTkFont(size=30, weight="bold"))
next_button = ctk.CTkButton(welcome_frame, text='Next', command=open_planner)

#welcome page layout
welcome_frame.pack(fill='both', expand=True)
welcome_label.pack(anchor = 'center', pady = 270)
next_button.pack(side = 'bottom',anchor = 'se')

root.mainloop()  


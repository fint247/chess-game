import tkinter as tk


count = 0
def add_new_frame(count):
        # if count == 1:
    new_frame = tk.Frame(window, bg="blue")  # Creating a new frame with a blue background
    new_frame.place(relwidth=1, relheight=1)  # Filling the entire window
    button = tk.Button(new_frame, text="Add New Frame", command= lambda: add_new_frame(count))
    button.pack(pady=10)
    # elif count == 1:
    #     new_frame2 = tk.Frame(window, bg="green")  # Creating a new frame with a blue background
    #     new_frame2.place(relwidth=1, relheight=1)  # Filling the entire window
    #     button = tk.Button(new_frame2, text="Add New Frame", command= lambda: add_new_frame(count))
    #     button.pack(pady=10)
    # else:
    #     new_frame3 = tk.Frame(window, bg="red")  # Creating a new frame with a blue background
    #     new_frame3.place(relwidth=1, relheight=1)  # Filling the entire window
    #     button = tk.Button(new_frame3, text="Add New Frame", command= lambda: add_new_frame(count))
    #     button.pack(pady=10)
    count +=1
    # button.config(state=tk.DISABLED)  # Disabling the button after adding the new frame

# Creating the main window
window = tk.Tk()
window.title("Tkinter Example")
window.geometry('500x600')

# Creating the initial frame with a red background
initial_frame = tk.Frame(window, bg="red")
initial_frame.place(relwidth=1, relheight=1)  # Filling the entire window

# Adding a button to add a new frame
button = tk.Button(window, text="Add New Frame", command= lambda: add_new_frame(count))
button.pack(pady=10)

window.mainloop()
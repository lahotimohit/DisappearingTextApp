from tkinter import *

message = ""
timer = None

border_color = '#D8D9DA'
background_color = '#272829'
foreground_color = '#FFF6E0'


def time_calculation(event):
    global message, timer

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "Backspace":
        message = message[0:len(message) - 1]

    elif event.char:
        message += event.char
        timer = window.after(5000, reset_app)


def reset_app():
    global timer, message
    typing_space.delete('1.0','end')
    message = ""
    timer=None
    return


def save_text():
    global message
    if message == "":
        return
    try:
        f = open('user_msg.txt', 'r')
    except FileNotFoundError:
        f = open('user_msg.txt', 'w')
        f.write(message)
        message = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = message
        else:
            text_to_write = f'\n{message}'

        with open('user_msg.txt', 'a') as f:
            f.write(text_to_write)
            message = ""
        return


heading = "Welcome to Disappearing Text App..."
instruction = "If you don't enter any key in 5 seconds your text automatically disappears."

window = Tk()
window.title("Disappearing Text App")
window.config(bg=background_color, padx=20, pady=20)


heading_main = Label(text=heading,
                     font=('Arial', 18, 'bold'),
                     fg=foreground_color,
                     background=background_color, pady=10, padx=10)
instruction_main = Label(text=instruction,
                         font=('Times New Roman', 14, 'italic'),
                         fg='#D8D9DA',
                         background=background_color,
                         pady=20)

typing_space = Text(font=('Arial', 14,'normal'),
                    pady=20, padx=10, width=100, height=10,
                    highlightcolor=border_color,
                    highlightbackground=border_color, highlightthickness=4)
typing_space.bind('<KeyPress>', time_calculation)

reset = Button(text='Reset', font=('Arial', 16, 'normal'),
               bg=background_color, fg=foreground_color, border=3,
               highlightbackground=foreground_color,
               highlightcolor=foreground_color,
               pady=6,
               padx=6,
               width=30,
               command=reset_app,
               highlightthickness=0)
save = Button(text='Save',
              width=30,
              command=save_text,
              pady=6,
              padx=6,
              font=('Arial', 16, 'normal'), bg=background_color,
              fg=foreground_color, border=3, highlightbackground=foreground_color,
              highlightcolor=foreground_color, highlightthickness=0)

heading_main.grid(row=0, column=0, columnspan=3)
instruction_main.grid(row=2, column=0, columnspan=3)
typing_space.grid(row=4, column=0, columnspan=3)
reset.grid(row=5, column=0)
save.grid(row=5, column=2)
window.mainloop()

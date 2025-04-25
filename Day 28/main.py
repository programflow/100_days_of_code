import tkinter
import time
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
DARKPURPLE = "#3D365C"
BLUE = "#5F99AE"
PINKPURPLE = "#C95792"
ORANGECREAM = "#F8B55F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


fg_reset = PINKPURPLE
fg_rest = ORANGECREAM
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps = 0
    check_mark_label.config(text= "")
    timer_label.config(text= "Timer", fg=fg_reset)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60

    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=fg_rest)

        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=fg_rest)
        countdown(short_break_sec)

    else:
        timer_label.config(text="Work",fg=BLUE)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    new_time = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=new_time)
    if count > 0:
        timer =window.after(1000, countdown, count -1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_mark_label["text"] = check_mark_label["text"] + "✔"



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=50, bg=DARKPURPLE)

fg = PINKPURPLE


canvas = Canvas(width=200, height=224, bg=DARKPURPLE,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=fg_reset, bg=DARKPURPLE, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_label = Label(text = "", fg = BLUE, bg=DARKPURPLE, font=(FONT_NAME, 30, "bold"), highlightthickness=0)
check_mark_label.grid(column=1, row=3)

window.mainloop()
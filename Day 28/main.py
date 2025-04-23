import tkinter
import time
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
DARKPURPLE = "#3D365C".lower()
BLUE = "#5F99AE".lower()
PINKPURPLE = "#C95792".lower()
ORANGECREAM = "#F8B55F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER = WORK_MIN*60
REPS = 2

# ---------------------------- TIMER RESET ------------------------------- #



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global TIMER
    countdown(TIMER)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = count // 60
    seconds = count % 60
    new_time = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=new_time)
    if count > 0:
        window.after(1000, countdown, count -1)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=50, bg=DARKPURPLE)

fg = BLUE


canvas = Canvas(width=200, height=224, bg=DARKPURPLE,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=fg, bg=DARKPURPLE, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark_label = Label(text = "✅", fg = BLUE, bg=DARKPURPLE, font=(FONT_NAME, 30, "bold"))
check_mark_label.grid(column=1, row=3)

window.mainloop()
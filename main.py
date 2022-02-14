import math
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
iterations = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(my_timer)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global iterations
    iterations = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global iterations

    iterations += 1
    if iterations % 2 == 1:
        count_time(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)
    else:
        if iterations == 8:
            count_time(LONG_BREAK_MIN * 60)
            timer.config(text="Break", fg=RED)
        else:
            count_time(SHORT_BREAK_MIN * 60)
            timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_time(counts):
    global my_timer

    minutes = math.floor(counts / 60)
    seconds = counts % 60

    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if counts > 0:
        my_timer = window.after(1000, count_time, counts - 1)
    else:
        start_timer()
        if iterations % 2 == 0:
            work_sessions = int(iterations / 2)
            check_label.config(text=work_sessions * "✔️")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label : Timer
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Courier", 35, "bold"), padx=30)
timer.grid(row=0, column=1)

# Canvas for photo
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=("Courier", 30, "bold"))
canvas.grid(row=1, column=1)

# Button to start timer

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Button to reset timer

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Label to check

check_label = tkinter.Label(fg=GREEN, bg=YELLOW, pady=30, font=("Courier", 20, "normal"))
check_label.grid(row=3, column=1)

window.mainloop()

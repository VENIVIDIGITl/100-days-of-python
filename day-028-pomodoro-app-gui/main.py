import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
DARK = "#292D3E"
PINK = "#e2979c"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, start_button
    reps = 0
    if timer:
        window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    start_button.config(state="normal")
    window.attributes('-topmost', 0)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, start_button
    start_button.config(state="disabled")
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg="Tomato")
        countdown(long_break_sec)
        focus_window("on")
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
        focus_window("on")
    elif reps == 1 or reps == 3 or reps == 5 or reps == 7:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)
        focus_window("off")
    else:
        title_label.config(text="Completed")
        canvas.itemconfig(timer_text, text="00:00")
        focus_window("on")
        window.bell()


def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    time_left = f"{count_min}:0{count_sec}" if count_sec < 10 else f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=time_left)
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        working_sessions = math.floor(reps/2)
        for _ in range(working_sessions):
            marks += "✓"
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("🍅 Pomodoro")
window.config(padx=25, pady=25, bg=DARK)

# Labels
title_label = tkinter.Label()
title_label.config(text="Timer", bg=DARK, fg=GREEN, font=(FONT_NAME, 28, "bold"))
title_label.grid(column=1, row=0)

check_marks = tkinter.Label()
check_marks.config(bg=DARK, fg=GREEN, font=(FONT_NAME, 36, "bold italic"), pady=10)
check_marks.grid(column=1, row=3)

# Buttons
start_button = tkinter.Button(text="Start", command=start_timer, highlightbackground=DARK)
start_button.config(fg=DARK, font=(FONT_NAME, 16, "bold"), padx=20, border=5)
start_button.grid(column=1, row=4)

reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightbackground=DARK)
reset_button.config(fg=DARK, font=(FONT_NAME, 16, "bold"), padx=20, border=5)
reset_button.grid(column=1, row=5)

# Canvas
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=DARK, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()

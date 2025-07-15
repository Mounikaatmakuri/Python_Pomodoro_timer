# ---------------------------- CONSTANTS ------------------------------- #
import tkinter
import math
from tkinter import Label

PINK = "#e2979c"
RED = "#e7305b"
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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 8:
        label1.config(text="long_break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0 :
        label1.config(text="short_break", fg=PINK)
        count_down(short_break_sec)

    else:
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)



    #count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
            label2.config(text="✔")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("POMORODO")
window.config(padx=100,pady=100,bg = YELLOW)

canvas = tkinter.Canvas(width=224, height=224,bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(110,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)


label1 = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,40))
label1.grid(column=2,row=1)

label2 = tkinter.Label(bg=YELLOW,fg=GREEN)
label2.grid(column=2,row=4)

button1 = tkinter.Button(text="start",highlightthickness=0,command=start_timer)
button1.grid(column=1,row=3)

button2 = tkinter.Button(text="reset",highlightthickness=0,command=reset_timer)
button2.grid(column=3,row=3)




window.mainloop()
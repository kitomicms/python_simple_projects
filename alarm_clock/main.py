# a simple alarm clock to pop up in the screen when time set is up

from tkinter import *
from datetime import datetime,timedelta
from playsound import playsound
def play():
    playsound('rotiCanai.mp3', block=False)

def alarm():
    
    # accept time input in minutes
    set_time = int(input("How many minutes you want? "))
    delta = timedelta(seconds=set_time)

    start_time = datetime.now()
    end_time = start_time + delta * 60

    # maybe add some sound
    # display label
    top = Tk()
    top.geometry("500x500")
    top.configure(background='red')
    top.lift()
    top.attributes('-topmost',True)

    text = Label(text=f"Time is up {delta}")
    text.config(font=("Courier, 30"))
    text.place(x=120,y=250)
    
    while True:
        if datetime.now() == end_time:
            play()
            top.mainloop()
            
            return False

if __name__ == "__main__":
    alarm()
            

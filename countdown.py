import tkinter
from tkinter import Label, StringVar
from threading import Thread
from datetime import datetime, timedelta
from time import sleep

# YYYY-MM-DD HH:MM
EVENT_START_TIME = '2021-10-05 22:00'

def update_label(win, remaining_time):
    event_time = datetime.strptime(EVENT_START_TIME, "%Y-%m-%d %H:%M")
    current_time = datetime.now()
    gap_seconds = int((event_time - current_time).total_seconds())
    while event_time > current_time:
        conversion = timedelta(seconds=gap_seconds)
        remaining_time.set(conversion)
        sleep(1)
        current_time = datetime.now()
        gap_seconds = int((event_time - current_time).total_seconds())
    remaining_time.set("00:00:00")
    win.quit()


class Win(tkinter.Tk):

    def __init__(self,master=None):
        tkinter.Tk.__init__(self,master)
        self.overrideredirect(True)
        self._offsetx = 0
        self._offsety = 0
        self.bind('<Button-1>',self.clickwin)
        self.bind('<B1-Motion>',self.dragwin)

    def dragwin(self,event):
        x = self.winfo_pointerx() - self._offsetx
        y = self.winfo_pointery() - self._offsety
        self.geometry('+{x}+{y}'.format(x=x,y=y))

    def clickwin(self,event):
        self._offsetx = event.x
        self._offsety = event.y


win = Win()
win.attributes('-topmost', True)
remaining_time = StringVar()
l = Label(win, textvariable=remaining_time, font=("Arial",55), bg='#0ff', fg='#05f')
l.pack()
t_update_lable = Thread(target=update_label, args=(win, remaining_time, ), daemon=True)
t_update_lable.start()
win.mainloop()

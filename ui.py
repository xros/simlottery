#!/usr/bin/env python2

from Tkinter import *
from lottery import RandomLottery

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

        self.get_lottery_number = Button(frame, text="Lottery", command=self.get_lottery_number)
        self.get_lottery_number.pack(side=RIGHT)

    def say_hi(self):
        print "hi there, everyone!"

    def get_lottery_number(self):
        print(RandomLottery().get_number_list())

root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below

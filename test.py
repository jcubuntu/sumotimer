from tkinter import *
import tkinter.messagebox as tkMessageBox
import time


def Display_info():
    Title = Label(root, text="BANGKOK ROBOTICS CHALLENGE 2019", font=("arial", 40), fg="white", bg="black")
    Title.pack(side=TOP)
    GamesTiltle = Label(root, text="Line Tracing LEGO", font=("arial", 40), fg="white", bg="black")
    GamesTiltle.pack(side=TOP)

def Main():
#Initial Tk and config Display
    global root
    root = Tk()
    root.title("BRC2019 Line Tracing LEGO")
    root.config(bg="black")
    width = 1024
    height = 768
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    Display_info()
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
#Key Input Control
    root.bind('<s>',stopWatch.Start)
    root.bind('<f>',stopWatch.Stop)
    

#Display 
    root.wm_attributes('-fullscreen','true')
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.mainloop() 

class StopWatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.timestr = StringVar()
        self.timeOut = 60*3
        self.onRunning = 0.0
        self.nextTime = 0.0
        self.startTime = 0.0
        self.MakeWidget()
    
    def MakeWidget(self):
        self.timeText = Label(self, textvariable=self.timestr, font=("times new roman",220), fg="green", bg="black")
        self.SetTime(self.nextTime)

    def Updater(self):
        self.nextTime = self.startTime-time.time()
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
    
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)
        self.timestr.set('%01d:%02d:%02d' % (minutes,seconds, miliSeconds))

    def Start(self,event=""):
        if not self.onRunning:
            self.startTime = time.time()
            self.nextTime = self.startTime - time.time()
            self.Updater()
            self.onRunning = 1
    
    def Stop(self,event=""):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = self.startTime - time.time()   
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Reset(self):
        self.after_cancel(self.timer)
        self.onRunning = 0




if __name__ == '__main__':
    Main()
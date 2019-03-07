from tkinter import *
import tkinter.messagebox as tkMessageBox
import time


def Main():
    global root
    root = Tk()
    root.title("BRC 2019 (Sumo Open Hardware)")
   
    width = 1024
    height = 768
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    
    Top = Frame(root, width=800)
    Top.pack(side=TOP)

    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    root.bind('<s>',stopWatch.Start)
    root.config(bg="black")
    gamename = Label(Top, text="LINE TRACING OPEN HARDWARE", font=("arial", 40), fg="white", bg="black")
    gamename.pack(fill=X)
    
    Bottom = Frame(root, width=600, bg="black")
    Bottom.pack(side=BOTTOM)
    #Start =  Button(Bottom, text='Start', command=stopWatch.Start, width=15, height=5,fg="white", bg="black")
    #Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=15, height=5, fg="white", bg="black")
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=15, height=5, fg="white", bg="black")
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=15, height=5, fg="white", bg="black")
    Exit.pack(side=LEFT)
    Title = Label(Top, text="BANGKOK ROBOTICS CHALLENGE 2019", font=("arial", 40), fg="white", bg="black")
    Title.pack()
    

    root.wm_attributes('-fullscreen','true')
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.mainloop() 
    

class StopWatch(Frame):  
# Initialize the Main Function of the Stopwatch                                     
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.TimerStart = 0.0        
        self.nextTime = 0.0
        self.onRunning = 0
        self.battleTime = FALSE   
        self.timestr = StringVar()   
        self.MakeWidget()      
 
# Create the widget of the Stopwatch Timer
    def MakeWidget(self):                      
        self.timeText = Label(self, textvariable=self.timestr, font=("times new roman",220), fg="green", bg="black")
        self.SetTime(self.nextTime)
        self.timeText.pack(fill=X, expand=NO, pady=0, padx=0) 
        self.timeOutText = Label(self, text="TIME UP", font=("times new roman",220), fg="RED", bg="black")
        self.timeOutText.pack(fill=X, expand=NO, pady=0, padx=0) 
        self.timeOutText.pack_forget()            
 
# Continously Update The Time From Counting
    def Updater(self): 
            self.nextTime = time.time-self.startTime()
            self.SetTime(self.nextTime)
            if self.nextTime < 180 :
                self.timer = self.after(50, self.Updater)
            else:
                self.timeText.pack_forget()
                self.timeOutText.pack(fill=X, expand=NO, pady=0, padx=0)
      
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)
        self.timestr.set('%01d:%02d:%02d' % (minutes,seconds, miliSeconds))
     
    def Start(self,event=""):                                                     
        if not self.onRunning:
            self.startTime = time.time()
            self.nextTime = time.time() - self.startTime            
            self.Updater()
            self.onRunning = 1 
           
    def Stop(self):                                    
        if self.onRunning:
            self.after_cancel(self.timer)            
            self.nextTime = time.time - self.startTime   
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Resume(self):
            self.startTime = time.time()
            self.nextTime = self.startTime-time.time()
            self.Updater()
            self.onRunning = 1
 
    def Exit(self):
        result = tkMessageBox.askquestion('Bangkok Robotics Challenge 2019', 'Are you sure you want to exit?', icon='warning')
        if result == 'yes':
            root.destroy()
            exit()
 
# Reset The Timer When Reset Button Is Clicked
    def Reset(self): 
        self.after_cancel(self.timer) 
        self.battleTime = FALSE
        self.onRunning = 0                                
        self.startTime = time.time()         
        self.nextTime = 0 
        self.SetTime(self.nextTime)
        self.timeOutText.pack_forget()
        self.TimerStart = 0
        self.timeText.pack(fill=X, expand=NO, pady=0, padx=0)

if __name__ == '__main__':
    Main()

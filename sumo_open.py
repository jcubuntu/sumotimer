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
    
    root.config(bg="black")
    gamename = Label(Top, text="", font=("arial", 40), fg="white", bg="black")
    gamename.pack(fill=X)
    
    Bottom = Frame(root, width=600, bg="black")
    Bottom.pack(side=BOTTOM)
    Start =  Button(Bottom, text='Start', command=stopWatch.Start, width=15, height=5,fg="white", bg="black")
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Pause', command=stopWatch.Stop, width=15, height=5, fg="white", bg="black")
    Stop.pack(side=LEFT)
    resume = Button(Bottom, text='Resume', command=stopWatch.Resume, width=15, height=5, fg="white", bg="black")
    resume.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=15, height=5, fg="white", bg="black")
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=15, height=5, fg="white", bg="black")
    Exit.pack(side=LEFT)
    Title = Label(Top, text="Time Remain", font=("arial", 40), fg="white", bg="black")
    Title.pack()
    

    root.wm_attributes('-fullscreen','true')
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.mainloop() 
    

class StopWatch(Frame):  
# Initialize the Main Function of the Stopwatch                                     
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.TimerStart = 5.0        
        self.nextTime = 5.0
        self.onRunning = 0
        self.battleTime = FALSE   
        self.timestr = StringVar()   
        self.MakeWidget()      
 
# Create the widget of the Stopwatch Timer
    def MakeWidget(self):                      
        self.timeText = Label(self, textvariable=self.timestr, font=("times new roman",220), fg="green", bg="black")
        self.SetTime(self.nextTime)
        self.timeText.pack(fill=X, expand=NO, pady=0, padx=0) 
        self.battleText = Label(self, text="BATTLE", font=("times new roman",60), fg="orange", bg="black")
        self.battleText.pack(fill=X, expand=NO, pady=0, padx=0)
        self.waitText = Label(self, text="WAIT START", font=("times new roman",60), fg="orange", bg="black")  
        self.waitText.pack(fill=X, expand=NO, pady=0, padx=0)  
        self.timeOutText = Label(self, text="TIME UP", font=("times new roman",220), fg="RED", bg="black")
        self.timeOutText.pack(fill=X, expand=NO, pady=0, padx=0) 
        self.battleText.pack_forget()
        self.timeOutText.pack_forget()
        self.waitText.pack_forget()                
 
# Continously Update The Time From Counting
    def UpdaterCoundown(self): 
            self.nextTime = self.startTime-time.time()
            self.SetTime(self.nextTime)
            if self.nextTime > -0.001 :
                self.timer = self.after(50, self.UpdaterCoundown)
            else :
                if not self.battleTime :
                    self.after_cancel(self.timer)               
                    self.SetTime(0)
                    self.onRunning = 0
                    self.battleTime = TRUE
                    self.TimerStart = 15*60
                    self.waitText.pack_forget()
                    self.Start()
                else :
                    self.SetTime(0)
                    self.battleText.pack_forget()
                    self.timeText.pack_forget()
                    self.timeOutText.pack(fill=X, expand=NO, pady=0, padx=0)
      
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*10)
        if not self.battleTime :                
            self.timestr.set('%01d:%01d' % (seconds, miliSeconds))
        else :
            self.timestr.set('%01d:%02d:%01d' % (minutes,seconds, miliSeconds))
     
    def Start(self,event=""):                                                     
        if not self.onRunning:
            self.startTime = time.time()+self.TimerStart
            self.nextTime = self.startTime-time.time()
            if self.battleTime :
                self.battleText.pack(fill=X, expand=NO, pady=0, padx=0)
            else :
                self.waitText.pack(fill=X, expand=NO, pady=0, padx=0)             
            self.UpdaterCoundown()
            self.onRunning = 1 
           
    def Stop(self):                                    
        if self.onRunning:
            self.after_cancel(self.timer)            
            self.nextTime = self.startTime - time.time()   
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Resume(self):
            self.startTime = time.time()+self.nextTime
            self.nextTime = self.startTime-time.time()
            self.UpdaterCoundown()
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
        self.nextTime = 5   
        self.SetTime(self.nextTime)
        self.battleText.pack_forget()
        self.timeOutText.pack_forget()
        self.waitText.pack_forget()
        self.timeText.pack_forget()
        self.TimerStart = 5
        self.timeText.pack(fill=X, expand=NO, pady=0, padx=0)

if __name__ == '__main__':
    Main()

from tkinter import *
import tkinter.messagebox as tkMessageBox
import time


def Main():
    global root
    root = Tk()
    root.title("SUMO ROBOT (OPEN HARDWARE)")
    width = 1024
    height = 768
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.wm_attributes('-fullscreen','true')
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=800)

    Top.pack(side=TOP)

    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    root.config(bg="black")
    Bottom = Frame(root, width=600, bg="black")
    Bottom.pack(side=BOTTOM)
    Start =  Button(Bottom,  fg="black",text='Start', command=stopWatch.Start, width=10, height=0,bg="black")
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', command=stopWatch.Stop, width=10, height=0, bg="black")
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text='Reset', command=stopWatch.Reset, width=10, height=0, bg="black")
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Exit', command=stopWatch.Exit, width=10, height=0, bg="black")
    Exit.pack(side=LEFT)
    Title = Label(Top, text="Bangkok Robotics Challenge 2019", font=("arial", 40), fg="white", bg="black")
    Title.pack()
    gamename = Label(Top, text="SUMO OPEN HARDWARE", font=("arial", 40), fg="white", bg="black")
    gamename.pack(fill=X)
    
    
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
        self.timeText = Label(self, textvariable=self.timestr, font=("times new roman",300), fg="green", bg="black")
        self.SetTime(self.nextTime)
        self.timeText.pack(fill=X, expand=NO, pady=0, padx=0) 
        self.battleText = Label(self, text="BATTLE", font=("times new roman",60), fg="orange", bg="black")
        self.battleText.pack(fill=X, expand=NO, pady=0, padx=0)
        self.waitText = Label(self, text="WAIT START", font=("times new roman",60), fg="orange", bg="black")  
        self.waitText.pack(fill=X, expand=NO, pady=0, padx=0)  
        self.timeOutText = Label(self, text="TIME OUT", font=("times new roman",80), fg="RED", bg="black")
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
                    self.TimerStart = 60*2
                    self.waitText.pack_forget()
                    self.Start()
                else :
                    self.SetTime(0)
                    self.battleText.pack_forget()
                    self.timeOutText.pack(fill=X, expand=NO, pady=0, padx=0)

     
# Set The Value of Time When Is Called    
    def SetTime(self, nextElap):
        minutes = int(nextElap/60)
        seconds = int(nextElap - minutes*60.0)
        miliSeconds = int((nextElap - minutes*60.0 - seconds)*100)
        if not self.battleTime :                
            self.timestr.set('%01d:%02d' % (seconds, miliSeconds))
        else :
            self.timestr.set('%01d:%02d:%02d' % (minutes,seconds, miliSeconds))
 
# Start The Stopwatch Counting When Button Start Is Clicked        
    def Start(self):                                                     
        if not self.onRunning:
            self.startTime = time.time()+self.TimerStart
            self.nextTime = self.startTime-time.time()
            if self.battleTime :
                self.battleText.pack(fill=X, expand=NO, pady=0, padx=0)
            else :
                self.waitText.pack(fill=X, expand=NO, pady=0, padx=0)             
            self.UpdaterCoundown()
            self.onRunning = 1 
           
 
# Stop The Stopwatch Counting When Button Stop Is Clicked
    def Stop(self):                                    
        if self.onRunning:
            self.after_cancel(self.timer)            
            self.nextTime = self.startTime - time.time()   
            self.SetTime(self.nextTime)
            self.onRunning = 0
 
# Close The Application When Exit Button Is Clicked
    def Exit(self):
        result = tkMessageBox.askquestion('Sourcecodester', 'Are you sure you want to exit?', icon='warning')
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
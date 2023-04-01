from tkinter import *
from pygame import mixer
mixer.init()
import os
#os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
root=Tk()
root.geometry("500x500")
def Play():
	b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\jitni.mp3"
	mixer.music.load(b)
	mixer.music.play()

def Pause():
	mixer.music.pause() 




play=Button(root,text="Play",height=5,width=8,command=Play)
play.pack(side=LEFT)
pause=Button(root,text="Pause",height=5,width=8,command=Pause)
pause.pack(side=LEFT)



root.mainloop()

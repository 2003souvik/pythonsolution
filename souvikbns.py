from tkinter import *
from pygame import mixer
mixer.init()
import os
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
root=Tk()
root.geometry("600x600")
l=Text(root)


#creating the list of songs
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
songs_list=os.listdir()
length_of_songsList=len(songs_list)


#creating a default variables
default_song=100
if songs_list==[]:
	playing_loop=-1
else:
	playing_loop=0
volume=0.5


#function to play the default_song
def Play():
	global songs_list,default_song,current_song
	if default_song==100:
		if songs_list!=[]:
			b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+songs_list[0]
			mixer.music.load(b)
			mixer.music.play()
			current_song=True
			default_song=0
	
def Pause():
    mixer.music.pause()
	
def Unpause():
    mixer.music.unpause()
	


#creating a funtion for next song
def next_song():
	global playing_loop,current_song,default_song,length_of_songsList
	if playing_loop<length_of_songsList-1:
		playing_loop+=1
	else:
		playing_loop=0
	b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+songs_list[playing_loop]
	mixer.music.load(b)
	mixer.music.play()
	current_song=True
	default_song=0
	
#creating a function for previous song
def previous_song():
	global playing_loop,current_song,default_song
	if playing_loop>0:
		playing_loop-=1
	else:
		playing_loop=length_of_songsList-1
	b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+songs_list[playing_loop]
	mixer.music.load(b)
	mixer.music.play()
	current_song=True
	default_song=0

#volume functions
def vol_up():
	global volume
	if volume==1.0:
		pass
	else:
		volume=volume+0.1
		mixer.music.set_volume(volume)

def vol_down():
	global volume
	if volume==0.0:
		pass
	else:
		volume=volume-0.1
		mixer.music.set_volume(volume)

l = Label(root, text = "MUSIC SYSTEM",fg="black")
l.config(font =("Courier", 14))

#buttons program
Previous_Song=Button(root,text="< Previous",height=3,width=2,command=previous_song)
Previous_Song.pack(side=LEFT,expand=True,fill="x")
Play=Button(root,text="Play",height=3,width=2,command=Play)
Play.pack(side=LEFT,expand=True,fill="x")
Pause=Button(root,text="Pause",height=3,width=2,command=Pause)
Pause.pack(side=LEFT,expand=True,fill="x")
Unpause=Button(root,text="Unpause",height=3,width=2,command=Unpause)
Unpause.pack(side=LEFT,expand=True,fill="x")

Next_Song=Button(text="Next >",height=3,width=2,command=next_song)
Next_Song.pack(side=LEFT,expand=True,fill="x")

Vol_up=Button(text="Vol +",height=3,width=2,command=vol_up)
Vol_up.pack(side=LEFT,expand=True,fill="x")
Vol_down=Button(text="Vol -",height=3,width=2,command=vol_down)
Vol_down.pack(side=LEFT,expand=True,fill="x")


root.mainloop()

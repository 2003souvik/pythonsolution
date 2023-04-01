from tkinter import *
from pygame import mixer
mixer.init()
import os
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
root=Tk()
root.geometry("600x600")


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
current_song=False


#function to play the default_song
def Play_pause():
	global songs_list,default_song,current_song
	if default_song==100:
		if songs_list!=[]:
			b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+songs_list[0]
			mixer.music.load(b)
			mixer.music.play()
			current_song=True
			default_song=0
	elif current_song==True:
		mixer.music.pause()
		current_song=False

	elif current_song==False:
		mixer.music.unpause()
		current_song=True


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


#buttons program
Previous_Song=Button(root,text="< Previous",height=8,width=4,command=previous_song)
Previous_Song.pack(side=LEFT,expand=True,fill="x")
Play_Pause=Button(root,text="Play/Pause",height=8,width=4,command=Play_pause)
Play_Pause.pack(side=LEFT,expand=True,fill="x")
Next_Song=Button(text="Next >",height=8,width=4,command=next_song)
Next_Song.pack(side=LEFT,expand=True,fill="x")

Vol_up=Button(text="Vol +",height=4,width=8,command=vol_up)
Vol_up.pack(side="bottom",)
Vol_down=Button(text="Vol -",height=4,width=8,command=vol_down)
Vol_down.pack(side="bottom")


root.mainloop()

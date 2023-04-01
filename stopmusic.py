import os
import multiprocessing
from playsound import playsound
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
print("choose the music from the list")
print(os.listdir())

#a=input("Enter the music name :")
b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+a+".mp3"

p = multiprocessing.Process(target=playsound, args=("C:\\Users\\kumar\\OneDrive\\Desktop\\music\\kabhi.mp3"))
p.start()
input("press ENTER to stop playback")
p.terminate()
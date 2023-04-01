from pygame import mixer
mixer.init()
import os
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
print("choose the music from the list")
print(os.listdir())
a=input("Enter the music name :")
b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+a+".mp3"
mixer.music.load(b)
mixer.music.play()
while(True):
    print("Press p to pause, press 'r' to resume,Press e to exit the music")
    q = input()
      
    if q == 'p': 
        mixer.music.pause()     
    elif q == 'r':
        mixer.music.unpause()
    elif q == 'e':
        mixer.music.stop()
        break

  

from playsound import playsound
import os
os.chdir("C:\\Users\\kumar\\OneDrive\\Desktop\\music")
print("choose the music from the list")
print(os.listdir())

while(True):
    print("Do you want to continue")
    ch=input("yes/no").lower()
    if ch=="yes":
        a=input("Enter the music name :")
        b="C:\\Users\\kumar\\OneDrive\\Desktop\\music\\"+a+".mp3"
        playsound(b)
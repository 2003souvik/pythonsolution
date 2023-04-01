import os

f=open("C:\\Users\\kumar\\OneDrive\\Desktop\\abc.txt",'a',newline='')
f.write("Hello1")
f.close()
f=open("C:\\Users\\kumar\\OneDrive\\Desktop\\abc.txt",'r')
z=f.readlines()
for i in z:
    print(i+"\n")
f.close()


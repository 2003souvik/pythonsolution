import csv
print("1. to number of students admitted in particular dept \n 2. to maximum marks in particular dept \n 3. search students with name \n 4. search with roll")
n=int(input("Enter the choice"))
if(n==1):
    f=open("std.csv",'r',newline='')
    Reader=csv.reader(f)
    dept=input("Enter the departement")
    c=0
    for i in Reader:
        if(i[5]==dept):
            c=c+1
    print("No of students = ",c)
    f.close()
elif(n==2):
    f=open("std.csv",'r',newline='')
    Reader=csv.reader(f)
    dept=input("Enter the departement")
    max=0
    for i in Reader:
        if(i[5]==dept):
            if(int(i[4])>=max):
                max=int(i[4])
    f.close()

    print("maximum marks = ",max)
elif(n==3):
    f=open("std.csv",'r',newline='')
    Reader=csv.reader(f)
    name=input("Enter the name")
    max=0
    for i in Reader:
        if(i[1]==name):
            print(i)
    f.close()
elif(n==4):
    f=open("std.csv",'r',newline='')
    Reader=csv.reader(f)
    roll=input("Enter the roll")
    max=0
    for i in Reader:
        if(i[0]==roll):
            print(i)
    f.close()







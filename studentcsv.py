import csv
'''f=open("student.csv",'w',newline='')
Writer=csv.writer(f)
field=["Roll number","Name","Address","Phone number","HS marks","Department"]
Writer.writerow(field)
f.close()
'''
print("Enter 1 to insert,2. to update,3.to delete")
n=int(input("Enter the choice"))

if(n==1):
    f=open("student.csv",'a',newline='')
    Writer=csv.writer(f)
    r=input("Enter the roll")
    nam=input("Enter the name")
    p=input("Enter the phone number")
    a=input("Enter the address")
    hs=input("Enter the highersecondary")
    de=input("Enter the departement")
    Writer.writerow([r,nam,p,a,hs,de])
    f.close()
elif(n==2):
    f=open("std.csv",'r+',newline='')
    Reader=csv.reader(f)
    l=[]
    ro=int(input("Enter the roll"))
    for i in Reader:
        if(i[0]==str(ro)):
            depart=input("Enter the departement")
            i[5]=depart
        l.append(i)
    Writer=csv.writer(f)
    Writer.writerows(l)
    f.close()


    



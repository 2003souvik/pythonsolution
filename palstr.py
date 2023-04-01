s=input("enter the string")
l=len(s)
z=""
for i in range(l-1,-1,-1):
    z=z+s[i]
if(z==s):
    print("Palindrome")
else:
    print("Not Palindrome")        
    

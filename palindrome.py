n=int(input("Enter the number"))
a=n
s=0
while n!=0:
    d=n%10
    s=s*10+d
    n=n//10
if(s==a):
    print("Palindrome")
else:
    print("Not Palindrome")    

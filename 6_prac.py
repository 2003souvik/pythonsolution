def hcf(n1,n2):
    if(n2!=0):
        return hcf(n2,n1%n2)
    else:
        return n1
n1=5
n2=4
h=hcf(n1,n2)
print("Hcf = ",h)
print("LCM = ",(n1*n2)/h)


a=input("Enter the sentence 1")
b=input("Enter the sentence 2")
l=[]
for i in a:
    if(i not in b):
        l.append(i)
print(list(set(l)))


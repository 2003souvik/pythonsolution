t1 = tuple(map(int, input().split()))
t2 = tuple(map(int, input().split()))
t3 = tuple(map(int, input().split()))
tup = [t1, t2, t3]
def Sort_Tuple(tuple1):
   tuple1.sort(key = lambda tuple1: tuple1[1])
   return tuple1
print(Sort_Tuple(tup))
tup=(1,2,3,4,5)
length=len(tup)
co=tup.count(1)
print(co)
print(type(tup))
tup2=(6,7,8,9)
print(tup+tup2)
index=tup[-3:-1]
l1=list(tup)
l1.insert(0, 9)
tup=tuple(l1)
print(length)
print(tup)
print(index)
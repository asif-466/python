
a=int(input("enter starting no: "))
b=int(input("enter range lenght: "))

for i in range(a,b+1):
    if (i%2==0):
        print("even",i)
    
for i in range(a,b+1):
    if (i%2!=0):
        print("odd",i)
        


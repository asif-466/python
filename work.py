a = input("enter any str:")
a = a.split(" ")
firstlen = len(a[0])
count=0
s=0
for i in a:
    length = len(i)
    if length > firstlen:
        print("phle str se bade wale str :",i)
    elif length < firstlen:
        count =count + 1
        
    elif length==firstlen:
        s=s + 1
print("phle str se chote wale str ka count:",count)
print("phle wale str ke equal len ka count:",s)



a=input("ENTER ANY STR:")
a=a.split(" ")
count=0
for i in a:
    b=i[0]
    c=i[-1]
    if b==c:
        count=count + 1
print(count)


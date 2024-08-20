a=input("ENTER ANY STR:")
a=a.split(" ")
count=0
for i in a:
    b=i[0]
    c=i[-1]
    if b==c:
        count=count + 1
print(count)

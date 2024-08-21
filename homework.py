a="hello,baby,hhhhhh,rr,e,hello"
a=a.split(",")
firstlen=len(a[0])
count=0
c=0
for  i in a:
        lenght=len(i)
        if lenght>firstlen:
                print("pahla str se bada wala str:",i)
        elif lenght<firstlen:
                count=count + 1
        elif lenght==firstlen:
                print("phla str ke chote wale str ka count:",count)
                print("phle wale str ke equal wale str ka count",c)
         
         
        
        
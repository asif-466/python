#this is a list var
list=["hello","my","lovely","baby"]
#indexing of list
index=list[0]
#second list var
list2=["no","bro"]
#sliceing of list var
list[1:3]=list2
#inserting of list
list.insert(1,"world")
#apending of list
list.append("e")
#removeing of list from element name
list.remove("e")
#removing from index no
list.pop(1)
#deleting from slice
del list[0:3]


print("print index",index)
print("print after insert",list)

#list for loop
l=[88,33,44,55,66]
#sorting of list
l.sort()
#sorting from reverse
s=sorted(l, reverse=True)
print("print after reverce sort",s)
print("print after sort",l)
#for loop for list
for i in l:
    print("print same line with end",i,end=" ")
#while loop for list
w=[1,2,3,4,5]
ind=0
while ind <len(w):
    print(w[ind])
    ind=ind +1

a=[1,2,3,4,5]#list for square loop
suare=[num**2 for num in a]#condition of square loop
print("print after suare",suare)

fruite=["apple","banana","mango"]#list for loop with index no
for index, i in enumerate(fruite):#condition
    print("print with index no",index,i)#print

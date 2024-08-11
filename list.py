list=["hello","my","lovely","baby"]#this is a list 
index=list[0]# indexing of list
list2=["no","bro"]#second list
list[1:3]=list2# sliceing of list
list.insert(1,"world")#inserting of list
list.append("e")#appending of last value
list.remove("e")#removing from elements name
list.pop(1)#removing from index no
del list[0:3]#deleting from slicing


print("print index",index)#print index
print("print after insert",list)#print after inserting list


l=[88,33,44,55,66]#list for loop
l.sort()#sort of list
s=sorted(l, reverse=True)
print("print after reverce sort",s)
print("print after sort",l)
for i in l:#for condition in list
    print("print same line with end",i,end=" ")#print in same line with end 

w=[1,2,3,4,5]#list for while loop
ind=0#index=0
while ind <len(w):#wile loop condition
    print(w[ind])#print while loop result
    ind=ind +1#append in index of while loop

a=[1,2,3,4,5]#list for square loop
suare=[num**2 for num in a]#condition of square loop
print("print after suare",suare)#print of square loop

fruite=["apple","banana","mango"]#list for loop with index no
for index, i in enumerate(fruite):#condition
    print("print with index no",index,i)#print

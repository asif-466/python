# #indexing and slicing of list
# list1=["hello","my","lovely","baby"]
# index=list[0]
# list2=["no","bro"]
# list1[0:2]=list2
# print(list2)
# print(list1)
# l1=["monu","a","a","m","jonu"]
# a=list1[0] +" "+ list1[4]
# b=list1[0] [2]
# print(a)
# print(b)
#inserting of list
# insertlist=["hello","baby","what","are","you","doing"]
# insertlist.insert(1,"world")
# print(insertlist)
#apending of list
# appendlist=["hello","baby","what","are","you","doing"]
# appendlist.append("e")
# print(appendlist)
#removeing of list from element name
# removelist=["hello","baby","what","are","you","doing"]
# removelist.remove("baby")
# print(removelist)
#removing from index no
# poplist=["hello","baby","what","are","you","doing"]
# poplist.pop(1)
# print(poplist)
# #sorting of list
# l=[88,33,44,55,66]
# l.sort()
# print(l)
# #sorting from reverse
# l=[88,33,44,55,66]
# s=sorted(l, reverse=True)
# print(s)
# #for loop for list
l=[88,33,44,55,66]
for i in l:
     print(i,end=" \n")#print same line with end
#while loop for list
w=[1,2,3,4,5]
ind=0
while ind <len(w):
     print(w[ind])
     ind=ind +1
# list for square loop
a=[1,2,3,4,5]
suare=[num**2 for num in a]
print("print after suare",suare)
# list for loop with index no

fruite=["apple","banana","mango"]
for index, i in enumerate(fruite):
     print("print with index no",index,i)

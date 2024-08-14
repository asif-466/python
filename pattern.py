
# num= int(input("enter lenght of pattern:"))

# for i in range(1, num +1):
    
#     for j in range(1, i + 1):
#         print(chr(96 + j), end=' ')
    
#     print()

num= int(input("enter lenght of pattern:"))
print("square pattern")

for i in range(1, num +1):
    
    for j in range(1, num + 1):
        print("*",end=" ")
    
    print()

num= int(input("enter lenght of pattern:"))
print("trangle pattern")

for i in range(1, num +1):
    
    for j in range(1, i + 1):
        print("*",end=" ")
    
    print()

num= int(input("enter lenght of pattern:"))
print("secound trangle pattern")

for i in range(1, num +1):
    
    for j in range(i, num + 1):
        print("*",end=" ")
    
    print()

num= int(input("enter lenght of pattern:"))
print("third trangle pattern")

for i in range(1, num +1):
    
    for j in range(i, num + 1):
        print(" ",end=" ")
    for j in range(1,i+1):
            print("*",end=" ")

    print() 

num=int(input("enter lenght of pattern:"))
print("fourth trangle pattern")

for i in range(1, num +1):
    
    for j in range(1,i + 1):
        print(" ",end=" ")
    for j in range(i,num+1):
            print("*",end=" ")
    print()

num=int(input("enter lenght of pattern:"))
print("hill pattern")

for i in range(1, num +1):
    
    for j in range(i,num + 1):
        print(" ",end=" ")
    for j in range(1,i):
        print("*",end=" ")
    for j in range(1,i+1):
         print("*",end=" ")
                 
    print()

num=int(input("enter lenght of pattern:"))
print("down hill pattern")

for i in range(1, num +1):
    
    for j in range(1,i + 1):
        print(" ",end=" ")
    for j in range(i,num ):
        print("*",end=" ")
    for j in range(i,num+1):
         print("*",end=" ")
                 
    print()

num=int(input("enter lenght of pattern:"))
print("dimand pattern")

for i in range(1, num):
    
    for j in range(i,num + 1):
        print(" ",end=" ")
    for j in range(1,i):
        print("*",end=" ")
    for j in range(1,i+1):
         print("*",end=" ")
                 
    print()

for i in range(1, num ):
    
    for j in range(1,i + 1):
        print(" ",end=" ")
    for j in range(i,num ):
        print("*",end=" ")
    for j in range(i,num+1):
         print("*",end=" ")
                 
    print()

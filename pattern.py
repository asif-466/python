
num= int(input("enter lenght of pattern:"))

for i in range(1, num +1):
    
    for j in range(1, i + 1):
        print(chr(96 + j), end=' ')
    
    print()

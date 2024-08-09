
s = input("enter str:")

chars = set()
unique_chars = ''

for char in s:
    if char not in chars:
        chars.add(char)  
        unique_chars =  unique_chars + char 
     

print(f"String with unique characters: '{unique_chars}'")


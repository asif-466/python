
s = input("enter str:")

set_var = set()
unique_chars = ''

for char in s:
    if char not in set_var:
        set_var.add(char)  
        unique_chars =  unique_chars + char

print(f"String with unique character: '{unique_chars}'")
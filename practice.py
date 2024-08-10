s= input("enter str:")
covert_list=list(s)
set_var = set()
set_var2 = set()
unique_chars = ''
unique_words = []

for char in s:
     if char not in set_var:
         set_var.add(char)  
         unique_chars =  unique_chars + char
         print("hello my love")

     print(f"String with unique character: '{unique_chars}'")
     unique_words = []
     seen = set()

for word in covert_list:
     if word not in set_var2:
         set_var2.add(word)
         unique_words.append(word)

         print("unique_word: ",unique_words)  






Mutability: Lists, sets, और dictionaries mutable हैं, जबकि strings और tuples immutable हैं।
Order: Lists, strings, और tuples ordered होते हैं, जबकि sets और dictionaries unordered होते हैं।
Duplicates: Sets और dictionaries में duplicates नहीं होते, लेकिन lists, strings, और tuples में होते हैं।
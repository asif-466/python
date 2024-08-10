user=input("enter any strings:")
key=input("search key:")
index=user.find(key)
count=user.count(key)
before=user[:index]
lenght=len(key)
after=user[index + lenght:]
print(f"index of {key}:",index)
print(f"count of {key}:",count)
print(f"index of before {key}:",before)
print(f"index of after  {key}:",after)

import os
import path

username = os.getenv("USERNAME")
path = os.getenv("PATH")
temp = os.getenv("TEMP")

print(username)
print(path)
print(temp)
print(os.getenv("MY_SECRET"))
print(os.getenv("CAR_COLOR"))
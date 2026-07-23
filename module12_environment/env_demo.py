import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("USERNAME")
path = os.getenv("PATH")
temp = os.getenv("TEMP")

print(username)
# print(path)
# print(temp)
# print(os.getenv("MY_SECRET"))
# print(os.getenv("CAR_COLOR"))

print(os.getenv("API_KEY"))
print(os.getenv("SECRET_KEY"))
print(os.getenv("DATABASE_URL"))
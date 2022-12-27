# import time
# timestamp = time.strftime('%I:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%I')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime

import datetime

def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    print(hour)
    name = input("Enter your name : ")
    if hour < 12:
        print(f"Good Morning!, {name}")
    elif hour < 17:
        print(f"Good Afternoon!, {name}")
    else:
        print(f"Good Evening!, {name}")

greet()

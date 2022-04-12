import random
from datetime import datetime


def get_random_date(start_date, end_date):
    return start_date + random.random() * (end_date - start_date)


start_date = datetime.strptime(input("Please Enter start time: "), "%Y-%m-%d")

end_date = datetime.strptime(input("Please Enter end time: "), "%Y-%m-%d")

print(start_date, end_date)
date = get_random_date(start_date, end_date)
print(date)

if date.weekday() == 0:
    print("I have no vinaigrette!")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = int(str(number)[-1:])
if lastnumber > 5:
    value = "and is greater than 5"
elif lastnumber == 0:
    value = "and is 0"
elif lastnumber < 6 and lastnumber != 0:
    value = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, lastnumber, value))

# main.py
from mylib import myfunc

num = int(input("How many turns you want to run [ ]: "))
for i in range(1, num + 1):
        print(myfunc("M", i))



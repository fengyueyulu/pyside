from io import  open
import time

with open("data", mode="r") as fp:
    alldata = fp.readlines()
    for i in range(len(alldata)):
        alldata[i]=alldata[i].strip()
    print(alldata[::-1])
#!/usr/bin/python3
newend = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=newend)
    else:
        if i == 99:
            newend = "\n"
        print(i, end=newend)

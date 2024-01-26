#!/usr/bin/python3
newend = ", "
for i in range(0, 100):
    ldigit = i % 10
    fdigit = i / 10
    if i < 10 and fdigit < ldigit:
        print("{}{}".format(0, i), end=newend)
    elif fdigit < ldigit:
        if i == 89:
            newend = "\n"
        print(i, end=newend)
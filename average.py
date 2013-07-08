#!/usr/bin/env python3

numbers=[]
lowest=None
highest=None
sum=0
count=0

while True:
    line = input("enter a number or Enter to finish: ")
    if line:
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        if lowest is None or number < lowest:
            lowest=number
        if highest is None or  number > highest:
            highest=number
        sum += number
        count += 1
        numbers.append(number)
    else:
        break
print("numbers: ",numbers)
print("count =", count, "sum =", sum,"lowest= ",
      lowest,"highest= ",highest, "mean =", sum / count)
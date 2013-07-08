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
for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j]>numbers[j+1]:
            x=numbers[j+1]
            numbers[j+1]=numbers[j]
            numbers[j]=x
median=len(numbers)//2
if median==len(numbers)/2:
    median=(numbers[median]+numbers[median-1]) / 2
else:
    median=numbers[median];
print("numbers: ",numbers)
print("count =", count, "sum =", sum,"lowest= ",
      lowest,"highest= ",highest,"median= ",median,"mean =", sum / count)
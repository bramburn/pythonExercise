count = 0
toAverage = []

while (count < 6):
    number = int(input("Enter a number: "))
    if (number <= 20 and number > 0):
        toAverage.append(number)
        count = count + 1
    else:
        print("Error!")

total = 0
for x in toAverage:
    total = total + int(x)

average = total / 6

print(F"Average is {average}")

# Make, using the while, a program that prints the numbers of a given interval [start, end]. The start and end values must be entered.

start = int(input("Enter the starting interval value: "))
end = int(input("Enter the ending interval value: "))

if (start > end):
    print("End value needs to be higher than start value")
    exit()

for x in range(start, end + 1):
    print(x)

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

month1 = [4, 6, 9, 11]
month2 = [1, 3, 5, 7, 8, 10, 12]

for months in month1:
    if(day > 30):
        day = 0

for months in month2:
    if(day > 31):
        day = 0

if(month == 2 and year%4 == 0 and year%100 == 0 and day > 29):
    day = 0
elif(month == 2 and day > 28):
    day = 0

day += 1
month += 1
year += 1

print(f"{day}/{month}/{year}")

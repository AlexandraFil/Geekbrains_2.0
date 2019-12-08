start = int(input("Enter your first result: "))
end = int(input("Enter your goal: "))

day_number = 1
result = start

while end > result:
    day_number += 1
    result *= 1.1

print(day_number)

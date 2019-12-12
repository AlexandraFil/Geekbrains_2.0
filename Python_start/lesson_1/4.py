number = input("Enter your number: ")
i = 0
max = int(number[i])

while i < len(number)-1:
    if max <= int(number[i+1]):
        max = int(number[i+1])
    i += 1

print(max)


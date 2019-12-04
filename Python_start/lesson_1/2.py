time = int(input("Enter time in seconds: "))

hh = time // 3600
mm = (time - hh * 3600) // 60
ss = time % 60

if hh > 99:
    print("Mistake! Your number is too big!")
if hh < 10:
    hh = "0" + str(hh)
if mm < 10:
    mm = '0' + str(mm)
if ss < 10:
    ss = '0' + str(ss)

print(f"{hh}:{mm}:{ss}")


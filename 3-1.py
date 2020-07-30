num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
aOptions = []
for i in range(0, len(num)):
    if num[i] % 4 == 0:
        aOptions.append(num[i])
for i in range(0, len(aOptions)):
    a = 3+aOptions[i]//4
    c = a-aOptions[i]
    if c<0:
        continue
    d = 2*a - aOptions[i]
    print(f"{a}{aOptions[i]}{c}{d}")

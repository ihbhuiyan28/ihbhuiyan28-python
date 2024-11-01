# break and continue
index = 0
while index <= 10:
    index = index + 1
    if index == 3:
        continue
    if index == 6:
        break
    print(index)

for index in range(1, 11):
    if index == 3:
        continue
    if index == 6:
        break
    print(index)
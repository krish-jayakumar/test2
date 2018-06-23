result = list()
xyz = [x for x in range(11, 21)]
number = [2520]
count = 0
while len(result) == 0:
    for n in number:
        print n
        for x in xyz:
            if n % x == 0:
                count += 1
            elif n % x != 0:
                count = 0
                break
    if count == 10:
        result.append(number[0])
    elif count != 10:
        number[0] += 1

print result 
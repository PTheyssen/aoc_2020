
# Day 2 of advent of code 2020
f = open('input.txt', 'r')
data = f.read()
f.close()
data = data.split('\n')[:-1]


def contains(c, s, n):
    counter = 0
    for x in s:
        if c == x:
            counter += 1
    if counter == n:
        return True
    else:
        return False

# solving part 1    
valid = 0
for l in data:
    x = l.split()
    s = x[2]
    c = x[1].strip(':')
    start, end = x[0].split('-')
    for i in range(int(start), int(end)+1):
        if contains(c, s, i):
            valid += 1

print(f"Part1: Number of valid passwords: {valid}")


# solving part 2
valid = 0
for l in data:
    x = l.split()
    s = x[2]
    c = x[1].strip(':')
    start, end = x[0].split('-')
    start = int(start)
    end = int(end)
    if (s[start-1] == c) and (not s[end-1] == c):
        valid += 1
    elif (not s[start-1] == c) and (s[end-1] ==c):
        valid +=1

print(f"Part2: Number of valid passwords: {valid}")

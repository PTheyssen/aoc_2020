# aoc 2020 day 5
import itertools as it

f = open('input')
data = f.read().split('\n')


def bs(m, l, u):
    lo = l
    up = u
    for x in m:
        diff = up - lo
        if x == 'F' or x == 'L':
            up -= (diff // 2) + 1
        if x == 'B' or x == 'R':
            lo += (diff // 2) + 1
        # print(f"lo: {lo}")
        # print(f"up: {up}")
        # print("---------")
    if m[-1] == 'F':
        return up
    else:
        return lo

# solve part 1
ids = []
for d in data:
    row = d[:-3]
    col = d[-3:]
    seat_id = bs(row, 0, 127) * 8 + bs(col, 0, 7)
    ids.append(seat_id)

print(f"Maximum seat id: {max(ids)}")

# solve part 2

# generate all possible ID of seats
# find ID that is not in my list but +1 and -1 ids in my list
all_ids = it.product(range(128), range(8))

for i in all_ids:
    seat = i[0] * 8 + i[1]
    if seat not in ids and (seat+1 in ids and seat-1 in ids):
        print(f"Found my seat ID: {seat}")

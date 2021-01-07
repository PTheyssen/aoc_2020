import itertools as it

# Day 1 of advent of code 2020
f = open('input', 'r')
data = f.read()
f.close()
data = data.split()
data = [int(x) for x in data]


# solve part 1
pairs = it.product(data, data)
for p in pairs:
    if p[0] + p[1] == 2020:
        print(f"Solution for first part: {p[0] * p[1]}")


# solve part 2
triples = it.product(data, data, data)
for t in triples:
    if t[0] + t[1] + t[2] == 2020:
        print(f"Solution for second part: {t[0] * t[1] * t[2]}")

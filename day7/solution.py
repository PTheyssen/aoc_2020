

f = open('input')
data = f.read().split('\n')


# how many bag colors can contain a shiny gold bag
# transitive relation

old_len = 0
bags =  ['shiny gold']
while old_len != len(bags):
    old_len = len(bags)
    for d in data:
        x = d.split(' bags contain')
        for b in bags:
            if b in x[1]:
                bags.append(x[0])
                bags = list(set(bags))

print(f'Solution part 1: number of bags {len(bags) - 1}')


result = 1
s = 0
for i in range(6):
    result *= 2
    s += result
print(s)

# start at shiny bag
# go through every bag thats inside and call the
# function for it to go deeper

clean = []
for d in data:
    x = d.split(' bags contain ')
    x[1] = x[1].split(',')
    x[1] = [i.strip() for i in x[1]]
    x[1][-1] = x[1][-1].strip('.')
    clean.append(x)

for c in clean:
    print(c)

start = ''
for c in clean:
    if c[0] == 'shiny gold':
        start = c[1]

print(start)

# this could be done with simple map (way better in functional way)
def get_names(bags):
    n = []
    for b in bags:
        if b != 'no other bags':
            name = b.split()[1:-1]
            name = name[0] + " " + name[1]
            n.append(name)
    return n

bags = start
result = 20
def solve(bags, result):
    for c in clean:
        for n in get_names(bags):
            if n == c[0]:
                for num in c[1]:
                    if num != 'no other bags':
                        # print(f"num: {num}")
                        print(f'result: {result}')
                        print(num[0])
                        print(c[1])
                        solve(c[1], result + int(num[0]))
    return result

print(f'solve part 2: {solve(start, 20)}')
        

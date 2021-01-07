
f = open('input')

data = f.read().split('\n\n')

# solve part 1
s = 0
for d in data:
    distinct = set()
    for c in d:
        if c != '\n':
            distinct.add(c)
    s += len(distinct)


print(f'Part 1 solution: {s}')

# solve part 2
def is_in(x, persons):
    for p in persons:
        if x not in p:
            return False
    return True


s = 0
for group in data:
    persons = group.split('\n')
    distinct = set()
    for x in group:
        if x != '\n' and is_in(x, persons):
            distinct.add(x)
    print(f'group: {group}')    
    print(f'persons: {persons}')
    print(distinct)
    s += len(distinct)
        

print(f'Part 2 solution: {s}')

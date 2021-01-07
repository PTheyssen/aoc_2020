f = open('input')
rows = f.read().split('\n')

# solve part 1
row_len = len(rows[0])
n = len(rows) - 1

def check_trees(d, r):
    down = 0
    right = 0
    trees = 0
    while down < n:
        down += d
        right += r
        right %= row_len
        if rows[down][right] == '#':
            trees += 1
    return trees

res = check_trees(1, 3)

print(f'I encounter {res} many trees')

# solve part 2
s_1 = check_trees(1, 1)
s_2 = check_trees(1, 3)
s_3 = check_trees(1, 5)
s_4 = check_trees(1, 7)
s_5 = check_trees(2, 1)

res = s_1 * s_2 * s_3 * s_4 * s_5
print(f'Product of encountered trees is {res}')

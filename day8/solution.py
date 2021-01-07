

f = open('input')

code = f.read().split('\n')

code = [[d.split(),False] for d in code]


acc = 0
pc = 0 # program counter

# run the code
while True:
    d = code[pc]
    # instruction is run a second time
    if d[1] == True:
        print(f"Program would enter infinite loop")
        print(f"acc: {acc}")
        break
    else:
        d[1] = True

    inst = d[0][0]
    if inst == 'nop':
        pass
    elif inst == 'acc':
        acc += int(d[0][1])
    elif inst == 'jmp':
        pc += int(d[0][1])
        continue
    
    pc += 1
    

floor = 0
rf = open('advent1.txt', 'r')
line = rf.readline()
pos = 0
part1 = True

for i in line:
    pos = pos + 1
    
    if i == '(':
        floor = floor + 1
    else:
        floor = floor - 1
    if (part1 == False):
        if floor == -1:
            print pos
            break

print floor

rf = open('advent3.txt', 'r')
directions = rf.readline()
rf.close()

coords = []
x = 0
y = 0
pair = [x,y]
coords.append(str(pair))

part1 = False

if part1 == True:
    for i in directions:
            if i == '^':
                y = y + 1
            if i == 'v':
                y = y - 1
            if i == '<':
                x = x - 1
            if i == '>':
                x = x + 1
                
            pair = [x,y]
            coords.append(str(pair))
        
    uniqueVals = set(coords)
    print len(uniqueVals)

else:
    x2 = 0
    y2 = 0
    for i in range(0,len(directions) - 1,2):
            if directions[i] == '^':
                y = y + 1
            if directions[i] == 'v':
                y = y - 1
            if directions[i] == '<':
                x = x - 1
            if directions[i] == '>':
                x = x + 1
                
            pair = [x,y]
            coords.append(str(pair))

            if directions[i+1] == '^':
                y2 = y2 + 1
            if directions[i+1] == 'v':
                y2 = y2 - 1
            if directions[i+1] == '<':
                x2 = x2 - 1
            if directions[i+1] == '>':
                x2 = x2 + 1
                
            pair = [x2,y2]
            coords.append(str(pair))
        
    uniqueVals = set(coords)
    print len(uniqueVals)

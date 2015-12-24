def calc(l, w, h):
    lw = l*w
    lh = l*h
    wh = w*h
    if lw <= lh and lw <= wh:
        least = lw
    elif lh <= lw and lh <= wh:
        least = lh
    elif wh <= lh and wh <= lw:
        least = wh
        
    surface = 2*l*w + 2*w*h + 2*h*l + least
    return surface

def rLength(l, w, h):
    maxL = 0
    if l >= h and l >= w:
        maxL = l
    elif h >= w and h >= l:
        maxL = h
    elif w >= l and w >= h:
        maxL = w
    length = l*w*h + 2*l + 2*w + 2*h - 2*maxL
    return length

part1 = False
if (part1 == True):		
    total = 0
    rf = open('advent2.txt', 'r')
    i = len(rf.readlines())
    rf.seek(0)

    for i in range(0, i):
        line = rf.readline().strip('\n').split('x')
        total = total + calc(int(line[0]),int(line[1]),int(line[2]))
    rf.close()

    print total
else:
    total = 0
    rf = open('advent2.txt', 'r')
    i = len(rf.readlines())
    rf.seek(0)

    for i in range(0, i):
        line = rf.readline().strip('\n').split('x')
        total = total + rLength(int(line[0]),int(line[1]),int(line[2]))
    rf.close()

    print total

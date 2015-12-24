from copy import deepcopy

def newConfigPls(oldConfig):
    newConfig = []
    newConfig = deepcopy(oldConfig)
    
    for i in range(1,len(oldConfig)-1):
        for j in range(1,len(oldConfig[0])-1):
            on = howMany(oldConfig[i-1][j-1],oldConfig[i-1][j],oldConfig[i-1][j+1],
                         oldConfig[i][j-1],oldConfig[i][j+1],
                         oldConfig[i+1][j-1],oldConfig[i+1][j],oldConfig[i+1][j+1])
            if (oldConfig[i][j] == '.'):
                if (on == 3):
                    newConfig[i][j] = '#'
            else:
                if (on != 2 and on != 3):
                    newConfig[i][j] = '.'
    return newConfig
            
def howMany(one, two, three, four, five, six, seven, eight):
    lights = [one, two, three, four, five, six, seven, eight]
    on = 0
    for i in range(0,len(lights)):
        if lights[i] == '#':
            on = on + 1
    return on

rf = open('advent18.txt','r')
rows = len(rf.readlines())
rf.seek(0)

###create buffer###
firstLast = []
for i in range(0,102):
    firstLast.append('a')

oldConfig = []
oldConfig.append(firstLast)

###create oldConfig###
for i in range(0,rows):
    line = list('a' + rf.readline().replace('\n','') + 'a')
    oldConfig.append(line)

oldConfig.append(firstLast)

###create newConfig###
for i in range(0,100):
    oldConfig[1][1] = '#'
    oldConfig[100][100] = '#'
    oldConfig[1][100] = '#'
    oldConfig[100][1] = '#'
    
    oldConfig = newConfigPls(oldConfig)

oldConfig[1][1] = '#'
oldConfig[100][100] = '#'
oldConfig[1][100] = '#'
oldConfig[100][1] = '#'

###count Lights on###
on = 0   
for i in range(0, len(oldConfig)):
    for j in range(0,len(oldConfig[0])):
        if(oldConfig[i][j] == '#'):
            on = on + 1
print on

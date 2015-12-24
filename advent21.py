import itertools
  
def letsCheck(weapon, armor, ring1, ring2):
    bossHP = 104
    bossDMG = 8
    bossDEF = 1
    myHP = 100
    myDMG = weapon[2] + ring1[2] + ring2[2]
    myDEF = armor[3] + ring1[3] + ring2[3]

    alive = True
    iFight = True
    win = False
    price = 0
    while alive:
        if iFight:
            bossHP = bossHP - max((myDMG - bossDEF),1)
            iFight = False
            if bossHP <= 0:
                alive = False
                win = True
        else:
            myHP = myHP - max((bossDMG - myDEF),1)
            iFight = True
            if myHP <= 0:
                alive = False
                win = False
    price = weapon[1] + armor[1] + ring1[1] + ring2[1]
    thisSet = [weapon[0],armor[0],ring1[0],ring2[0]]
    return win,price,thisSet

def findMin(myList):
    mini = myList[0][1]
    for i in range(0,len(myList)):
        if myList[i][1] < mini:
            mini = myList[i][1]
            index = i
    return mini, index

def findMax(myList):
    maxi = myList[0][1]
    for i in range(0,len(myList)):
        if myList[i][1] > maxi:
            maxi = myList[i][1]
            index = i
    return maxi, index
    
weapons = [["Dagger",8,4,0],
           ["Shortsword",10,5,0],
           ["Warhammer",25,6,0],
           ["Longsword",40,7,0],
           ["Greataxe",74,8,0]]

armor = [["none",0,0,0],
         ["Leather",13,0,1],
         ["Chainmail",31,0,2,],
         ["Splintmail",53,0,3],
         ["Bandedmail",75,0,4],
         ["Platemail",102,0,5]]

rings = [["none",0,0,0],
         ["Damage1",25,1,0],
         ["Damage2",50,2,0],
         ["Damage3",100,3,0],
         ["Defense1",20,0,1],
         ["Defense2",40,0,2],
         ["Defense3",80,0,3]]

sets = []

indices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,11,12,13,14,15,16,17]
for subset in itertools.combinations(indices, 4):
    if ((subset[0] >= 0 and subset[0] < 5) and (subset[1] >= 5 and subset[1] < 11)):
        if (subset[2] == 11 and subset[3] == 11):
            sets.append(subset)
        elif (subset[2] != subset[3] and subset[2] >= 11 and subset[3] >= 11):
            sets.append(subset)

possCom = list(set(sets))

iWin = []
iLose = []
for i in range(0,len(possCom)):
    this = []
    win,price,this = letsCheck(weapons[possCom[i][0]], armor[possCom[i][1] - 5],
                    rings[possCom[i][2] - 12], rings[possCom[i][3] - 12])
    aList = [win,price,this]
    if win == True:
        iWin.append(aList)
    else:
        iLose.append(aList)

minPrice,winI = findMin(iWin)
maxPrice,loseI = findMax(iLose)

print "Cheapest set and I still win: $" + str(minPrice)
print iWin[winI][2]
print "Most expensive set and I still lose: $" + str(maxPrice)
print iLose[loseI][2]

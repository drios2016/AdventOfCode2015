#name,cost,damage,heal,recharge,def]
moves = [["MagicMissile",53,4,0,0,0],
         ["Drain",73,2,2,2,0],
         ["Shield",113,0,0,0,7],
         ["Poison",173,3,0,0,0],
         ["Recharge",229,0,0,101,0]]

#bossHP,bossDMG,myHP,myDEF,myMana,manaUsed
stats = [51,9,50,0,500,0]
notDead = True
shield = False
sCtr = 6
poison = False
pCtr = 6
recharge = False
rCtr = 5
myTurn = True
totalAdded = 0

movesUsed = []
hardmode = True

while (notDead == True):
    if (myTurn == True):
        print "\n---------------------------------------------------"
        print "Boss Stats: "
        print "\tHP: " + str(stats[0])
        
        print "Your Stats: "
        print "\tHP: " + str(stats[2])
        print "\tMana: " + str(stats[4])
        print "\tShield is " + str(shield) + ", Poison is " + str(poison) + ", Recharge is " + str(recharge)
        print "---------------------------------------------------\n"
        
        print "It's your turn!"

        if (hardmode == True):
            print "You lose 1 HP..."
            stats[2] = stats[2] - 1
            if (stats[2] <= 0):
                notDead = False
                print "You died! MyHP = ", stats[2]
                print "BossHP = ", stats[0]
                break
       
        if (shield == True):
            sCtr = sCtr - 1
            stats[3] = 7
            print "\tYour shield is active! MyDEF = 7"
            if (sCtr == 0):
                shield = False
                sCtr = 6
                stats[3] = 0
        if (poison == True):
            pCtr = pCtr - 1
            stats[0] = stats[0] - 3
            print "\tYou poisoned him! BossHP -3"
            if (pCtr == 0):
                poison = False
                pCtr = 6
        if (recharge == True):
            rCtr = rCtr - 1
            stats[4] = stats[4] + 101
            print "\tYou recharged mana! Mana +101"
            if (rCtr == 0):
                recharge = False
                rCtr = 5
        if (stats[0] <= 0):
            print "\nYou won! BossHP = ", stats[0]
            break
        if (stats[4] < 53):
            print "You ran out of mana!"
            break
        
        print "\nAvailable moves: "
        if (stats[4] >= moves[0][1]):
            print "\t0: " + moves[0][0]
        else:
            print "\t0: " + moves[0][0] + " (Not enough mana...)"
        if (stats[4] >= moves[1][1]):
            print "\t1: " + moves[1][0]
        else:
            print "\t1: " + moves[1][0] + " (Not enough mana...)"
        if (shield == False):
            if (stats[4] >= moves[2][1]):
                print "\t2: " + moves[2][0]
            else:
                print "\t2: " + moves[2][0] + " (Not enough mana...)"
        else:
            print "\t2: " + moves[2][0] + " (Available in ",sCtr," turns...)"
        if (poison == False):
            if (stats[4] >= moves[3][1]):
                print "\t3: " + moves[3][0]
            else:
                print "\t3: " + moves[3][0] + " (Not enough mana...)"
        else:
            print "\t3: " + moves[3][0] + " (Available in ",pCtr," turns...)"
        if (recharge == False):
            if (stats[4] >= moves[4][1]):
                print "\t4: " + moves[4][0]
            else:
                print "\t4: " + moves[4][0] + " (Not enough mana...)"
        else:
            print "\t4: " + moves[4][0] + " (Available in ",rCtr," turns...)"

        index = int(input("\nWhat's your move?: "))
        movesUsed.append(index)
        
        if (index == 0):
            print "\tYou used " + moves[0][0] + "! BossHP -4"
            stats[4] = stats[4] - moves[0][1]
            stats[5] = stats[5] + moves[0][1]
            stats[0] = stats[0] - moves[0][2]
        if (index == 1):
            print "\tYou used " + moves[1][0] +"! BossHP -2, YourHp +2"
            stats[4] = stats[4] - moves[1][1]
            stats[5] = stats[5] + moves[1][1]
            stats[0] = stats[0] - moves[1][2]
            stats[2] = stats[2] + moves[1][3]
        if (index == 2):
            print "\tYou used " + moves[2][0] +"!"
            shield = True
            stats[4] = stats[4] - moves[2][1]
            stats[5] = stats[5] + moves[2][1]
        if (index == 3):
            print "\tYou used " + moves[3][0] +"!"
            poison = True
            stats[4] = stats[4] - moves[3][1]
            stats[5] = stats[5] + moves[3][1]
        if (index == 4):
            print "\tYou used " + moves[4][0] +"!"
            recharge = True
            stats[4] = stats[4] - moves[4][1]
            stats[5] = stats[5] + moves[4][1]
        myTurn = False
    else:
        print "\n\nBoss is attacking!"    
        if (shield == True):
            sCtr = sCtr - 1
            stats[3] = 7
            print "\tYour shield is active! DEF = 7"
            if (sCtr == 0):
                shield = False
                sCtr == 6
        if (poison == True):
            pCtr = pCtr - 1
            stats[0] = stats[0] - 3
            print "\tYou poisoned him! BossHP -3"
            if (pCtr == 0):
                poison = False
                pCtr = 6
        if (recharge == True):
            rCtr = rCtr - 1
            stats[4] = stats[4] + 101
            print "\tYou recharged mana! Mana +101"
            if (rCtr == 0):
                recharge = False
                rCtr = 5
        if (stats[0] <= 0):
            print "You won! BossHP = ", stats[0]
            break
        
        stats[2] = stats[2] - (max(stats[1]-stats[3],1))
        print "Boss hit you! YourHP -" + str(stats[1] - stats[3])
        if (stats[2] <= 0):
            notDead = False
            print "\nYou died! MyHP = ", stats[2]
            print "BossHP = ", stats[0]
        if (shield == False):
            stats[3] = 0
        myTurn = True
      
print "\nMana Left: ",stats[4]
print "Mana Used: ",stats[5]
print "You used the moves: "
for i in range(0,len(movesUsed)):
    print "\t" + str(movesUsed[i]) + ": " + moves[movesUsed[i]][0]
    
#4,2,3,0,0,2,4,3,0,0,   1242
#4,3,0,0,0,0,           lost
#4,2,3,0,0,2,0,0,0,0,0, lost
#4,2,3,0,0,4,0,3,0,0,   1182, 328
#3,4,2,3,0,0,0,0,       900,105,1,-1 Correct pt1  
#3,4,2,3,4,2,3,0
#3,4,2,3,4,0,3,0
#3,4,2,3,0,0,3
#3,4,2,3,0,0,0,
#3,4,2,3,1,0,0,
#2,4,3,2,4,3,0,3,0,0
#3,4,2,3,4,2,3,0,0,
#3,4,2,3,0,2,0,0,
#3,4,2,3,4,2,3,0       1256
#3,4,2,3,4,2,0,0,0,0   1242
#3,4,2,3,0,2,0,0,
#3,4,2,3,0,1,0,0,
#3,4,2,3,1,0,3,0,

#Henry
#4,2,3,0,2,3,0,0,       lost, 960,45,3,26
#4,2,3,4,2,3,4,2,3,0,2,3lost, 1369,141,-2,
#2,4,3,2,4,3,2,4,3,2,0,3,0,

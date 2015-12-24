#children: 3
#cats: 7
#samoyeds: 2
#pomeranians: 3
#akitas: 0
#vizslas: 0
#goldfish: 5
#trees: 3
#cars: 2
#perfumes: 1

def letsCheck(category, num):
    if category == "children":
        if int(num) == 3:
            return True
    elif category == "cats":
        if int(num) > 7:
            return True
    elif category == "samoyeds":
        if int(num) == 2:
            return True
    elif category == "pomeranians":
        if int(num) < 3:
            return True
    elif category == "akitas":
        if int(num) == 0:
            return True
    elif category == "vizslas":
        if int(num) == 0:
            return True
    elif category == "goldfish":
        if int(num) < 5:
            return True
    elif category == "trees":
        if int(num) > 3:
            return True
    elif category == "cars":
        if int(num) == 2:
            return True
    elif category == "perfumes":
        if int(num) == 1:
            return True
    else:
        return False

rf = open('advent16.txt','r')
num = len(rf.readlines())
rf.seek(0)

fact1 = False
fact2 = False
fact3 = False

for i in range(0,num):
    line = rf.readline().replace(':', '').replace(',','').split()     
    fact1 = letsCheck(line[2],line[3])
    fact2 = letsCheck(line[4],line[5])
    fact3 = letsCheck(line[6],line[7])
    if (fact1 == True and fact2 == True and fact3 == True):
        print line[1]

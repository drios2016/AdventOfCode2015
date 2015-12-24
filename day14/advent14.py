#Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
#Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
#Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
#Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
#Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
#Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
#Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
#Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
#Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.

vix = 0
vixrest = False
vixcounter = 0

rud = 0
rudrest = False
rudcounter = 0

don = 0
donrest = False
doncounter = 0

blitz = 0
blitzrest = False
blitzcounter = 0

com = 0
comrest = False
comcounter = 0

cup = 0
cuprest = False
cupcounter = 0

dash = 0
dashrest = False
dashcounter = 0

danc = 0
dancrest = False
danccounter = 0

pranc = 0
prancrest = False
pranccounter = 0

dist = []
dist.append(vix)
dist.append(rud)
dist.append(don)
dist.append(blitz)
dist.append(com)
dist.append(cup)
dist.append(dash)
dist.append(danc)
dist.append(pranc)

points = []
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)
points.append(vix)

for i in range(0,2503):
    if (vixrest == False):
        dist[0] = dist[0] + 19
        vixcounter = vixcounter + 1
        if (vixcounter == 7):
            vixrest = True
            vixcounter = 0
    else:
        vixcounter = vixcounter + 1
        if (vixcounter == 124):
            vixrest = False
            vixcounter = 0
    #print vix       
    if (rudrest == False):
        dist[1] = dist[1] + 3
        rudcounter = rudcounter + 1
        if (rudcounter == 15):
            rudrest = True
            rudcounter = 0
    else:
        rudcounter = rudcounter + 1
        if (rudcounter == 28):
            rudrest = False
            rudcounter = 0
    #print rud
    if (donrest == False):
        dist[2] = dist[2] + 19
        doncounter = doncounter + 1
        if (doncounter == 9):
            donrest = True
            doncounter = 0
    else:
        doncounter = doncounter + 1
        if (doncounter == 164):
            donrest = False
            doncounter = 0
    #print don
    if (blitzrest == False):
        dist[3] = dist[3] + 19
        blitzcounter = blitzcounter + 1
        if (blitzcounter == 9):
            blitzrest = True
            blitzcounter = 0
    else:
        blitzcounter = blitzcounter + 1
        if (blitzcounter == 158):
            blitzrest = False
            blitzcounter = 0
    #print blitz
    if (comrest == False):
        dist[4] = dist[4] + 13
        comcounter = comcounter + 1
        if (comcounter == 7):
            comrest = True
            comcounter = 0
    else:
        comcounter = comcounter + 1
        if (comcounter == 82):
            comrest = False
            comcounter = 0
    #print com
    if (cuprest == False):
        dist[5] = dist[5] + 25
        cupcounter = cupcounter + 1
        if (cupcounter == 6):
            cuprest = True
            cupcounter = 0
    else:
        cupcounter = cupcounter + 1
        if (cupcounter == 145):
            cuprest = False
            cupcounter = 0
    #print cup
    if (dashrest == False):
        dist[6] = dist[6] + 14
        dashcounter = dashcounter + 1
        if (dashcounter == 3):
            dashrest = True
            dashcounter = 0
    else:
        dashcounter = dashcounter + 1
        if (dashcounter == 38):
            dashrest = False
            dashcounter = 0
    #print dash
    if (dancrest == False):
        dist[7] = dist[7] + 3
        danccounter = danccounter + 1
        if (danccounter == 16):
            dancrest = True
            danccounter = 0
    else:
        danccounter = danccounter + 1
        if (danccounter == 37):
            dancrest = False
            danccounter = 0
    #print danc
    if (prancrest == False):
        dist[8] = dist[8] + 25
        pranccounter = pranccounter + 1
        if (pranccounter == 6):
            prancrest = True
            pranccounter = 0
    else:
        pranccounter = pranccounter + 1
        if (pranccounter == 143):
            prancrest = False
            pranccounter = 0
    #print pranc
    maxi = 0
    index = 0
    for j in range(0,9):
        if (dist[j] > maxi):
            maxi = dist[j]
            index = j
    for k in range(0,9):
        if (dist[k] == maxi):
            points[k] = points[k] + 1

maxi = 0
for i in range(0,9):
    if (points[i] > maxi):
        maxi = points[i]

print maxi

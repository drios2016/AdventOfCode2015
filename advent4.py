import hashlib
key = "ckczppom"
i = 0
part1 = False

if part1 == True:
    while True:
        hash1 = hashlib.md5(key + str(i)).hexdigest()
        if (hash1[0] == '0' and hash1[1] == '0' and hash1[2] == '0'
            and hash1[3] == '0' and hash1[4] == '0'):
            print i
            break
        else:
            i = i + 1
else:
    while True:
        hash1 = hashlib.md5(key + str(i)).hexdigest()
        if (hash1[0] == '0' and hash1[1] == '0' and hash1[2] == '0'
            and hash1[3] == '0' and hash1[4] == '0' and hash1[5] == '0'):
            print i
            break
        else:
            i = i + 1

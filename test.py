import math

def findMissingRIndex(a1,r1,a2,r2):

    missingRIndex = (math.sin(math.radians(a2)) * r2) / math.sin(math.radians(a1))
    print(missingRIndex)

findMissingRIndex(45,False,30,1)

#a1 = 30 r1 = 1 a2 = 45 r2 = N/A
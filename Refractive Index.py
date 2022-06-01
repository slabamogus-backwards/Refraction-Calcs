import math

print("This program is intended to find the critical angle for a set of materials.")
print("-------------------------------------------------------------------------------------------------------------------------\n")

def getAngle():
    unknown = input("Is this angle unknown Y/N? ")
    if unknown == "Y":
        return False
    else:
        try:
            angleInput = float(input("What is the angle? "))
            print("")
            if angleInput < 0 or angleInput > 90:
                print("The angle can't be less than 0 or greater than 90.\n")
                getAngle()
            else:
                return angleInput
        except:
            print("Enter a number.\n")
            getAngle()

    

def refractiveIndex():
    unknown = input("Is this refractive index number unknown Y/N? ")
    if unknown == "Y":
        return False
    else:
        try:
            rIndex = float(input("What is the refractive index? "))
            print("")
            if rIndex < 1:
                refractiveIndex()
            else:
                return rIndex
        except:
            getAngle()

def findUnknown(a1,r1,a2,r2):
    if a1 == False:
        return 1
    elif r1 == False:
        return 2
    elif a2 == False:
        return 3
    elif r2 == False:
        return 4

def findMissingAngle(a1,r1,a2,r2):
    sineAngle = (math.sin(math.radians(a2)) * r2) / r1
    missingAngle = math.degrees(math.asin(sineAngle))
    print("The unkown angle is",missingAngle)

def findMissingRIndex(a1,r1,a2,r2):
    missingRIndex = (math.sin(math.radians(a2)) * r2) / math.sin(math.radians(a1))
    print("The unknown Refractive Index is",missingRIndex)

angleIncidence = getAngle()
rIndexIncidence = refractiveIndex()
angleReflection = getAngle()
rIndexReflection = refractiveIndex()
unknownvalue = findUnknown(angleIncidence,rIndexIncidence,angleReflection,rIndexReflection)

# n1 * sin()1 = n2 * sin()2

################
# Main Program #
################

if unknownvalue == 1:
    findMissingAngle(angleIncidence,rIndexIncidence,angleReflection,rIndexReflection)
elif unknownvalue == 2:
    findMissingRIndex(angleIncidence,rIndexIncidence,angleReflection,rIndexReflection)
elif unknownvalue == 3:
    findMissingAngle(angleReflection,rIndexReflection,angleIncidence,rIndexIncidence)
elif unknownvalue == 4:
    findMissingRIndex(angleReflection,rIndexReflection,angleIncidence,rIndexIncidence)
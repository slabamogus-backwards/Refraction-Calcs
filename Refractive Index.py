print("This program is intended to find the critical angle for a set of materials.")
print("-------------------------------------------------------------------------------------------------------------------------\n")

def getAngle():
    unknown = input("Is this angle unknown Y/N? ")
    if unknown == "Y":
        return "N"
    else:
        try:
            angleInput = float(input("What is the angle? "))
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
        return "N"
    else:
        try:
            rIndex = float(input("What is the refractive index? "))
            if rIndex < 1:
                refractiveIndex()
            else:
                return rIndex
        except:
            getAngle()


angleIncidence = getAngle()
rIndexIncidence = refractiveIndex()
angleReflection = getAngle()
rIndexReflection = refractiveIndex()

# n1 * sin()1 = n2 * sin()2
#Need to find an efficient way to figure out which one is unknown

print(angleIncidence,rIndexIncidence,angleReflection,rIndexReflection)
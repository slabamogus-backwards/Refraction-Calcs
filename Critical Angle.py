import math

def refractiveIndex():
    try:
        rIndex = float(input("What is the Refractive Index? "))
        if rIndex < 1:
            print("Enter a Refractive Index > 1")
            refractiveIndex()
        else:
            return rIndex
    except:
        print("Enter a refractive Index")
        refractiveIndex()

def calculator(rFast,rSlow):
    print("We are using {} as the rIndex of the medium light is leaving and {} as the rIndex light is entering\n".format(rSlow,rFast))

    ratioOfR = rFast/rSlow
    print("The critical angle is {} degrees (to 1 d.p)".format(round(math.degrees(math.asin(ratioOfR)),1)))
    print("The critical angle is {} radians (to 3 d.p)".format(round(math.asin(ratioOfR),3)))

################
# Main Program #
################

print("This program is designed to find the ciritical angle of a beam of light entering two seperate mediums.")
print("You enter two Refractive Index's of the mediums and the program will calculate the Refractive Index of the beam of light from the slow medium to the faster medium.\n")

rIndex1 = refractiveIndex()
rIndex2 = refractiveIndex()

if rIndex1 > rIndex2:
    calculator(rIndex2,rIndex1)
elif rIndex2 > rIndex1:
    calculator(rIndex1,rIndex2)

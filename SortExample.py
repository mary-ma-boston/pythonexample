arrNumbers = [-3,3,5,-5,7,-7,7,8,1]
arrNew = []

while arrNumbers:
    
    minimum = arrNumbers[0]

    for arrEle in arrNumbers:
        if arrEle < minimum:
            minimum = arrEle
    arrNew.append(minimum)
    arrNumbers.remove(minimum)

print(arrNew)




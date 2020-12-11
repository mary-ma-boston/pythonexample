def GetCountOfChar(ch, strInput):
    retValue = 0
    for chInput in strInput:
        if chInput == ch:
            retValue += 1

    return retValue

testStr = "assassination"
for ch in testStr:
    if GetCountOfChar(ch, testStr) <= 1:
        print(ch)
        break
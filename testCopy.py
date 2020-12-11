import copy
# originalData = {"name":"yue ma"}
# copyData = copy.deepcopy(originalData)
# copyData = originalData
# copyData["name"] = "pig"
# print(originalData["name"])

# strOriginalData = "yue ma"
# copyStrData = strOriginalData
# strOriginalData = "pig"
# print(copyStrData)

# originalData = {"name":"yue ma"}
# copyData = originalData
# originalData["name"] = "pig"
# print(copyData["name"])

# def testStrCopy(strInput):
#     strInput = "test pig"


# strOriginalData = "yue ma"
# testStrCopy(strOriginalData)
# print(strOriginalData)

originalData = [1,2,3,4]
copyData = originalData[:]
originalData[0] = 9
print(copyData)
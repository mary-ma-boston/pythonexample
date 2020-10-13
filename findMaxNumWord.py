from collections import Counter
from operator import itemgetter
from collections import OrderedDict
import operator

# Create an empty dictionary 
myDict = dict() 

myfiles = open("C:\\MaryCode\\pythonexample\\JobTitle.txt","r",encoding='utf-8')
lines = myfiles.read()
lines = lines.replace(",", " ")
lines = lines.replace(".", " ")
lines = lines.replace("..."," ")
lines = lines.replace(":"," ")
lines = lines.replace("\""," ")
lines = lines.replace("“"," ")
lines = lines.replace("/"," ")
lines = lines.replace("("," ")
lines = lines.replace(")"," ")
lines = lines.replace("\n"," ")
lines = lines.lower()
words = lines.split(" ")

for word in words:
    if word in myDict:
        if word == "python":
            print(word)
        myDict[word] = myDict[word] +1
    else:
        myDict[word] = 1

sorted_myDict = sorted(myDict.items(), key=operator.itemgetter(1))

for element in sorted_myDict:
    print(element) 
    

    




        



    
 

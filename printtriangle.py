# the star triangle
# the user gives a base length, to print a 



base_length = int(input("enter the base of the triangle: "))  
space = base_length-1
for row in range(base_length):
    row = row + 1
    print(" "*space,end="")
    print("*"*(2*row-1))
    space = space - 1

    
#def GetRandomData()
#    retResult = https.get(https://official-joke-api.appspot.com/jokes/programming/random)
#    if retResult != "6":

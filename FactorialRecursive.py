def myFactorial(x):
    if x <= 1:
        return 1
    
    else:
        return ( x * myFactorial(x-3))

num = 5
print("The factorial of", num , "is" , myFactorial(num))

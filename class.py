class Printtriangle:
    model = 1

    def __init__(self):       # instance-dependent method
        pass
    
    def Test(self):
        print("test")

    def Triangle(self,base_length):
        self.Test()
        #self.model
        space = base_length-1
        for row in range(base_length):
            row = row + 1
            print(" "*space,end="")
            print("*"*(2*row-1))
            space = space - 1    

n = int(input("enter the base of the triangle: "))       
p1 = Printtriangle()
p1.Triangle(n)
def show():
    print("hello")
show()

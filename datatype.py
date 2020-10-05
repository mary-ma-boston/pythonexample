# string str
x = "hello world"
print(type(x))

# numeric int float complex
x = 5
y = 5.1
z = 1 + 5j
print(type(x))
print(type(y))
print(type(z))

# sequence list tuple range
x = ["apple", "banana","orange"]
y = ("apple","banana","orange")
z = range(1,3)
#print(type(x))
#print(type(y))
#print(type(z))
print(x[2])
x[1] = "bananas"
print(x[1])
print(y[2])
for j in x:
    print(j)

for j in x:
    print(j)

print("-"*20)
first = True
for j in x:
    if first:
        first = False
        continue
    print(j)
print("-"*20)


print("*"*20)
for j in x[-2:]:
    print(j)
print("*"*20)


# mapping dict
dic = {"name":"mayue","age":18}

dic = {"name":"mayue","age":["x"]}
print(type(dict))
#print(dic["name"])
dic["name"] = "xukai"
for i in dic:
    #print(i)
    #print(dic[i])
    print(i+":"+str(dic[i]))


# set frozenset
mySet = {"BANANA","BANANA","ORANGE","APPLE"}
print(mySet)

# boolean bool
x = True
print(type(x))

# binary bytes bytearray memoryview
x = b"HELLO"
y = bytearray((15))
z = memoryview(bytes(5))
print(type(x))
print(type(y))
print(type(z))

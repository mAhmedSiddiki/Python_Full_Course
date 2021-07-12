# =============================================================================
# Function
# =============================================================================









def hey(a):
    return lambda b:a*b

x = hey(6)

print(x(6))
print(x(7))
print(x(8))


print(hey(5,7))




x = lambda a,b,c:a+b+c

print(hey(5,6,7))
print(x(5,6,7))

print((lambda a,b,c:a+b+c)(5,6,7))




















def china():
    # global z,m
    z = 12
    # m = 15
    
    def gansu():
        nonlocal z
        z = 17
        print("Gansu",z)
    
    gansu()
    print("China",z)

china()
















def bangladesh():
    global z
    z = 13
    print("Bangladesh",x,y,z,m)

x = 10
y = 11
z = 0

print("Global",x,y,z)
china()
bangladesh()
print("Global",x,y,z,m)




















def hey():
    x = 10
    
    def hello():
        print(x)
    
    hello()
    print(x)

hey()
















def count(no):
    if no == 3:
        return no
    else:
        return count(no+1)+1

print(count(1))
















def hello():
    
    for i in range(0,5):
        yield i
    
    # yield 1
    # yield "jadh"
    # yield ("sdjf","sdf")


# print(hello())

for i in hello():
    print(i)
















def hey():
    pass
    
hey()














def info(name,subtitle = "codinglaugh"):
    print(name,subtitle)
    
info("Marjuk","Student")
info("Ahmed")









def bazar(**world):
    
    for i,j in world.items():
        print(i,j)
    
    # print(world["item2"])

bazar(item1 = "Mango",item2 = "Egg")

















def marjuk():
    return "apple"

print(marjuk())












def summation():
    return 1+1

def subtraction():
    return 2-1

print(summation())
print(subtraction())

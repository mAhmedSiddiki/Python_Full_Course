# =============================================================================
# tuple()
# =============================================================================


a = ("Doreamon","sdjfhan","Tom and Jerry")
b = (1,2,3,4,5,3,3)

print(b.count(3))

print(sorted(a,reverse=True))

print(a.index("Tom and Jerry"))

print(sum(b))

print(min(b))

print(len(a))

print(b+a)

print(a*2)


if "Shinchan" in a:
    print("found")
else:
    print("not found")

for i in a:
    print(i)

a = ()

print(a)


b = list(a)

b.append("sjdhf")

print(a,b,sep="\n")
      
a = tuple(b)

print(a)




print(a)

print(a[-3:-1])



b = ("Doreamon",["Shinchan",2,3,4],("codinglaugh","marjuk"),1,4,7,2)

print(len(b[1]))

for i in b:
    if type(i) is list:
        for j in i:
            print(j)
    elif type(i) is tuple:
        for j in i:
            print(j)
    else:
        print(i)
    


b[1][0] = "djhbf"

print(b)

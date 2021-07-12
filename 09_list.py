# =============================================================================
# List
# =============================================================================

a = ["Doreamon",'Shinchan',"Tom and Jerry",
     1,3,4,'Shinchan',1.4]

b,c = ["Doreamon","dorejsdhfamon","Shinchan",
       'shhdsvssinchan'],[1,6,3,8,2,4]

print(sum(c))

print(min(b))

# def length(i):
#     return len(i)

# c.sort(reverse=True)
print(sorted(c,reverse=True))

# a.reverse()

print(a)

# print(a.count(1.4))

print(a.index("Doreamon"))









b = ["jdhbf",2,3,4,"jdshbf"]

print(b+a)

b = a.copy()

print(b)



if "Shinsjdbhfchan" in a:
    print("paichi")
else:
    print("Pai nai")

print(len(a))



for i in a:
    print(i)

#del a[1:4]

a.remove('Shinchan')

a.pop(2)

a.clear()

print(a)





# a[2] = "Meena"

# a[2:5] = ["Meena",2,"Hello"]





print(a)


a.append("Hey")

a.extend(["Hello","I","Am"])

a.insert(1,4)

print(a)


b = ["Doreamon",'Shinchan',["codinglaugh","marjuk",1,4],
     "Tom and Jerry",3,1,4,1.4]

# c = b[2].copy()

# print(c)

# print(["hey"]*2)


# print(len(b[1]))

c = []

for i in b:
    if type(i) is list:
        c = i.copy()
        # for j in i:
        #     print(j)
    else:
        print(i)

print(c)

# del b[2][0]


# b.append("hey")

# b[2][1] = 3

# b.insert(2,"hey")

print(b)

# -*- coding: utf-8 -*-

a = 'codinglaugh'
b = "codinglaugh"

print(a,type(a))
print(b,type(b))

c = "youtube channel name is 'codinglaugh'"
print(c)

d = '''codinglaugh
    learn
        something
everyday'''

print(d,type(d))

e = 'codinglaugh '
f = "learn "
g = "something "
h = "everyday "

# print(e+f+g+h+"marjuk")

print(e*5)

print("c" not in e)

print(len(e))

length = 0
for i in e:
    print(i,end="")
    length += 1
print()
print(length)







h = "codinglaugh"


if "codingdshflaugh" != h:
    print("matched")
else:
    print("something wrong")







i = "abc"
j = "ABC"

print(i>j)

# print(e[-12])

# print(e[:])
# e = e[:3]+"m"+e[4:]

# e = e[:3]+""+e[4:]

# del e[3]

print(e)


# =============================================================================
# String format()
# =============================================================================

a = "codinglaughsdh"
b = 4
c = 3.4534758

# d = a + " {1} {0:.3f}".format(c,b)

d = "{0:$>20} {1} {0} marjuk".format(a,"jsdbf")

print(d)





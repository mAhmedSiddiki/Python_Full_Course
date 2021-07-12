# =============================================================================
# None Boolean Number
# =============================================================================

#none

a = 10
a = None
a = 5

if a == None:
    print("Yes None")
else:
    print("Not none")

print(type(a))


#Boolean

print(type(10<20))
a = 10>20
if a == True:
    print("10 is small")
else:
    print("20 is big")
    
#int float complex
a = 3
print(a,type(a))

b = 3.476574
print(b,type(b))
print("{:.3f}".format(b))

#real and imaginary
c = 10 + 12j
print(c,type(c))

print(20.354j+c)

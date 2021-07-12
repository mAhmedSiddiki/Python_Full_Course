# =============================================================================
# print() or output
# =============================================================================

print("codinglaugh","learn","something","everyday",10,20,sep="*")

print("codinglaugh","hdsjbhfh",end="\n\n")
print("learn something everyday")

#pass value as parameter
a = "I"
b = "Love"
c = "You"

print("Hey",a,b,c)

#sequential formatiing pass value
a = "I"
b = "You"
c = "Me"

print("{} love {}".format(a, b))
print("{} love {}".format(b, c))

#number formatiing pass value
a = "I"
b = "You"
c = "Me"

print("{0} love {1}".format(a, b))
print("{1} love {0}".format(b, c))

#names formatiing pass value
a = "I"
b = "You"
c = "Me"

print("{name2} love {name}".format(name = a, name2=b))
print("{} love {}".format(b, c))


#tuple pass value
a = "I"
b = "You"
c = "Me"

print("%s love %s"%(a,b))
print("{} love {}".format(b, c))

#tuple pass value
a = "I"
b = "You"
c = "Me"

print("%(hoi)s love %(hey)s"%{"hey" : a,"hoi" : b})

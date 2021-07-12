# -*- coding: utf-8 -*-

# =============================================================================
# input()
# =============================================================================

a = input("Enter your name: ")
b = int(input("Enter your age: "))
c = float(input("Enter your result: "))

print("Name: {}\nAge: {}\nCGPA: {}".format(a,b,c))


a,b,c,d,e,f,g = input("Enter some number: ").split("*")
print("{} {} {} {} {} {} {}".format(a,b,c,d,e,f,g))
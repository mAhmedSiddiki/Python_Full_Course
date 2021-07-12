# -*- coding: utf-8 -*-

# =============================================================================
# Operators
# =============================================================================

#Arithmetic opertors
a = 10
b = 2

print(a + b)    #Addition
print(a - b)    #Subtraction
print(a * b)    #Multiplication
print(a / b)    #Division - float
print(a // b)   #Division - floor
print(a % b)    #Modulus
print(a ** b)   #Power

#Comparison / Relation operators
a = 12
b = 10

print(a == b)   #Equal
print(a != b)   #Not equal
print(a > b)    #Greater than
print(a < b)    #Less than
print(a >= b)   #Greater than equal
print(a <= b)   #Less than equal


#Logical operators

a = 10
b = 5

print(a == 11 and b == 5)   #AND
print(a == 11 or b == 6)    #OR
print(not b==3)     #NOT


#Membership operators

a = "codinglaugh"

print("coding" in a)    #in
print("codingshdf" not in a)    #not in


#Identity operators
a = 5
b = 6

print(a is b)   #is
print(a is not b)   #is not

#Bitwise operators
a = 10
b = 12

print(a | b)    #bitwise or(|) 

#Bitwise operators
a = 10

print(~a) #Bitwise not (~)

#Bitwise operators
a = 10
b = 12

print(a ^ b)    #Bitwise XOR (^)

#Bitwise operators
a = 12

print(a >> 2)   #Bitwise right shift(>>)

#Bitwise opeartors
a = 12

print(a << 2)     #Bitwise left shift


#Assignment operators
a = 10

a += 10 #a = a+10

print(a)

a = 10

a -= 10 #a = a-10

print(a)

a = 10

a *= 10 #a = a*10

print(a)

a = 10

a /= 10 #a = a/10

print(a)

a = 10

a //= 3 #a = a//3

print(a)

a = 10

a %= 3 #a = a%3

print(a)

a = 10

a **= 2 #a = a**2

print(a)
# =============================================================================
# Flow Control
# =============================================================================

#If - statement

a = "Chocolate"
b = "Cadfdfke"
c = "Shinchan"

if a=="Chocolate":
    print("Home work done")
    if c == "Doraemon":
        print("Eat food")
    else:
        print("Not eating")
elif b == "Cake":
    print("Home work done")
else:
    print("Home work not finished")

print("codinglaugh")


#while - loop

i = 1

while i<=5:
    print("okk")
    i += 1 # i = i+1 #1,2,3,4,5,6


#while - loop

while True:
    print("okkey")
    
#while - nested loop
i = 1
j = 1

while i<=5:
    while j<=5:
        print("i=",i," j=",j,sep="")
        j += 1
    else:
        print("j is end")
    i += 1
    j = 1
    
    
#for loop
a = "codinglaugh"
#tuple,list,set,dictionary,string

for i in a:
    print(i)
    
    
#range for loop

for i in range(1,11,3): #start,end,step
    print(i)


#nested loop
for i in range(1,6):
    for j in range(1,6):
        print("i=",i," j=",j,sep="")
    else:
        print("j is end")
        
        
# break
for i in range(1,6):
    pass

i = 1
while i<=5:
    if i == 3:
        pass
    print(i)
    i += 1


a = 5

a = None

print(type(20>2))

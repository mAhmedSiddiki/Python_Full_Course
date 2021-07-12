# =============================================================================
# Set - unordered | unindexed | no duplicate value
# =============================================================================

#Union
a,b = {1,2,5,4,7,9},{3,10,12,11}

print(a.isdisjoint(b))

print(b.issuperset(a))

print(a.issubset(b))







print(sorted(a,reverse=True))

print(a.union(b))


#Intersection
a,b = {1,2,4,7,9},{2,5,7,8}

b.intersection_update(a)

print(b)


#Difference
a,b = {1,2,4,7,9},{2,5,7,8}

b.difference_update(a)

print(b)


#Symmetric Difference
a,b = {1,2,4,7,9},{2,5,7,8}

print(min(a))

print(len(a))

print(sum(a))

a.symmetric_difference_update(b)

print(a)












a = {"Shinchan","Doreamon","Shinchan","Meena",
     2,5,3,3.4,("sdfh",2,3)}

b = {"shdgvhf","Shinchan"}

print(b.union(a))

print(sorted(b,reverse=True))

print(min(b))

print(sum(b))


c = frozenset(b)

c.add("Doremon")

print(b)

# b.update(a)

print(b.union(a))

# a.remove("Shinchdhan")

# a.pop()

# a.discard("Doresjdhfamon")

# a.clear()

print(a)


# del a

# a.add("Tom and Jerry")

a.update(["Tom and Jerry","Nobita"])

print(a)

for i in a:
    if type(i) is tuple:
        for j in i:
            print(j)
    else:
        print(i)
    

print(a)


# =============================================================================
# Dictionary - > key:value
# =============================================================================




a = {"cartoon1":"Doreamon",
     "jfhbjds":"Shinchan",
     "zgvdshgf":"Tom and Jerry"}

print(sorted(a,reverse=True))



print(len(a))

b = a.setdefault("cartoon4","jhdshf")

print(a,b,sep="\n\n")










a = ("name","email","phone")

b = dict.fromkeys(a)

for i in b:
    if i == "name":
        b["name"] = "Marjuk"
    elif i == "email":
        b["email"] = "djshf@hotmail.com"
    elif i == "phone":
        b["phone"] = "28748392"

print(b)












a = {"name":"Marjuk",
     "phone":"02536253625"}

print(a)

b = {"email":"marjuk@hotmail.com",
     "name":"Marjuk Ahmed Siddiki"}

a.update(b)

print(a)












a = {"cartoon1":"Doreamon",
     "cartoon2":"Shinchan",
     "cartoon3":"Tom and Jerry"}

print(a.items())

a.clear()

print(a)

print("cartoon3" in a)

for i,j in a.items():
    print(i,"=",j)

# print(b)

# del a["cartoon2"]

# a.get("cartoon3")

# a.pop("cartoon3")

# a.popitem()


# a["cartoon4"] = "Meena"
# a["cartoon2"] = "Meena"

print(a)



a = {"cartoon1":["Doreamon",2,3,4],
     "cartoon2":("sdhfhdf","dshjd",2,1,3),
     "cartoon3":{"one":1,
                 "two":2,
                 "three":3,
                 "four":4},
     "cartoon4":"Meena"}


for i,j in a.items():
    if type(j) is list:
        print("List: ")
        for i in j:
            print(i)
    elif type(j) is tuple:
        print("Tuple: ")
        for i in j:
            print(i)
    elif type(j) is dict:
        print("Dictionary: ")
        for i,k in j.items():
            print(i,"=",k)
    else:
        print(i, j)

# a["cartoon3"].pop("three")

# c = a["cartoon3"].copy()


# print(c)

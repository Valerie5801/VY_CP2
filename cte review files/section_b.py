#make an empty list
mylist = []

#add items
mylist.append(30)
mylist.append("mari")
mylist.append("mewo")
#[30, "mari", "mewo"]
print(mylist)

mylist.insert(2, "sunny")
#[30, "mari", "sunny", "mewo"]
print(mylist)

#remove items
mylist.remove("mewo")
#[30, "mari", "sunny"]
print(mylist)

mylist.pop(1)
#[30, "sunny"]
print(mylist)

#sorting a list (from section a)
numlist = [23, 2, 235, 9, 54, 187, 49, 41]
print(sorted(numlist))
numlist.sort()
print(numlist)

#loop through lists
for item in numlist:
    print(item)

#range
print("")
for i in range(10):
    print(i)

#enumerate
print("")
omori_list = ["sunny", "aubrey", "kel", "hero", "mari", "basil"]
enumerate(omori_list)
for char in omori_list:
    print(char)
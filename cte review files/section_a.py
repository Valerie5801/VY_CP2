#list
mylist = ["red", "blue", "yellow", 19, True]
#get value "yellow"
print(mylist[2])

#sorting a list
numlist = [23, 2, 235, 9, 54, 187, 49, 41]
print(sorted(numlist))
numlist.sort()
print(numlist)

#list comprehension
for item in mylist:
    print(item)
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
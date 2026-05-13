#string operations
string_one = "Welcome to white space."
string_two = "Everything is going to be okay."

#comparison operators
if string_one == string_two:
    print("These are the same strings")
else:
    print("These are different strings")

#find the length
print(f'"{string_one}" has {len(string_one)} characters.')

#slicing strings
part_string = string_one[11:22]
print(part_string)

#combining strings
protag = "Sunny"
sibling = "Mari"
sentence = protag + " and " + sibling + " are siblings."
print(sentence)

#find part of a string
print(protag.find("Sun"))
try:
    print(sibling.index("Something"))
except:
    print("that is not in the string")

#insert text
friends = "Sunny, Kel, Aubrey, Hero"
friends += ", Mari, Basil"
print(friends)
friends = friends.replace("Sunny", "OMORI")
print(friends)
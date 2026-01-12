#VY 2nd Types of Lists Notes

#Lists
characters = ["Mari", "Aubrey", "Kel", "Hero", "Basil", "Sunny"]
characters[-1] = "OMORI"
characters.append("Mari") #dupes allowed
print(characters)

#Tuples
white = (255, 255, 255)
#white[1] = 0   Tuples are immutable
#Unpack a tuple
red,green,blue = white
print(red)

#Set
bosses = {"Sweetheart", "Unbread Twins", "Capt. Spaceboy", "The Hooligans"}
#no order and no duplicates
print(bosses)
bosses.remove("The Hooligans")
bosses.add("Mr. Jawsum")
#VY 2nd Writing Notes

"""with open("notes/sample.txt", "a") as file:
    file.write("\nDoughie\n")
    file.write("Biscuit\n")
    file.write("Captain Spaceboy\n")
    file.write("Sweetheart")
    #wawa

print("WONDERHOY!")"""

"""something = []
with open("notes/sample.txt", "r+") as file:
    for line in file:
        something.append(line.strip())
    
    index = something.index("Sunny")
    something[index] = "OMORI"

    file.truncate(0)   #clear file

    for name in something:
        file.write(name + "\n")

print("we done")"""

import csv                               #newline makes a new line between each line
"""with open("notes/test.csv", "w", newline='') as csvfile:
    fieldnames = ['username', 'favorite color']
    writer = csv.writer(csvfile)

    #writer.writerow(fieldnames)
    writer.writerow(["cosmic_voyager", "indigo"])
    writer.writerow(["tech_wizard", "turquoise"])"""

users = [
    {"username":"cosmic_voyager", "favorite color":"indigo"},    #using dictionaries
    {"username": "tech_wizard", "favorite color":"turquoise"}, 
    {"username":"nature_lover", "favorite color":"emerald"}, 
    {"username":"bookworm42", "favorite color":"maroon"}
    ]
with open("notes/test.csv", "r+", newline='') as csvfile:
    fieldnames = ['username', 'favorite color']   #first line of the csv so as we iterate over dictionary it will ignore username and color
    #writer = csv.writer(csvfile)
    reader = csv.reader(csvfile)
    writer = csv.DictWriter(csvfile, fieldnames)

    #writer.writerow(fieldnames)
    #writer.writerow(["cosmic_voyager", "indigo"])   using loists
    #writer.writerow(["tech_wizard", "turquoise"])
    writer.writerows(users)
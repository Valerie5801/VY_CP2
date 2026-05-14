import csv
#text file
with open("cte review files/strand 2/test.txt", "w") as file:
    file.write("Doughie\n")
    file.write("Biscuit\n")
    file.write("Captain Spaceboy\n")
    file.write("Sweetheart\n")

with open("cte review files/strand 2/test.txt", "a") as file:
    file.write("Mr. Jawsum")

list = []
with open("cte review files/strand 2/test.txt", "r") as file:
    for line in file:
        list.append(line.strip())
print(list)

#csvs
with open("cte review files/strand 2/test_csv.csv", "w", newline="") as file:
    fieldnames = ["name", "item"]
    writer = csv.writer(file)

    writer.writerow(["Omori", "knife"])
    writer.writerow(["Sunny", "violin"])

characters = [{"name": "Omori", "item": "knife"},
              {"name": "Sunny", "item": "violin"},
              {"name": "Aubrey", "item": "baseball bat"},
              {"name": "Kel", "item": "ball"}
              ]
with open("cte review files/strand 2/test_csv.csv", "r+", newline="") as file:
    fieldnames = ["name", "item"]

    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer = csv.DictWriter(file, fieldnames)
    writer.writerows(characters)

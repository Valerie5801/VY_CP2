#VY 2nd Reading Files
import csv

try:
    with open("notes/sample.txt", "r") as file:
        content = []
        for line in file:
            content.append(line.strip())
except:
    print("that file doesn't exist sadly")
else:
    for line in content:
        print(f"Hello {line}")


try:
    with open("notes\Class CSV Sample.csv", mode= "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)    #next grabs the next value in CSV reader
        users = []
        for line in reader:      #bulid a dictionary to show the username a user and their favorite color
            users.append(
                {
                    header[0]: line[0],
                    header[1]: line[1]
                }
            )
except:
    print("CSV doesn't exist")
else:
    for user in users:
        print(user)
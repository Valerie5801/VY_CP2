#global
character = "Sunny"
#local
def make_side():
    side_chars = ["Aubrey", "Kel", "Hero", "Basil"]
    side_chars.append("Mari")
    for char in side_chars:
        print(char)

make_side()

#using keyword "global"
def global_var():
    global x
    x = 10

global_var()
x += 3
print(x)
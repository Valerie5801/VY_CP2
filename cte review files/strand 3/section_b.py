def add(num1, num2):
    total = num1 + num2
    return total

def set_add():
    total = 2 + 3
    return total

def mult(num1 = 3, num2=5):
    total = num1 * num2
    if total < 0:
        return False
    else:
        return total

print(add(4, 3))
print(set_add())
print(mult())
print(mult(-1, 5))
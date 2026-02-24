#VY 2nd Recursion Notes

number = 5
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)


def factor(num):
    if num == 1: return 1
    return num * factor(num-1)   #function calls itself

print(factor(5))
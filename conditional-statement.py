# Take three user inputs and the print the greatest number from those inputs
# using the if-else condition.
a = int(input('Enter an integer value for a: '))
b = int(input('Enter an integer value for b: '))
c = int(input('Enter an integer value for c: '))

def greatestnumber(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(greatestnumber(a, b, c))

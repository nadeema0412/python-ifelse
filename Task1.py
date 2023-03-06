# create a list containing squares of numbers from 1 to 10.
def squarenumbers():
    block = []
    for i in range(1, 11):
        block.append(i ** 2)
    return block

print(squarenumbers())



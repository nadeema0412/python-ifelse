# write a function that takes an array and returns another array that contains
# the members of the first array that are even.
def EvenList(numbers):
    NewList = []
    for i in numbers:
        if i % 2 == 0:
            NewList.append(i)  # add each new value to the new list.
    return NewList

List = [2, 8, 72, 13, 142, 8]
print(EvenList(List))

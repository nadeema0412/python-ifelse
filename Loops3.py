# Create a list from user input that is having random integer values and with the for loop,
# fetch the prime numbers and print the numbers.
array = []
def ElementsOfList():
    n = int(input('Enter the number of the elements for the list: '))  # The number of elements as the inputs
    for i in range(0, n):
        values = int(input())

        array.append(values)  # this adds all the elements to the list

def ForPrimeNumbers(ListOfNumbers):
    myList = array
    print('Your list is: ')
    print(array)
    print('Prime numbers in your list is/are: ')
    for num in myList:
       if num > 1:  # Prime number are always greater than 1
        for i in range(2, num):
           if (num % i) == 0:
            break
        else:
            print(num)
 
(ElementsOfList())
print(ForPrimeNumbers(array))









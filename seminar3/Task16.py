import random
def validate(text):
    while((num:= input(text)).isdigit() == False):
        print('It\'s not a number, try again ')
    return int(num)
def createRandomList(size, min, max):
    return [random.randint(min,max) for num in range(size)]
def findQuantityOfNumber(array, numberToFind):
    count = 0
    for num in array:
        if num == numberToFind:
            count += 1
    return count
size = validate('Enter quantity of elements ')
min = validate('Enter min nalue ')
max = validate('Enter max value ')
findNumber = validate('Enter a number that you wanna find ')
rand_list = createRandomList(size, min, max)
quantityOfNumber = findQuantityOfNumber(rand_list, findNumber)
print(f'Initial array: {rand_list} \n The number that you are looking for: {findNumber}\n Quantity of this numbers: {quantityOfNumber}')
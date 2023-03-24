import random
import math
def validate(text):
    while((num:= input(text)).isdigit() == False):
        print('It\'s not a number, try again ')
    return int(num)
def createRandomList(size, min, max):
    return [random.randint(min,max) for num in range(size)]
def getClosest(array, number, maxElem):
    closestNum = array[0]
    dif = max + 1000
    for index, num in enumerate(array):
        if index == 0: continue
        if num > number and dif > num - number:
            dif = num - number
            closestNum = num
        elif num <= number and dif >= number - num:
            dif = number - num
            closestNum = num
    return closestNum
size = validate('Enter quantity of elements ')
min = validate('Enter min nalue ')
max = validate('Enter max value ')
findNumber = validate('Enter a number that or close to which you wanna find ')
rand_list = createRandomList(size, min, max)
closestNum = getClosest(rand_list, findNumber, max)
print(f'Initial array: {rand_list} \n The number that you are looking for: {findNumber}\n The closest number in array is: {closestNum}')
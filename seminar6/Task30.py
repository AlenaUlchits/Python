firstNum = int(input('Enter the first element: '))
d = int(input('Enter the difference of progression: '))
size = int(input('Enter a quantity of elements in progression: '))
lastNumber = firstNum + d*size
result = [item for item in range(firstNum, lastNumber, d)]
print(f'array: {result}')
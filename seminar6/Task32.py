import random
origin = [random.randint(-10, 10) for num in range(random.randint(2, 10))]
print(f'original array: {origin}')
min = int(input('Enter minimal value: '))
max = int(input('Enter max value: '))
result = []
for ind, item in enumerate(origin):
    if min <= item <=max:
        result.append(ind)
print(f'indexes of elements by your criteria: {result}')

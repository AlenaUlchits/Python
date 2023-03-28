import random
length = int(input('Enter length of plant: '))
plant = [random.randint(1, 10) for _ in range(length)]

max = 0
max_index = 0
sum = 0

for index in range(-1, length - 1):
    sum = plant[index - 1] + plant[index] + plant[index + 1]
    if max < sum:
        max = sum
        max_index = index

# normalize index
if max_index < 0:
    max_index += length

print(f'we get this plant: {plant}')
print(f'we can get {max} from bush #{max_index}')
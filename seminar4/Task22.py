import random
n = int(input('Enter size of first set: '))
m = int(input('Enter size of second set: '))

# getting list
n_list = [random.randint(n // 2, n * 2) for _ in range(n)]
m_list = [random.randint(m // 2, m * 2) for _ in range(m)]

# make unique
n_unique = set(n_list)
m_unique = set(m_list)

# make intersection
result = [item for item in n_unique.intersection(m_unique)]

# make sort
result.sort()

# answer
print('first:', n_list)
print('second:', m_list)
print('result:', result)
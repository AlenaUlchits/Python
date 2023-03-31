def sum(a:int, b:int)->int:
    if a == 0: 
        return b
    return int(sum(a - 1, b + 1))

first_number = float(input('Enter first number: '))
second_number = float(input( 'Enter second number: '))

result = sum(first_number,second_number)
print(f'result: {result}')
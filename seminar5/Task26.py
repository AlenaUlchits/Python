def pow(number:float, power:int)-> float: 
    if power < 0: 
        power *= -1
        number = 1 / number
    if power == 1 : return number
    return number * pow(number, power - 1)

number = float(input('Enter number: '))
power = float(input( 'Enter  power: '))

result = pow(number, power)
print(f'result: {result}')
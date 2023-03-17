def sumOfDigits(source):
    sum = 0
    while source != 0:
        sum += source % 10
        source //=10
    return sum
def numberValidation(text):
    while((num:= input(text)).isdigit() == False):
        print('It\'s not a number, try again ')
    return int(num)
num = numberValidation('Enter a number: ')
sum = sumOfDigits(num)
print('Digit\'s sum of ', num, 'is',sum)

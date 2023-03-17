def numberValidation(text):
    while((num:= input(text)).isdigit() == False or (100000 <= int(num)< 1000000)==False):
        print('It\'s not a number or it doesn\'t contain 6 digits, try again ')
    return int(num)
def sumOfDigits(source):
    sum = 0
    while source != 0:
        sum += source % 10
        source //=10
    return sum
num = numberValidation('Enter a ticket number: ')
sumOfFristDigits = sumOfDigits(num // 1000)
sumOfLastDigits = sumOfDigits(num % 1000)
if sumOfFristDigits == sumOfLastDigits:
    print('You have a lucky ticket')
else:
    print('Try your luck the next time')
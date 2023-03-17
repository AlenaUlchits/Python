def numberValidation(text):
    while((num:= input(text)).isdigit() == False):
        print('It\'s not a number, try again ')
    return int(num)

m = numberValidation('Enter length of the first chocolate side: ')
n = numberValidation('Enter length of the second chocolate side: ')
k = numberValidation('Into how many bars do you wanna break: ')

if k >= m*n:
    print('It\'s too many')
elif k % m == 0 or k % n == 0:
    print('It\'s possible to devide')
else:
    print('Not possible to devide')
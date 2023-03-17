def cranesValidation(text):
    while((cranes:=input(text)).isdigit()==False or int(cranes) % 6 != 0):
        print('Not possible to devide between children and/or is not a number, try again: ')
    return int(cranes)
cranes = cranesValidation('Enter quantity of cranes ')
peter = cranes // 6
sergey = peter
kate = 2*(peter+sergey) 
print('Peter made ',peter,'cranes, Sergey made ',sergey,'cranes and Kate made ',kate,'cranes')
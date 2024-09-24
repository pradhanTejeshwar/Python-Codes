weight = int(input('Weight: '))
unit = input(f'(L)bs or (K)g: ')
if unit.lower() == 'l' :
    conversion = weight * 0.453592
    kg = "{0:.2f}".format(conversion)
    print(f'You are {kg} kilos')
else :
    conversion = weight / 0.453592
    lbs = "{0:.2f}".format(conversion)
    print(f'You are {lbs} pounds')
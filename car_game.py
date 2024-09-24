command = ''
started = False
while True :
    command = input('>').lower()
    if command == 'start' :
        if started :
            print('Car is already started ! You do not need to start it again !')
        else :
            started = True
            print('Car started !')
    elif command == 'stop' :
        if started :
            started = False
            print('Car stopped !')
        else :
            print('Car is already Stopped ! You do not need to stop it again !')
    elif command == 'help' :
        print('''        Type :-
start - to start the car
stop - to stop the car
quit - to quit the game
        ''')
    elif command == 'quit' :
        break
    else :
        print("Sorry ! I don't undertand that !")
        print(command)
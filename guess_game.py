import random

secret_code = random.randrange(0,9)
guess_count = 1
guess_limit = 3
while guess_count <= guess_limit :
    secret = int(input('Guess : '))
    guess_count += 1    
    if(secret_code == secret) :
        print('You have Won !')
        break
else :
    print('You have failed !')
import random
import os

mylist=['rock','paper','scissors']
cw=0
uw=0
while True:
    os.system('cls')
    f=random.choice(mylist)
    print('komputerin hesabi: ',cw,'userin hesabi: ',uw)
    user=input('rock/paper/scissors?')
    user=user.lower()
    print('komputerin secimi: ',f)
    if user not in ('rock','paper','scissors','q'):
        print('duzgun variant secin')
        continue
    elif user=='q':
        exit=input('are you sure? (y/n)')
        if exit.lower()=='y':
            print('oyun bitdi')
            break
        else:
            continue
    else:
        if f==user:
            print('hech heche')
        elif f=='rock':
            if user=='paper':
                uw+=1
                print('user wins')
            elif user=='scissors':
                cw+=1
                print('computer wins')
        elif f=='paper':
            if user=='rock':
                cw+=1
                print('computer wins')
            elif user=='scissors':
                uw+=1
                print('user wins')
        elif f=='scissors':
            if user=='rock':
                uw+=1
                print('user wins')
            elif user=='paper':
                cw+=1
                print('computer wins')

if uw>cw:
    print('user won')
elif uw==cw:
    print('hech heche')
else:
    print('user lost')



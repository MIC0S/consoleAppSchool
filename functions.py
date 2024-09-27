import os
from database import Database


db = Database()


def shutdown():
    print('Program killed')
    return -1


def echo(args):
    print('echod: ', end='')
    print(*args[1:])
    return 0


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Screen cleared')
    return 0


def helpExt():
    print(f"""List of available commands:
shutdown                 - shuts down the program
echo [text]              - repeats all arguments back
cls                      - clears console
help                     - gives this list
repeat [amount] [text]   - repeats [text] given [amount] of times
adduser [name] [pwd]     - creates new user with [name] and [pwd] password""")
    return 0


def repeat(args):
    try:
        if len(args) < 3:
            print('Too few args!')
        else:
            amount = int(args[1])
            text = " ".join(args[2:])
            print(amount * text)
    except ValueError:
        print('Invalid args given!')
    return 0


def adduser(args):
    if len(args) == 3:
        status = db.createUser(args[1], args[2])
        if status == -1:
            print('Username claimed')
        else:
            print('User added successfully!')
    else:
        print('wrong arguments!')
    return 0

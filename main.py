import os
from database import Database

db = Database()

def execute(command, arguments):
    if command == 'shutdown':
        print('Program killed')
        return -1
    if command == 'echo':
        print('echod: ', end='')
        print(*arguments[1:])
        return 0
    if command == 'cls':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Screen cleared')
        return 0
    if command == 'help':
        print(f"""List of avaliable commands:
shutdown                 - shuts down the program
echo [text]              - repeats all arguments back
cls                      - clears console
help                     - gives this list
repeat [amount] [text]   - repeats [text] given [amount] of times
adduser [name] [pwd]     - creates new user with [name] and [pwd] password""")
        return 0
    if command == 'repeat':
        try:
            amount = int(arguments[1])
            text = " ".join(arguments[2:])
            print(amount*text)
        except:
            print('Invalid args given!')
        return 0
    if command == 'adduser':
        if len(arguments) == 3:
            status = db.createUser(arguments[1], arguments[2])
            if status == -1:
                print('Username claimed')
            else:
                print('User added successfully!')
        else:
            print('wrong arguments!')
        return 0


def auth():
    used_attempts = 0
    while True:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if db.authUser(username, password):
            return True
        else:
            used_attempts += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            if used_attempts >= 3:
                return False
            else:
                print(f'Incorrect Credentials, please try again:\nTotal attempts {used_attempts}/3')





def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    authStatus = auth()
    if not authStatus:
        print('Auth failed')
        return -1
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Welcome!')
    while True:
        command_list = input().split()
        command = None
        if len(command_list) > 0:
            command = command_list[0].lower()
        else:
            pass
        try:
            res = execute(command, command_list[0:])
            if res == -1:
                return 0
        except BaseException as error:
            print(f'Error during code execution: {error}')


if __name__ == '__main__':
    main()

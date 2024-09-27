import os
from database import Database
import functions as f

db = Database()


def execute(command, args):
    if command == 'shutdown':
        return f.shutdown()
    if command == 'echo':
        return f.echo(args)
    if command == 'cls':
        return f.cls()
    if command == 'help':
        return f.helpExt()
    if command == 'repeat':
        return f.repeat(args)
    if command == 'adduser':
        return f.adduser(args)


def auth():
    used_attempts = 0
    while True:
        username = input('Enter username: ')
        password = input('Enter password: ')

        if db.authUser(username, password):
            return username
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
    print(f'Welcome, dear {authStatus}')

    while True:
        print(authStatus, end="> ")
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

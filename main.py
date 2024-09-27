import os


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
shutdown         - shuts down the program
echo             - repeats all arguments back
cls              - clears console
help             - gives this list""")
        return 0


def main():
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
                return
        except BaseException as error:
            print(f'Error during code execution: {error}')


if __name__ == '__main__':
    main()

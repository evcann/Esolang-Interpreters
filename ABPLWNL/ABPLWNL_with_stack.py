def ABPLWNL_input(program):
    commands = list(program)

    a, b = 0, 0
    stack = []

    for i, command in enumerate(commands):
        match (command):
            case '1':
                a += 1
            case '2':
                if a != 0:
                    a -= 1
            case '3':
                a, b = b, a
            case '4':
                if b != 0:
                    b -= 1
                    a += 1
            case '5':
                a += b
                b = 0
            case '6':
                print(b, end='')
            case '7':
                print(chr(b), end='')
            case '8':
                a = 0
            case '9':
                try: 
                    b = int(input(':'))
                except ValueError:
                    print("\nError: invalid literal for int with base 10")
                    print(f"Command: {command}, index: {i}")
                    exit()
            case 'a':
                if not a:
                    commands.pop(i+1)
            case 't':
                stack.append(a)
            case 'u':
                if len(stack) > 0:
                    a = stack.pop()
                else:
                    print(f"Stack underflow error.")
                    print(f"Command: {command}, index: {i}")
                    exit()
            case 'e':
                exit()
            case _:
                print(f"\nInvalid command {command} at index {i}.")
                exit()

if __name__ == "__main__":
    try:
        program_input = open("ABPLWNL/in.{{{files}}}", 'r').read()
    except FileNotFoundError:
        open("ABPLWNL/in.{{{files}}}", 'x')
        print("Place program in ABPLWNL/in.{{{files}}}, then run again.")
        exit()

    ABPLWNL_input(program_input)
    print('\n')
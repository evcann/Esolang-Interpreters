from ABPLWNL import ABPLWNL_input

def shift_right(a):
    a.insert(0, a.pop())

def IMPOSSIBLE_input(program, ignore_unknown = False, output_code = False):
    commands_stack = []
    program_list = list(program)

    commands = ['>', '<', '.']

    command_pointer = 1

    for command in program_list:
        if command == commands[0]:
            command_pointer += 1
            if command_pointer == 10:
                command_pointer = 1
        
        elif command == commands[1]:
            command_pointer -= 1
            if command_pointer == 0:
                command_pointer = 9

        elif command == commands[2]:
            commands_stack.append(str(command_pointer))

        else:
            if not ignore_unknown:
                print(f"Unknown command: {command}")
                exit()

        shift_right(commands)

    if output_code:
        return ''.join(commands_stack)
    else: 
        ABPLWNL_input(''.join(commands_stack))

if __name__ == "__main__":
    IMPOSSIBLE_in = input("Enter code:")
    IMPOSSIBLE_input(IMPOSSIBLE_in)
    print('\n')
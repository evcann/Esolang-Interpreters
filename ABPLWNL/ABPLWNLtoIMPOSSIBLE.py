ABPLWNL_code = open("ABPLWNL/in.ABPLWNL", 'r').read()

for x in ABPLWNL_code:
    match (x):
        case 'a':
            print("The 'a' command is not supported in !I!M!P!O!S!S!I!B!L!E!")
            exit()
        case '0':
            print(f"Invalid command: {x}")
            exit()
    try:
        int(x)
    except ValueError:
        print(f"Invalid command: {x}")
        exit()

def shift_right(a):
    a.insert(0, a.pop())

ABPLWNL_code = tuple(map(int, tuple(ABPLWNL_code)))

command_pointer = 1
commands = ['>', '<', '.']
command_stack = []

for command in ABPLWNL_code:
    difference = command - command_pointer

    if difference > 0:
        for i in range(difference):
            command_stack.extend(commands[0])
            command_pointer += 1
            shift_right(commands)
    if difference < 0:
        for i in range(-difference):
            command_stack.extend(commands[1])
            command_pointer -= 1
            shift_right(commands)

    command_stack.append(commands[2])
    shift_right(commands)

output_file = open("ABPLWNL/out.IMPOSSIBLE", 'w')
print("Code has been translated and written to ABPLWNL/out.IMPOSSIBLE")
output_file.write(''.join(command_stack))
output_file.close()
from textwrap import wrap

input_string = open("3 bits, 1.5 bytes/in", 'r').read()

if set(input_string) != {'0', '1'}:
    print("Your program must be written in binary as text and only contain 0 and 1.")
    exit()

if len(input_string) > 12:
    print(f"Memory overflow error: your program has {len(input_string)} bits! Only 12 bits or less are supported.")
    exit()

if len(input_string) / 3 != float(len(input_string) // 3):
    print("Your code must be made up of groups of 3 bits!")
    exit()

memory = wrap(input_string, 3)

def ACT(x):
    out = []
    for digit in x:
        match (digit):
            case '0':
                out.append('1')
            case '1':
                out.append('0')
    return ''.join(out)

def logic(a, b, operator):
    out = []
    for i in range(3):
        match (operator):
            case "OR":
                if a[i] == '1' or b[i] == '1':
                    out.append('1')
                else:
                    out.append('0')
            case "XOR":
                if a[i] != b[i]:
                    out.append('1')
                else:
                    out.append('0')
            case "NAND":
                if not (a[i] == '1' and b[i] == '1'):
                    out.append('1')
                else:
                    out.append('0')
    return ''.join(out)

command_pointer = 0

while True:
    if command_pointer >= len(memory):
        command_pointer = command_pointer // len(memory)
    match (memory[command_pointer]):
        case '000': # NOT
            command_pointer += 1
        case '001': # ACT
            memory[command_pointer + 1] = ACT(memory[command_pointer + 1])
            command_pointer += 2
        case '010': # JMP
            addr = memory[command_pointer + 1]
            command_pointer = int(addr, 2)
        case '011': # CJM
            addr = memory[command_pointer + 2]
            if memory[command_pointer + 1] != '000':
                command_pointer = int(addr, 2)
        case '100': # OR
            # This language does not specify where the results of logical operations are stored, so I have to make some assumptions :(
            memory[command_pointer + 1] = logic(memory[command_pointer + 1], memory[command_pointer + 2], "OR")
            memory[command_pointer + 2] = '000'
            command_pointer += 3
        case '101': # XOR
            memory[command_pointer + 1] = logic(memory[command_pointer + 1], memory[command_pointer + 2], "XOR")
            memory[command_pointer + 2] = '000'
            command_pointer += 3
        case '110': # NAND
            memory[command_pointer + 1] = logic(memory[command_pointer + 1], memory[command_pointer + 2], "NAND")
            memory[command_pointer + 2] = '000'
            command_pointer += 3
        case '111': # END
            print(memory)
            exit()
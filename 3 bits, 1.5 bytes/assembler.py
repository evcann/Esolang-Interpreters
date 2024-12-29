file = open("3 bits, 1.5 bytes/in.3basm", 'r').read()

lines = file.splitlines()

out = []

commands = {
    "NOT": "000",
    "ACT": "001",
    "JMP": "010",
    "CJM": "011",
    "OR": "100",
    "XOR": "101",
    "NAND": "110",
    "END": "111"
}

for line in lines:
    out.append(commands[line.split()[0]])
    if len(line.split()) > 1:
        args = line.split()[1].split(",")
        out.extend((arg.replace('b', '') for arg in args))

print(out)
print(''.join(out))
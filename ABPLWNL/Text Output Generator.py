text_input = input("Enter text: ")
input_as_list = list(text_input)
program_commands = []

b = 0

for i, letter in enumerate(input_as_list):
    unicode_value = ord(letter)
    difference = unicode_value - b

    if input_as_list[i - 1] == letter:
        continue # Skip repeated letters as that is already handled

    if difference >= 0:
        program_commands.extend('1' * difference)
    else:
        program_commands.extend('2' * -difference)

    if i+1 == len(input_as_list):
        program_commands.extend(('3', '7')) # 3 command is not needed at the end because the program ends
        print(''.join(program_commands))

    elif input_as_list[i + 1] != letter:
        program_commands.extend(('3', '7', '3')) # Regular case, where there are no repeated letters

    else:
        repeats_count = 0
        for x in input_as_list[i:]:
            if x == letter:
                repeats_count += 1
            else:
                break
        program_commands.extend(('3', '7'*repeats_count, '3'))
        # This can be optimized more for cases of repeats at the end of the text
        # For example: "Bass" would unnecessarily add a 3 command at the end

    b = unicode_value
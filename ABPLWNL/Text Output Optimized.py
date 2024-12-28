text_input = input("Enter text: ")
input_as_list = list(text_input)
program_commands = []

a, b = 0, 0

for letter in input_as_list:
    if b != letter:
        difference_a = ord(letter) - a
        difference_b = ord(letter) - b

        least_difference = min(abs(difference_a), abs(difference_b))

        if least_difference == abs(difference_b) and abs(difference_b) < abs(difference_a):
            program_commands.append('3')
            a, b = b, a
        
        if a >= ord(letter):
            program_commands.extend('2'*least_difference)
            a -= least_difference
        else:
            program_commands.extend('1'*least_difference)
            a += least_difference
            
        program_commands.extend(('3', '7'))
        a, b = b, a
    else:
        program_commands.append('7')

output_file = open("ABPLWNL/out.ABPLWNL", 'w')
print("Output has been sucessfully generated and written to ABPLWNL/out.ABPLWNL")
output_file.write(''.join(program_commands).replace('33', ''))
output_file.close()
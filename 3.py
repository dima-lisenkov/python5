"""Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
"""
file_4code = 'rle_4code.txt'
file_coded = 'rle_coded.txt'
file_decoded = 'decoded.txt'

my_textes = []


with open(file_4code, 'r') as f1:
    for row in f1:
        my_textes.append(row.rstrip('\n'))


print(f'Прочитано из файла для кодирования {my_textes}')


def LineCoder(my_string: str) -> str:
    result_line = ''
    current_char = my_string[0]
    counter = 0
    for i in range(len(my_string)):
        if current_char == my_string[i]:
            counter += 1
        else:
            result_line += f'{counter}{my_string[i-1]}'
            counter = 1
        if i == len(my_string)-1:
            result_line += f'{counter}{my_string[i]}'
        current_char = my_string[i]
    
    return result_line



with open(file_coded, 'w') as f2:
    for elem in my_textes:
        f2.write(f'{LineCoder(elem)}\n')


coded_textes = []
with open(file_coded, 'r') as f3:
    coded_textes = f3.readlines()

print(f'Прочитано из файла для декодирования {coded_textes}')

def LineDecoder(coded_string='1B4A') -> str:
    digits_list = [str(i) for i in range(10)]
    result_string = ''
    num_str = ''
    count = 0
    for i in range(len(coded_string)):
        if coded_string[i] in digits_list:
            num_str += coded_string[i]
        else:
            if num_str=='':
                count = 0
            else:
                count = int(num_str)
           
            for c in range(count):
                result_string += coded_string[i]
            num_str = ''
    return result_string

with open(file_decoded, 'w') as f4:
    for elem in coded_textes:
        f4.write(f'{LineDecoder(elem)}\n')
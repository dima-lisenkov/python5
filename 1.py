"""Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

text_line = 'абв грачи идут по лесу'

def DelIn(text_line: str, del_string: str) -> str:
    text_list = text_line.split()
    result_list = list(filter(lambda x: not CheckLine(x, del_string), text_list))
    result_text = ' '.join(result_list)
    return result_text        
    
def CheckLine(string_line: str, inner_line: str) -> bool:
    step = len(inner_line)
    for i in range(len(string_line)):
        if string_line[i:i+step] == inner_line:
            return True
    return False


print(DelIn(text_line, del_string='абв'))
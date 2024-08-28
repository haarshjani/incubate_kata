import re

def add(number):
    
    result = 0
    deliminator = ","

    deliminator_re = re.search("//(.*)\n",number)
    if deliminator_re :
        deliminator = deliminator_re.group(1)
        deliminator_to_remove = "//"+deliminator+"\n"
        number = number.replace(deliminator_to_remove,'')

    numbers = number.split(deliminator)

    if(len(number) == 0):
        return result
    # elif(len(numbers) == 1):
    #     return int(numbers[0])
    for x in numbers:
       result += int(x)

    return result


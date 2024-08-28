import re

def add(number):
    
    result = 0
    deliminator = ","
    negatives = []

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
       if(int(x) < 0):
           negatives.append(x)
       result += int(x)
       
    if(len(negatives) > 0) :
        raise ValueError("negative numbers not allowed" + ','.join(negatives))
        
    return result


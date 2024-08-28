

def add(number):
    
    numbers = number.split(",")
    result = 0

    if(len(number) == 0):
        return result
    # elif(len(numbers) == 1):
    #     return int(numbers[0])
    for x in numbers:
       result += int(x)

    return result


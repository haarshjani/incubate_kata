

def add(number):
    
    numbers = number.split(",")

    if(len(number) == 0):
        return 0
    elif(len(numbers) == 1):
        return int(numbers[0])
    elif(len(number) == 0):
        return 0

    return int(numbers[0]) + int(numbers[1])


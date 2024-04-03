def countdown(num):
    list = []
    counter = num
    while counter >= 0:
        list.append(counter)
        counter -= 1
    return list

def print_and_return(list):
    print(list[0])
    return(list[1])

def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

def greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for num in list:
        if num > list[1]:
            new_list.append(num)
    print(len(new_list))
    return(new_list)

def length_and_value(size,value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list
def make_it_big(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list

def count_positives(list):
    count = 0
    for num in list:
        if num > 0:
            count += 1
    list[len(list) - 1] = count
    return list

def sum_total(list):
    sum = 0
    for num in list:
        sum += num
    return sum

def average(list):
    return (sum_total(list) / len(list))

def length(list):
    count = 0
    for num in list:
        count += 1
    return count

def minimum(list):
    if len(list) == 0: return False
    elif len(list) == 1: return list[0]
    else:
        min = list[0]
        for num in list:
            if num < min: min = num
        return min

def maximum(list):
    if len(list) == 0: return False
    elif len(list) == 1: return list[0]
    else:
        max = list[0]
        for num in list:
            if num > max: max = num
        return max
    
def ultimate_analyze(list):
    dict = {
        "Sum Total": sum_total(list),
        "Average": average(list),
        "Minimum": minimum(list),
        "Maximum": maximum(list),
        "Length": length(list)
    }
    return dict

def reverse_list(list):
    for i in range(len(list)):
        j = len(list) - i - 1
        if j > i:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
    return list

array = [-1,3,5,-5,2]

print(reverse_list(array))
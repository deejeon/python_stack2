def selection_sort(list):
    if len(list) == 1:
        return list
    for i in range(len(list) - 1):
        current_min = list[i]
        for j in range(i + 1, len(list)):
            if list[j] < current_min:
                current_min = list[j]
                swap_idx = j
        if current_min != list[i]:
            list[i], list[swap_idx] = list[swap_idx], list[i]
    return list

print(selection_sort([2,6,5,9,7,0]))


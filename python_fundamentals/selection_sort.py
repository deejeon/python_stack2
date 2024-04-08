def selection_sort(list):
    if len(list) == 1:
        return list
    for i in range(len(list) - 1):
        current_min = list[i]
        for j in range(i + 1, len(list)):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
                swap_idx = j


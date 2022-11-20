def insertion_sort(random_list, n):
    if n == 0:
        return "No list to sort"
    if n == 1:
        return str(random_list)
    for i in range(1, n):
        key = random_list[i]
        j = i - 1
        while j >= 0 and random_list[j] < key:
            random_list[j+1] = random_list[j]
            j -= 1
        random_list[j + 1] = key

    return str(random_list)
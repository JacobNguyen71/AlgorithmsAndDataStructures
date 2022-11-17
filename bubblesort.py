def bubble_sort(random_list, n):
    if n == 0:
        return "No list to sort"
    if n == 1:
        return str(random_list)
    for k in range(n):
        for i in range(n - 1):
            j = i + 1
            if random_list[i] > random_list[j]:
                random_list[j], random_list[i] = random_list[i], random_list[j]

    return str(random_list)
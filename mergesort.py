def merge_sort(random_list, n):
    if n > 1:
        middle = n//2
        leftArray = random_list[:middle]
        rightArray = random_list[middle:]
        leftLength = len(leftArray)
        rightLength = len(rightArray)
        merge_sort(leftArray, leftLength)
        merge_sort(rightArray, rightLength)

        i = j = k = 0
        while i < leftLength and j < rightLength:
            if leftArray[i] <= rightArray[j]:
                random_list[k] = leftArray[i]
                i += 1
            else:
                random_list[k] = rightArray[j]
                j += 1
            k += 1

        while i < leftLength:
            random_list[k] = leftArray[i]
            i += 1
            k += 1

        while j < leftLength:
            random_list[k] = rightArray[j]
            j += 1
            k += 1


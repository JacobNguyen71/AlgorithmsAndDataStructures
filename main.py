from createRandomList import generate_list
from bubblesort import bubble_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
import time

def main():
    lower_bound, upper_bound = int(input("Please enter a lower bound: ")), \
                                  int(input("Please enter a upper bound: "))
    random_list = generate_list(lower_bound, upper_bound)

    start_time = time.time()
    print(random_list)
    bubble_sort(random_list, len(random_list))
    print("bubble sort: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    insertion_sort(random_list, len(random_list))
    print("insertion sort: --- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(random_list)
    merge_sort(random_list, len(random_list))
    print("merge sort: --- %s seconds ---" % (time.time() - start_time))

main()

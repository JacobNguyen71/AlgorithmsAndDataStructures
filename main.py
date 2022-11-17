from createRandomList import generate_list
from bubblesort import bubble_sort
import time

def main():
    lower_bound, upper_bound = int(input("Please enter a lower bound: ")), \
                                  int(input("Please enter a upper bound: "))
    random_list = generate_list(lower_bound, upper_bound)

    start_time = time.time()
    print(random_list)
    print(bubble_sort(random_list, len(random_list)))
    print("--- %s seconds ---" % (time.time() - start_time))
main()

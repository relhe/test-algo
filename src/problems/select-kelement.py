import heapq
import time
import secrets


def select_kth_element_group_five(number_list: list, kth_element: int)->int:
    # divide the list into groups of five
    # sort each group
    # find the median of each group
    # find the median of medians
    # partition the list around median of medians
    # find the position of the median of medians in the list
    # if the position is equal to k, return the element
    # if the position is greater than k, repeat the process on the left sublist
    # if the position is less than k, repeat the process on the right sublist
    list_of_groups = []
    import math

    for i in range(0, len(number_list), 5):
        list_of_groups.append(number_list[i:i+5])
    for group in list_of_groups:
        group = sorted(group)
    median_list = []
    for group in list_of_groups:
        median_list.append(group[math.ceil(len(group)/2)-1])
    median_of_medians = median_list[math.ceil(len(median_list)/2)-1]
    left = []
    right = []
    for number in number_list:
        if number < median_of_medians:
            left.append(number)
        else:
            right.append(number)
    if len(left) == kth_element - 1:
        return median_of_medians
    elif len(left) > kth_element - 1:
        return select_kth_element_group_five(left, kth_element)
    else:
        return select_kth_element_group_five(right, kth_element - len(left) - 1)

# select kth element from an array
def select_kth_element(number_list: list, kth_element: int)->int:
    """
    This function takes a list of numbers and returns the kth smallest element using quick select algorithm.
    """
    if len(number_list) == 1:
        return number_list[0]
    else:
        pivot = number_list.pop()
        left = []
        right = []
        for number in number_list:
            if number < pivot:
                left.append(number)
            else:
                right.append(number)
        if len(left) == kth_element - 1:
            return pivot
        elif len(left) > kth_element - 1:
            return select_kth_element(left, kth_element)
        else:
            return select_kth_element(right, kth_element - len(left) - 1)

# time complexity
# best case O(n)
# worst case O(n^2)
# average case O(n)
# space complexity O(n)

# implementation using a heap
def select_kth_element_heap(number_list: list, kth_element: int)->int:
    """
    This function takes a list of numbers and returns the kth smallest element using heap data structure.
    """
    heap = []
    for number in number_list:
        heapq.heappush(heap, number)
    for _ in range(kth_element - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# time complexity
# worst case O(n log n)
# average case O(n)
# best case O(n)
# space complexity O(1) in place-sorting

# implementation using brute force for sorting
def select_kth_element_brute_force(number_list: list, kth_element: int)->int:
    """
    This function takes a list of numbers and returns the kth smallest element using brute force sorting.
    """
    # qs.quicksort_inplace(number_list)
    num = sorted(number_list)
    return num[kth_element - 1]

if __name__ == "__main__":
    # generate a list of 1500 number with secrets module
    number_list = [secrets.randbelow(23500000000) for _ in range(1000000)]
    kth_element = 10
    # measure the time taken by the function execution
    print(sorted(number_list))
    print("\n")
    start_time = time.time()
    print("kth smallest element using quick select: ", select_kth_element(number_list, kth_element))
    print("Time taken by quick select: ", time.time() - start_time)
    start_time = time.time()
    print("kth smallest element using heap: ", select_kth_element_heap(number_list, kth_element))
    print("Time taken by select using heap: ", time.time() - start_time)
    start_time = time.time()
    print("kth smallest element using brute force: ", select_kth_element_brute_force(number_list, kth_element))
    print("Time taken by select with brute force sorting: ", time.time() - start_time)
    start_time = time.time()
    print("kth smallest element using group of five: ", select_kth_element_group_five(number_list, kth_element))
    print("Time taken by select with group of five: ", time.time() - start_time)

import random
# Quicksort algorithm implementation in Python.

# quicksort without using extra space
def quicksort_inplace(number_list:list, low:int, high:int)->None:
    """Sorts a list of numbers using the quick sort algorithm.
    Args:
        number_list (list): List of numbers to sort.
        low (int): Starting index of the list.
        high (int): Ending index of the list.
    """
    if low < high:
        pivot = partition(number_list, low, high)
        quicksort_inplace(number_list, low, pivot - 1)
        quicksort_inplace(number_list, pivot + 1, high)

def partition(number_list:list, low:int, high:int)->int:
    """Partitions the list around a pivot.
    Args:
        number_list (list): List of numbers to sort.
        low (int): Starting index of the list.
        high (int): Ending index of the list.
    Returns:
        int: The index of the pivot.
    """
    pivot = number_list[high]
    i = low - 1
    for j in range(low, high):
        if number_list[j] < pivot:
            i += 1
            number_list[i], number_list[j] = number_list[j], number_list[i]
    number_list[i + 1], number_list[high] = number_list[high], number_list[i + 1]
    return i + 1

def quick_sort(number_list:list)->list:
    """Sorts a list of numbers using the quick sort algorithm.
    Args:
        number_list (list): List of numbers to sort.
    Returns:
        list: Sorted list of numbers.
    """
    if len(number_list) <= 1:  # threshold of 1 but can be more efficient with a threshold to be determined experimentally
        return number_list
    else:
        pivot = number_list.pop()
        left = []
        right = []
        for number in number_list:
            if number < pivot:
                left.append(number) # partitioning
            else:
                right.append(number)
        return quick_sort(left) + [pivot] + quick_sort(right) # recombine

# best case O(n log n)
# worst case O(n^2)
# average case O(n log n)
# space complexity O(n)

if __name__ == "__main__":
    random_list = [random.randint(0, 100) for _ in range(20)]
    print("Unsorted list:")
    print(random_list)
    print("Sorted list:")
    print(quick_sort(random_list))
    print("quicksort inplace")
    print("Unsorted list:")
    print(random_list)
    quicksort_inplace(random_list, 0, len(random_list) - 1)
    print("Sorted list:")
    print(random_list)
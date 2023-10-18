# Quicksort algorithm implementation in Python.

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
    import random
    random_list = [random.randint(0, 100) for _ in range(20)]
    print("Unsorted list:")
    print(random_list)
    print("Sorted list:")
    print(quick_sort(random_list))
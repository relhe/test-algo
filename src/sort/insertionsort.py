
def insertion_sort(number_list:list)->list:
    """
    This function takes a list of numbers and returns an ascending sorted list using insertion sort algorithm.
    """
    for i in range(1, len(number_list)):
        key = number_list[i]
        j = i - 1
        while j >= 0 and key < number_list[j]:
            number_list[j + 1] = number_list[j]
            j -= 1
        number_list[j + 1] = key
    return number_list

if __name__ == "__main__":
    number_list = [int(i) for i in input("Enter the numbers to be sorted separated by space: ").split()]
    print("Sorted list: ", insertion_sort(number_list))
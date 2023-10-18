# Merge sort algorithm implementation

def merge_sort(number_list:list)->list:
    """
    Merge sort algorithm implementation
    :param number_list: list of numbers
    :return: sorted list of numbers
    """
    if len(number_list) <= 1:
        return number_list
    else:
        middle = len(number_list) // 2
        left = merge_sort(number_list[:middle])
        right = merge_sort(number_list[middle:])
        return merge(left, right)

def merge(left_number_list:list, right_number_list:list)->list:
    """
    Merge two sorted list into one sorted list
    :param left_number_list: sorted list of numbers
    :param right_number_list: sorted list of numbers
    :return: sorted list of numbers
    """
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left_number_list) and right_index < len(right_number_list):
        if left_number_list[left_index] < right_number_list[right_index]:
            result.append(left_number_list[left_index])
            left_index += 1
        else:
            result.append(right_number_list[right_index])
            right_index += 1
    if left_index < len(left_number_list):
        result.extend(left_number_list[left_index:])
    if right_index < len(right_number_list):
        result.extend(right_number_list[right_index:])
    return result

if __name__ == '__main__':
    print(merge_sort([1, 5, 3, 2, 4, 6, 7, 8, 9, 10]))
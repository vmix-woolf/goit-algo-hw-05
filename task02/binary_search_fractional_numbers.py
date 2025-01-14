def binary_search_fractional_numbers(array, value):
    """
    Implements binary search for the sorted array with fractional numbers
    :param array: sorted array with fractional numbers
    :param value: target value for searching
    :return: tuple (iterations, upper_bound)
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if array[mid] == value:
            return iterations, array[mid]  # exact match

        if array[mid] < value:
            left = mid + 1
        else:
            upper_bound = array[mid]  # update upper bound
            right = mid - 1

    # if target value is not found, return upper bound
    return iterations, upper_bound


if __name__ == '__main__':
    arr = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

    for i in [0.05, 0.2, 0.35, 0.45, 1.0]:
        result = binary_search_fractional_numbers(arr, i)
        print(f"Total iterations: {result[0]}, Upper bound: {result[1]}")

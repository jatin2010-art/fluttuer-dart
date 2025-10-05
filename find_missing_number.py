def find_missing_number(arr):
    n = len(arr) + 1  # Total numbers including the missing one
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    arr_sum = sum(arr)             # Sum of numbers in the list
    return total_sum - arr_sum

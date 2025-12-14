def reverse_array(arr: list) -> list:
    reversed_list = []
    for i in range(len(arr)-1,-1,-1):
        reversed_list.append(arr[i])

    # END OF YOUR CODE
    return reversed_list

# Example calls for testing
print(f"Input: [1, 2, 3], Output: {reverse_array([1, 2, 3])}")
print(f"Input: ['a', 'b'], Output: {reverse_array(['a', 'b'])}")
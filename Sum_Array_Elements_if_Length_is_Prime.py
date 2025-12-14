def sum_if_length_prime(arr: list[int]) -> int:
    n = len(arr)

    # Check if n is prime
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    # Compute result based on primality
    result = sum(arr) if is_prime else 0
    return result


# Example calls for testing
print(f"Input: [1, 2, 3], Output: {sum_if_length_prime([1, 2, 3])}")
print(f"Input: [10, 20, 30, 40], Output: {sum_if_length_prime([10, 20, 30, 40])}")

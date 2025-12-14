def increment_digits(digits: list[int]) -> list[int]:
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    # If all digits were 9 (e.g., 9,9 → 1,0,0)
    return [1] + digits


# Example calls for testing
print(f"Input: [1,2,3], Output: {increment_digits([1,2,3])}")
print(f"Input: [9,9], Output: {increment_digits([9,9])}")

def find_single_number(nums: list[int]) -> int:
    single_number = 0
    for num in nums:
        single_number ^= num 
    return single_number

print(f"Input: [2, 2, 1], Output: {find_single_number([2, 2, 1])}")
print(f"Input: [4, 1, 2, 1, 2], Output: {find_single_number([4, 1, 2, 1, 2])}")
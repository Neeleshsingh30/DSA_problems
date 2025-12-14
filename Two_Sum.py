def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    # Since the problem guarantees exactly one solution, we never reach here
    return []
print(two_sum([2, 7, 11, 15], 9))     
print(two_sum([3, 2, 4], 6))         
print(two_sum([3, 3], 6))            
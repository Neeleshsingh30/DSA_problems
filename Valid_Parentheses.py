def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            if not stack:
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return len(stack) == 0


print(f'Input: "()", Output: {is_valid("()")}')
print(f'Input: "()[]{{}}", Output: {is_valid("()[]{}")}')

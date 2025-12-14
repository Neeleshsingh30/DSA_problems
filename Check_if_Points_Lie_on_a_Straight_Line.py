def check_straight_line(coordinates: list[list[int]]) -> bool:

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    dx = x2 - x1
    dy = y2 - y1

    is_straight = True

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]

        # Cross multiplication to avoid division
        if (x - x1) * dy != (y - y1) * dx:
            is_straight = False
            break

    # END OF YOUR CODE
    return is_straight


# Example calls for testing
print(f"Input: [[1,1],[2,2],[3,3]], Output: {check_straight_line([[1,1],[2,2],[3,3]])}")
print(f"Input: [[1,1],[2,2],[3,4]], Output: {check_straight_line([[1,1],[2,2],[3,4]])}")

from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    MAX_COUNT =amount + 1 
    dp = [MAX_COUNT] * (amount + 1)

    dp[0] = 0
    for i in range(1, amount + 1 ):
        for coin in coins:
            if i>= coin:
                dp[i] = min(dp[i],dp[i-coin] + 1)
    # min(current_best,1 + min_coins_for_remaining_amount)
    # min_coins = -1

    # END OF YOUR CODE
    return dp[amount] if dp[amount] != MAX_COUNT else -1

print(f"Input: coins=[1, 2, 5], amount=11, Output: {coin_change([1, 2, 5], 11)}")
print(f"Input: coins=[2], amount=3, Output: {coin_change([2], 3)}")
def find_first_n_primes(n: int) -> list[int]:
    prime_numbers = []
    num = 2

    while len(prime_numbers) < n:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers.append(num)

        num += 1  # increment every time

    return prime_numbers


print(f"Input: n = 1, Output: {find_first_n_primes(1)}")
print(f"Input: n = 5, Output: {find_first_n_primes(5)}")

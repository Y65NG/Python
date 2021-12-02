def sieve(a, b):
    nums = [True] * (b - a + 1)
    for i in range(2, int(b ** 0.5)):
        for j in range(len(nums)):
            if j + a < 2: nums[j] = False
            elif nums[j] and (j + a) != i and (j + a) % i == 0:
                nums[j] = False
    primes = []
    for _ in range(len(nums)):
        if nums[_]: primes.append(_ + a) 
    return primes

print(sieve(-100, 100))
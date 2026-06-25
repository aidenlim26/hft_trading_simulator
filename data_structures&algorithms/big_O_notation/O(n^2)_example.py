def example2(nums):
    results = [1 for _ in range(len(nums))]     # n

    for i, num1 in enumerate(nums):             # n 
        for num2 in nums:                       # n
            if num1 == num2:
                continue

            results[i] *= num2

    return results

# n + n*3n
# O(n^2)
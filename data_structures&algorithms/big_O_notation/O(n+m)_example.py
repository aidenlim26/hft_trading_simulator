def example3(nums1,nums2):      # let nums1 = n, and nums2 = m
                                # multiple inputs needs multiple variables
    results = []                        # 1

    for num in nums1:                   # n
        results.append(num)             # 1

    for i, num in enumerate(nums2):     # m
        if i >= len(results):           # 1
            results.append(1)           # 1
        results[i] *= num               # 1

    return results                      # 1

# 1 + n + 3m + 1
# O(n + m)

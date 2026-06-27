def example4(nested_list):      # let nested_list = n, inner_list = m
    total = 0                           # 1

    for inner_list in nested_list:      # n
        for num in inner_list:          # m
            total += num                # 1

        for num in inner_list:          # m
            total += num                # 1
        
        for num in inner_list:          # m
            total += num                # 1

    return total                        # 1

# 1 + 1 + n(m+m+m)
# O(nm)


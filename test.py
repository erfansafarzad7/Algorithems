"""
Top one
    [1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 5, 5, 6] => [2, 3]
"""


def top(lst):
    values = {}
    result = []
    f_val = 0

    for i in lst:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue

    return f"most repeated items:{result} \n values: {values}"


print(top([1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 5, 5, 6]))

# -----------------------------------------------------------------


"""
Top one
    [1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 5, 5, 6] => [2, 3]
"""


# def top(lst):
#     values = {}
#     result = []
#     f_val = 0
#
#     for i in lst:
#         if i in values:
#             values[i] += 1
#         else:
#             values[i] = 1
#
#     f_val = max(values.values())
#
#     for i in values.keys():
#         if values[i] == f_val:
#             result.append(i)
#         else:
#             continue
#
#     return f"most repeated items:{result} \n values: {values}"
#
#
# print(top([1, 2, 3, 2, 3, 1, 2, 2, 3, 4, 5, 5, 6]))

# -----------------------------------------------------------------

# from string import ascii_letters

"""
Caesar Cipher
"""


# def encrypt(string: str, key: int):
#     alpha = ascii_letters
#     result = ''
#
#     for ch in string:
#         if ch not in alpha:
#             result += ch
#         else:
#             new_key = (alpha.index(ch) + key) % len(alpha)
#             result += alpha[new_key]
#
#     return result
#
#
# def decrypt(string: str, key: int):
#     key *= -1
#     return encrypt(string, key)
#
#
# def brute_force(string):
#     alpha = ascii_letters
#     key = 1
#     result = ''
#     brute_force_data = {}
#
#     while key <= len(alpha):
#         result = decrypt(string, key)
#         brute_force_data[key] = result
#         result = ''
#         key += 1
#     return brute_force_data
#
#
# print(encrypt('erfan', 7))
# print(decrypt('lymhu', 7))
# print(brute_force('lymhu'))

# -----------------------------------------------------------------

"""
Search Insert
    [1, 2, 5, 8, 10], 6 => 3
"""


# def search_insert(array, val):
#     low = 0
#     high = len(array) - 1
#     mid = high // 2
#
#     while low <= high:
#         if val > array[mid]:
#             mid += 1
#             low = mid
#         else:
#             mid -= 1
#             high = mid
#     return low
#
#
# print(search_insert([1, 2, 5, 8, 10], 6))

# -----------------------------------------------------------------

"""
Is Isomorphic
    foo, bar => False
    foo, bee => True
    paper, title => True
"""


def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dic = {}
    set_values = set()

    for i in range(len(s)):
        if s[i] not in dic:
            if t[i] in set_values:
                return False
            dic[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dic[s[i]] != t[i]:
                return False

    return True


print(is_isomorphic('paper', 'title'))

# -----------------------------------------------------------------

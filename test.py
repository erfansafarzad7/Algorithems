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


# def is_isomorphic(s, t):
#     if len(s) != len(t):
#         return False
#
#     dic = {}
#     set_values = set()
#
#     for i in range(len(s)):
#         if s[i] not in dic:
#             if t[i] in set_values:
#                 return False
#             dic[s[i]] = t[i]
#             set_values.add(t[i])
#         else:
#             if dic[s[i]] != t[i]:
#                 return False
#
#     return True
#
#
# print(is_isomorphic('paper', 'title'))

# -----------------------------------------------------------------

"""
a1z26
    erfan => [31, 44, 32, 27, 40]
"""


# def encode(text):
#     return [ord(elm) - 70 for elm in text]
#
#
# def decode(lst):
#     return "".join([chr(elm + 70)for elm in lst])
#
#
# print(encode('erfan'))
# print(decode([31, 44, 32, 27, 40]))

# -----------------------------------------------------------------

"""
Bead Sort
    [5, 1, 3, 9, 6, 3, 8, 2] => [1, 2, 3, 3, 5, 6, 8, 9]
"""


# def bead_sort(sequence):
#     if any(not isinstance(x, int) or x < 0 for x in sequence):
#         raise TypeError('sequence must be list of non-negative integers')
#
#     for _ in range(len(sequence)):
#
#         for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
#
#             if rod_upper > rod_lower:
#                 sequence[i] -= rod_upper - rod_lower
#                 sequence[i + 1] += rod_upper - rod_lower
#
#     return sequence
#
#
# print(bead_sort([5, 1, 3, 9, 6, 3, 8, 2]))

# -----------------------------------------------------------------

"""
ZigZag Iterator
    [1, 3, 5, 7, 9], [2, 4, 6, 8, 10] => 1 2 3 4 5 6 7 8 9 10
"""


# class ZigZag:
#     def __init__(self, l1, l2):
#         self.queue = [l1, l2]
#
#     def next(self):
#         v = self.queue.pop(0)
#         r = v.pop(0)
#         if v:
#             self.queue.append(v)
#         return r
#
#     def has_next(self):
#         if self.queue:
#             return True
#         return False
#
#
# z = ZigZag([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# while z.has_next():
#     print(z.next(), end=' ')

# -----------------------------------------------------------------

"""
Move Zeros
    [False, 1, 3, 2, 0, 4, 0, 'a'] => [False, 1, 3, 2, 4, 'a', 0, 0]
"""


# def move_zeros(seq):
#     result = []
#     zeros = 0
#     for i in seq:
#         if i == 0 and type(i) != bool:
#             zeros += 1
#         else:
#             result.append(i)
#
#     result.extend([0] * zeros)
#     return result
#
#
# print(move_zeros([False, 1, 3, 2, 0, 4, 0, 'a']))

# -----------------------------------------------------------------

"""
Remove Min
    [3, 6, 2, 5, 9, -1, 3] => [3, 6, 2, 5, 9, 3]
"""


def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:
        return stack

    m = stack[0]
    # m = stack.pop()
    # stack.append(m)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= m:
            m = val
        storage_stack.append(val)

    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != m:
            stack.append(val)

    return stack, m


print(remove_min([3, 6, 2, 5, 9, -1, 3]))

# -----------------------------------------------------------------

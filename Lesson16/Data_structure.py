lst = [(0, 1), (0, 9), (5, 7), (2, 4)]


def find_largest_sum(lst):
    sum_list = []
    for t in lst:
        sum = 0
        sum += t[0] + t[1]
        sum_list.append(sum)
    index = sum_list.index(max(sum_list))
    return lst[index]


def find_largets_sum_2(lst):
    if len(lst) == 0:
        return -1, -1
    max_sum = lst[0][0]+lst[0][1]
    max_index = 0
    for i in range(len(lst)):
        sum = lst[i][0] + lst[i][1]
        if sum >= max_sum:
            max_sum = sum
            max_index = i
    return lst[max_index]


# magic
print(max(lst, key=sum))


def find_second_largest_num(lst):
    if len(lst) == 0:
        return -1, -1
    max_second_num = lst[0][1]
    max_index = 0
    for i in range(len(lst)):
        if lst[i][1] >= max_second_num:
            max_second_num = lst[i][1]
            max_index = i
    return lst[max_index]

print(find_second_largest_num(lst))



"""print(find_largest_sum(lst))
print(find_second_largest_num(lst))"""


"""letters_to_numbers = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4
}


def letter_to_number(phrase):
    new_phrase = ""
    for char in phrase:
        new_phrase += letters_to_numbers[char]
    return new_phrase

phrase = ""
"""


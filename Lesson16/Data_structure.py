lst = [(0, 1), (0, 9), (5, 7), (2, 4)]


def find_largest_sum(lst):
    sum_list = []
    for t in lst:
        sum = 0
        sum += t[0] + t[1]
        sum_list.append(sum)
    index = sum_list.index(max(sum_list))
    return lst[index]


def find_second_largest_num(lst):
    second_num_list = []
    for t in lst:
        if t[0] >= t[1]:
            second_num_list.append(t[0])
        elif t[0] < t[1]:
            second_num_list.append(t[1])
    return max(second_num_list)


print(find_largest_sum(lst))
print(find_second_largest_num(lst))





letters_to_numbers = {
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


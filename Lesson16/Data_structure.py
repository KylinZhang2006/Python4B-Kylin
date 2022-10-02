# lst = [(0, 1), (0, 9), (5, 7), (2, 4)]
#
#
# def find_largest_sum(lst):
#     sum_list = []
#     for t in lst:
#         sum = 0
#         sum += t[0] + t[1]
#         sum_list.append(sum)
#     index = sum_list.index(max(sum_list))
#     return lst[index]
#
#
# def find_largets_sum_2(lst):
#     if len(lst) == 0:
#         return -1, -1
#     max_sum = lst[0][0]+lst[0][1]
#     max_index = 0
#     for i in range(len(lst)):
#         sum = lst[i][0] + lst[i][1]
#         if sum >= max_sum:
#             max_sum = sum
#             max_index = i
#     return lst[max_index]
#
#
# # magic
# #print(max(lst, key=sum))
#
#
# def find_second_largest_num(lst):
#     if len(lst) == 0:
#         return -1, -1
#     max_second_num = lst[0][1]
#     max_index = 0
#     for i in range(len(lst)):
#         if lst[i][1] >= max_second_num:
#             max_second_num = lst[i][1]
#             max_index = i
#     return lst[max_index]
#
# print(find_second_largest_num(lst))
#
#
# # magic
# def second_num(t):
#     return t[1]
#
#
# print(max(lst, key=second_num))
#
#
#
#
# # letter_to_number("afdegh") => 0f34gh

"""Homework"""

# Dictionary
letters_to_numbers = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4
}


# Method 1: With change to the original phrase


def letter_to_number_1(phrase):
    new_phrase = ""
    for char in phrase:
        if char in letters_to_numbers:
            new_phrase += str(letters_to_numbers[char])
        else:
            new_phrase += char
    return new_phrase


print(letter_to_number_1("afdegh"))

# Method 2: Without change to the origninal phrase


def letter_to_number_2(phrase):
    for i in range(len(phrase)):
        if phrase[i] in phrase:
            phrase[i] = str(letters_to_numbers[char])
    return phrase


print(letter_to_number_1("afdegh"))


passage = "Alpha and Beta went down a road and realized that their names are Greek alphabets"
passage2 = "It was unfortunate to hear that Alpha had Pneumonoultramicroscopicsilicovolcanoconiosis"


def longest_word(passage):
    splitted_passage = passage.split(" ")
    longest_word = ""
    for word in splitted_passage:
        if len(word) > len(longest_word):
            longest_word = word
    return word


print(longest_word(passage))
print(longest_word(passage2))








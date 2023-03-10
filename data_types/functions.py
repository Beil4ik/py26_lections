"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
"""
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


'Task 1'

# list_ = [1, 2, 3]
# list_2 = [5, 5, 5, 5, 5]

# def func(list_1):
#     a = list_1[0]
#     b = list_1[1]
#     c = list_1[2]
#     c = 4
#     list_new = [a, b, c]
#     return list_new

# print(func(list_))
# print(func(list_2))

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.  

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: 

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


'Task 2'

# def romanToInt(s: str) -> int:
#     dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     s = list(s)
#     new_list = []
#     for i in s:
#         num = dict_[i]
#         new_list.append(num)
#     list1 = new_list[::-1]

#     i = 0
#     last = list1[0]
#     for x in list1:
#         if x < last:
#             i -= x
#         else:
#             i += x
#         last = x
#     return i

# print(romanToInt('III'))
# print(romanToInt('LVIII'))
# print(romanToInt('MCMXCIV'))
# print(romanToInt('MMXCV'))

"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""
"""
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

"""
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
"""
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""


'Task 3'

# def compare_to_arrays(word1, word2):
#     from functools import reduce
#     oper = reduce(lambda x, y: (x + y), word1)
#     oper1 = reduce(lambda x, y: (x +y), word2)
#     if oper == oper1:
#         return True
#     else:
#         return False

# print(compare_to_arrays(['a', 'cb'], ['ab', 'c']))
# print(compare_to_arrays(["abc", "d", "defg"], ["abcddefg"]))

"""
Создайте функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно. Если пользователь задаст первое число больше чем второе, просто поменяйте их местами.
"""


'Task 4'

# def sum_range(start, end):
#     if start > end:
#         list_ = list(range(end, start+1))
#         sum_ = sum(list_)
#         return sum_
#     else:
#         list_ = list(range(start, end+1))
#         sum_ = sum(list_)
#         return sum_


# print(sum_range(6, 1))

"""
На входе имеем список строк разной длины.
Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
Длину итоговой строки определяем исходя из самой большой из них.
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
Расположение элементов начального списка не менять.
"""

"""
Input: ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
Output: ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']
"""


'Task 5'

# lst = ['a', 'aa', 'aaa', 'aaaa', 'aaaaaa']

# def all_eq(lst):
#     max_ = len(max(lst))
#     list_ = []
#     for i in lst:
#        if len(i) != max_:
#            n = max_ - len(i)
#            under = "_" * n
#            un = i + under
#            list_.append(un)

#     list_.append(max(lst))
#     return list_

# print(all_eq(lst))

"""
Дано предложение "Это короткое предложение", оно может быть перетасовано как "предложение3 короткое2 Это1" или "короткое2 предложение3 Это1".
Учитывая перетасованные предложения, содержащие не более 9 слов, восстановите и верните исходное предложение, удалив цифры в конце слов.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
"""


'Task 6'

# text = "is2 sentence4 This1 a3"

# def func(text):
#     list_ = text.split()
#     list_.sort(key = lambda x: x[-1])
#     new_string = ""
#     for i in list_:
#         new_string = new_string + i[:-1] + " "
#     return new_string.strip()
    

# print(func(text))
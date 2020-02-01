"""
2.  Given an array print all the numbers that are repeating in it and the number of times they are repeating.

Below is an example:

Input: [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
Output:
1 - 4
2 - 2
5 - 3
8 - 2
4 - 2

Note: The final order of output need not be the same as above. The number after the dash(-) is the repeating count
"""


def numbers_repeat(lst):
    count_num = ''
    for i in list(set(lst)):
        if 1 < lst.count(i):
            count_num += f"{str(i)} - {str(lst.count(i))} \n"
    return count_num.rstrip('\n')


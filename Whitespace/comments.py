# Given an array of size N-1 such that it only contains distinct
# integers in the range of 1 to N. Find the missing element.
# 10
# [6, 1, 2, 8, 3, 4, 7, 10, 5]
# output = 9
# 5
# sum([1,2,3,5]) = 11
# 1+2+3+4+5 = 15 15-11
# Block Comments

def MissingNumber(n, list1):
    """
    Finding a missing number from a list by having the expected amount of
    numbers.
    :param n: Expected number of elements
    :type n: Int
    :param list1: A list that has n-1 elements
    :type list1: list
    :return: The missing integer from list1
    """
    # Finding the sum of the total number of elements referred by n,
    # while the sum_of_list is the sum of all elements in the list.
    total = (n+1) * n//2
    sum_of_list = sum(list1)

    return total - sum_of_list

print(MissingNumber(10, [6, 1, 2, 8, 3, 4, 7, 10, 5]))


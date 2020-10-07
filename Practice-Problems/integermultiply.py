# -*- coding: utf-8 -*-
"""
Given an array of integers return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our
input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
"""
def productlist(lst):
    result=1
    for i in lst:
        result=result*i
    return result


def newlist(input_list):
    output_list=[]
    product = productlist(input_list)
    for i in input_list:
        output_list.append(product/i)
    return output_list


print newlist([1, 2, 3, 4, 5])
"""


def productlist(lst):
    output_lst=[]
    i=0
    while i <len(lst):
        result = 1
        value = lst[i]
        lst_compare=lst
        del lst[i]
        for nuumber in lst:
            result=result*nuumber
        output_lst.append(result)
        lst_compare.insert(i, value)
        i+=1
    return output_lst


print (productlist([1, 2, 3, 4, 5]))
print productlist([3, 2, 1])
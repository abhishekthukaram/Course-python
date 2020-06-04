"""
Merge two lists in ascending order
"""


def merge_lists(my_list, alices_list):
    merged_list = len(my_list) + len(alices_list)
    output_list = [None] * merged_list
    i , j , k = 0,0 ,0
    while k < len(output_list):
        if i<len(my_list) and (j >= len(alices_list) or my_list[i] < alices_list[j]):
            output_list[k] = my_list[i]
            i+=1
        else:
            output_list[k] = alices_list[j]
            j+=1
        k+=1
    return output_list

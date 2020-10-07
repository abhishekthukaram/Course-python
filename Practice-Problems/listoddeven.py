"""
Create a function that goes through the list, incrementing (+1) for each odd element and
decrementing (-1) for each even number.
"""

def transform(lst):
    for i in range(len(lst)):
        if lst[i]&1:
            lst[i]-=1
        else:
            lst[i]+=1
    return lst
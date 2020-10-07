def exists_higher(lst, n):
    if len(lst)==0:
        return False
    else:
        output_max = max(lst)
        if n <=output_max:
            return True
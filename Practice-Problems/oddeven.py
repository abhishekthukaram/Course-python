def check_all_even(lst):
    return all(x % 2 == 0 for x in lst)

def hash_plus_count(txt):
    hash_count=0
    plus_count=0
    for i in txt:
        if i =="#":
            hash_count+=1
        else:
            plus_count+=1
    return [hash_count, plus_count]
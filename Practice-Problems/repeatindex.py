def double_char(txt):
    n = 2
    result = "".join([char*n for char in txt])
    return result


print (double_char("Hello"))
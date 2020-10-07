def mapping(string_in):
    result = {}
    for character in string_in:
        if character in result:
            result[character]+=1
        else:
            result[character]=1
    return result

def makeAnagram(a, b):
    count = 0
    dict_a = mapping(a)
    dict_b = mapping(b)
    for key in dict_a.keys():
        if key not in dict_b.keys():
            count+=dict_a[key]
        else:
            count+=max(0, abs(dict_a[key]-dict_b[key]))
    for keys_b in dict_b.keys():
        if keys_b not in dict_a.keys():
            count+=dict_b[keys_b]
        else:
            count+=max(0, abs(dict_b[keys_b]-dict_a[keys_b]))
    return count

print makeAnagram("abcd", "abba")
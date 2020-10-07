def repeatedString(s, n):
    count =0
    new = s*n
    print(new)
    for i in range(n):
        #print new[i]
        if str(new[i]) == 'a':
            count+=1
    return count


print repeatedString('aba', 10)
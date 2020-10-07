def return_str(s):
    odd = ""
    even = ""
    for i in range(len(s)):
        if i%2==0:
            even+=s[i]
        else:
            odd+=s[i]
    return (even + " "+ odd)


print return_str("Hacker")

"""
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False

def checkbrackets(brackets):
    count = 0
    open_list = ['{','(','[']
    close_list = ['}',')', ']']
    for i in brackets:
        if i in open_list:
            count+=1
        elif i in close_list:
            count -=1
    print count
    if count == 0:
        return True
    else:
        return False

"""


def checkbrackets(brackets):
    count = []
    brac_dict = {'{':'}','(':')','[':']'}
    for i in brackets:
        if i == '(' or i == '{' or i == '[':
            count.append(i)
            print(count)
        elif i == ')' or i == '}' or i == ']':
            if len(count) == 0:
                return False
            opened = count.pop()
            if brac_dict[opened] != i:
                return False
    if len(count) == 0:
        return True
    return False


print(checkbrackets("{ [ ] ( ) }"))
print (checkbrackets("{ [ ( ] ) }"))
print(checkbrackets("{ [ }"))




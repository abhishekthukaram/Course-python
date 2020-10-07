def replacenth(txt, nth , old_char, new_char):
    count = 0
    if nth<= 0 or nth >len(txt):
        return txt
    for character_index in range(len(txt)):
        if txt[character_index] == old_char:
            count += 1
        if count == nth:
            txt = txt[0:character_index] + new_char + txt[character_index+1:]
            count = 0
    return txt


print(replacenth("abababa", 3, "a", "Z"))
print (replacenth("Vader said: No, I am your father!", 2, "a", "o"))
print(replacenth("A glittering gem is not enough.", 0, "o", "-"))



def isAlienSorted(words, order):
    order_index = {c: i for i, c in enumerate(order)}

    for i in xrange(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        print word1
        print word2

isAlienSorted()

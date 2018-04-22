def most_repeated_letters(word_1):

    x= {}

    for letter in word_1:      
        if not x.get(letter):
            x[letter] = 0
        x[letter] = x.get(letter) + 1

    ret = {}

    for k,v in x.iteritems():
        if x[k] == max(x.values()):
            ret[k] = v

    return ret

most_repeated_letters('jackaby')

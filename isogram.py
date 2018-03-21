def is_isogram(word):
    if type(word)!=str:
    raise typeerror("argument should be a string")
    elif word=="":
        return(word,false)
    else:
        word=word.lower()
        for char in word:
            if word.count(char)>1:
            return(word,false)
        else:
            return(word,true)

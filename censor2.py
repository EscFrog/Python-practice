def censor(text, word):
    lst = text.split()
    for i in lst:
        if word in lst:
            loc = lst.index(word)
            lst.remove(word)
            lst.insert(loc, "*" * len(word))
    new_text = " ".join(lst)
    return new_text

print(censor("this hack is wack hack", "hack"))
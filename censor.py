def censor(text, word):
    lst = text.split()
    new_lst = []
    for element in lst:
        if element == word:
            new_lst.append("*" * len(element))
        else:
            new_lst.append(element)
    new_text = " ".join(new_lst)
    return new_text

print(censor("this hack is hack", "hack"))
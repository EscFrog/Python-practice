def anti_vowel(text):
    vowel = "aeiouAEIOU"
    new_word = ""
    for letter in text:
        if letter not in vowel:
            new_word += letter
    return new_word

print(anti_vowel("sorry"))
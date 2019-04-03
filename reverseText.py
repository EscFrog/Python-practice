def reverse(text):
    reverse_text = ""
    i = 0
    while i < len(text):
        reverse_text += text[len(text) - 1 - i]
        i += 1
    return reverse_text

print(reverse("I am super man"))

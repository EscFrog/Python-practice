# 인사하자
print ('Welcome to PygLatin translator!')

# 접미사 설정
pyg = 'ay'

# 입력을 받자
original = raw_input('Enter a word:')

# 글자수가 0개 이상인지, 그리고 알파펫인지 검사하자
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    # 모음인지 자음인지 확인 (vowel or consonant)
    # 모음이면 뒤에 접미사만 붙이자
    if first in 'aeiou':
        new_word = word + pyg
        print (new_word)
    # 자음이면 첫글자를 맨뒤로 보내고 접미사를 붙이자
    else:
        new_word = word[1:] + word[0] + pyg
        print (new_word)
# 글자수가 0개 이상인데, 알파벳이 아니라면
elif len(original) > 0 and not original.isalpha():
    print ('oops, it is not a word')
# 글자수가 0개 이하라면
else:
    print ('The input is empty. Please enter \'a word\' and try again')

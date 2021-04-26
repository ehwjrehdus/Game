import random 

print('영어 단어 번역 게임')
print('영어 단어를 번역하는 게임 입니다.')

dictionary = {
    'lion': '사자', 
    'apple': '사과',
    'airplane': '비행기',
    'zoo': '동물원',
    'sun': '태양'
}

keys = list(dictionary.keys())
random.shuffle(keys)

for english in keys:
    korean = dictionary[english]

    guess = input('{} 영어 단어를 번역하세요: '.format(english))

    if guess == korean: 
        print('영어 단어의 번역이 맞습니다.') 
    else: 
        print('영어 단어의 번역이 틀립니다.')
import random 

print('반다이 남코 에서 만든 슈팅 게임 입니다' )

print('갤러그 캐릭터 이름 맟추기 게임')

print('내용을 읽고 해당 캐릭터 이름을 맞추는 게임 입니다.')



dictionary = {
    '벌의 형태를 하고 있다?' : '자코', 
    '나비나 나방의 형태를 하고 있다?': '고에이',
    '2발을 맞춰야 이길수 있는 캐릭터는?': '보스 갤러가',
    '전갈모양을 한 캐릭터는?': '사소리',
    '가오리 같은 모습을 가진 캐릭터는?': '미도리',
    '고속으로 부딪혀 오는 강적은?' :  '갤럭시아',
    '잠자리 형태를 지닌 캐릭터는?' :  '톤보',
    '단풍잎 처럼생긴 캐릭터는?' : '모미지',
    '스타 트렉의 모티브가 주된 캐릭터는?' : '엔터프라이즈'
}

keys = list(dictionary.keys())
random.shuffle(keys)

for Galaga in keys:
    Gal = dictionary[Galaga]

    guess = input('{}: '.format(Galaga))

    if guess == Gal: 
        print('정답입니다!') 
    else: 
        print('땡 틀렸습니다!')

        print('게임 종료')    
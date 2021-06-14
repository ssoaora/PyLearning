"""
question_list = ['최근에 가장 떠오르는 프로그래밍 언어', '작업을 수행하는 문장들의 집합에 이름을 붙인것']
question = random.choice(question_list)
"""

problems = {'파이썬': '최근에 가장 떠오르는 프로그래밍 언어',
            '변수': '데이터를 저장하는 메모리 공간',
            '함수': '작업을 수행하는 문장들의 집합에 이름을 붙인것',
            '리스트': '서로 관련이 없는 항목들의 모임'}

for word in problems.keys():
    print('다음은 어떤 단어에 대한 설명일까요?')
    print(problems[word])
    print('(1)파이썬 (2)함수 (3)리스트 (4)변수')
    answer = input('정답을 적으시오: ')
    if answer == word:
        print('정답입니다! \n')
    else:
        print('틀렸습니다. 다시 생각해보세요. \n')
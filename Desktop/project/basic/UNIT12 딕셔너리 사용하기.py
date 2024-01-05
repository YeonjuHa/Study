# 딕셔너리 만들기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)

# 키 이름이 중복되면?
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
lux

# 딕셔너리 키의 자료형
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
x

x = {[10, 20]: 100}
x = {{'a': 10}: 100}


# 빈 딕셔너리 만들기
x = {}
x

y = dict()
y

# dict로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux1

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
lux2

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
lux4


# 딕셔너리의 키에 접근하고 값 할당하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
lux['armor']


# 딕셔너리의 키에 값 할당하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037
lux['mana'] = 1184
lux

# 새로운 키-값 쌍 할당
lux['mana_regen'] = 3.28
print(lux)
# 없는 키 출력
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['attack_speed']


# 딕셔너리에 키가 있는지 확인하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'health' in lux
'attack_speed' in lux

'attack_speed' not in lux
'health' not in lux


# 딕셔너리의 키 개수 구하기
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
len(lux)
len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})




pokemon = list(input('포켓몬이 얼마나 있습니까?\n'))
pokemonNum = int(len(pokemon))
pokemonList = []

print('초기 리스트: %s' %pokemon)
print('초기 리스트 인덱스 수: %d' %pokemonNum)

def change(before, n, after):
  for i in range(1, n):
    for j in range(n):
      if j == i:
        after.append(before[i])
        # print(j)
        i += 3
    break
  return after

pokemons = change(pokemon, pokemonNum, pokemonList)
print(pokemons)
can_getNum = int(len(pokemons)/2)
print('가질 수 있는 포켓몬 수: %d' %can_getNum)

# from itertools import combinations
# numList = list(combinations(pokemons, can_getNum)) # 초기 리스트 크기가 2일 때 예외처리
# print(numList)

num_count = 0
new_list = []
old_list = []

# while num_count < can_getNum:
#   for ch in pokemons:
#     if ch not in new_list:
#       new_list.append(ch)
#       num_count += 1
#       print(num_count)
#     else:
#       old_list.append(ch)
#   break

for ch in pokemons:
  if ch not in new_list:
    new_list.append(ch)
  else:
    old_list.append(ch)

# for i in range(can_getNum):
#   for ch in pokemons:
#     if ch not in new_list:
#       new_list.append(ch)
#       i += 1
#       print(i)

# for ch in pokemons:
#   if ch not in new_list:
#     new_list.append(ch)

print(new_list)
print(old_list)
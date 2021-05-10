def solution(nums):
    answer = 0
    pokemonNum = int(len(nums))
    pokemonList = []

    def change(before, n, after):
        for i in range(1, n):
            for j in range(n):
                if j == i:
                    after.append(before[i])
                    i += 3
            break
        return after

    pokemons = change(nums, pokemonNum, pokemonList)
    can_getNum = int(len(pokemons) / 2)

    new_list = []
    old_list = []

    for ch in pokemons:
        if ch not in new_list:
            new_list.append(ch)
        else:
            old_list.append(ch)

    final = int(len(new_list))

    if final > can_getNum:
            answer = can_getNum
    elif final < can_getNum:
            answer = final
    else:
            answer = can_getNum

    return answer

try:
    pokemon = list(input(''))
    print(solution(pokemon))
except EOFError:
    print('error')
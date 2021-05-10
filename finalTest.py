def delete(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back

def solution(participant, completion):
    answer = ''
    pp_list = []
    ct_list = []

    for i in range(len(participant)):
        if participant[i] == '[' or ']' or '"':
            delete(participant,i)
            return participant
            break
        print(participant)

    # for i in range(len(participant)):
    #     for j in range(len(completion)):

    return answer

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))

def solution(survey, choices):
    answer = ''

    score = dict()
    score['R'] = 0
    score['T'] = 0
    score['C'] = 0
    score['F'] = 0
    score['J'] = 0
    score['M'] = 0
    score['A'] = 0
    score['N'] = 0

    qs = [('T', 'R'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += (4 - choices[i])
        elif choices[i] > 4:
            score[survey[i][1]] += (choices[i] - 4)
    for q in qs:
        if score[q[0]] >= score[q[1]]:
            answer += q[0]
        else:
            answer += q[1]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["AN", "CF", "MJ", "RT", "NA"], [4, 4, 4, 4, 4]))
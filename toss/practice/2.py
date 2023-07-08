def isBefore(today, param):
    t_year, t_month, t_day = map(int, today.split("."))
    p_year, p_month, p_day = map(int, param.split("."))

    if t_year < p_year:
        return True
    elif t_year > p_year:
        return False
    else:
        if t_month < p_month:
            return True
        elif t_month > p_month:
            return False
        else:
            if t_day < p_day:
                return True
            else:
                return False


def solution(today, terms, privacies):
    answer = []

    tps = dict()
    for term in terms:
        alpha, month = term.split()
        tps[alpha] = int(month)

    prs = list()
    for privacy in privacies:
        date, alpha = privacy.split()
        year, month, day = map(int, date.split("."))

        year = int(year) + tps[alpha] // 12
        month = int(month) + tps[alpha] % 12
        if month > 12:
            year += month // 12
            month += month % 12
        prs.append(str(year) + "." + str(month) + "." + str(day))

    for i in range(len(prs)):
        if not isBefore(today, prs[i]):
            answer.append(i + 1)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.12.17", ["A 12"], ["2010.01.01 A", "2019.12.17 A"]))
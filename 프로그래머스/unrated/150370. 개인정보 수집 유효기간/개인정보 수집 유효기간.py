def solution(today, terms, privacies):
    answer = []
    timeDict = dict()
    year, month, day = int(today[:4]), int(today[5:7]), int(today[8:])
    
    for term in terms:
        case = term[0]
        timeDict[case] = int(term[2:])
    
    for idx, privacy in enumerate(privacies):
        date, case = privacy.split(' ')
        pYear, pMonth, pDay = int(date[:4]), int(date[5:7]), int(date[8:])
        pMonth += timeDict[case]
        
        while pMonth > 12:
            pMonth -= 12
            pYear += 1
        
        if pYear > year:
            continue
        elif pYear == year:
            if pMonth > month:
                continue
            elif pMonth == month:
                if pDay > day:
                    continue
        
        answer.append(idx + 1)

    return answer
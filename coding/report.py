def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {id : 0 for id in id_list}
    
    for i in set(report):
        reports[i.split()[1]] += 1
    for i in set(report):
        if reports[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
    
    print(answer)
    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    solution(id_list, report, k)
    
    
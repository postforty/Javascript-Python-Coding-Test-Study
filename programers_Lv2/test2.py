
def solution(id_list, report, k):
    answer = []
    new_list = []
    result_list = []
    report_dict = {}
    for i in id_list:
        report_dict[i.split(' ')[0]]=0
    for i in id_list:
        if new_list.count(i) >= 2:
            result_list.append(i)
    for i in report:
        print(i.split(' ')[1])
        print(result_list)
        if i.split(' ')[1] in result_list:
            report_dict[i.split(' ')[1]] += 1
    print(report_dict)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
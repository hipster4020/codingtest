# my code
def solution(lottos, win_nums):
    answer = [0] * 2
    dic_win = {v : k+1 for k, v in enumerate(range(6, 0, -1))}
    max = 0
    min = 0

    for lotto in lottos:
        if lotto in win_nums:
            min += 1
        if lotto == 0:
            max += 1

    answer[1] = dic_win[1] if min == 0 else dic_win[min]
    answer[0] = dic_win[1] if max == 0 else dic_win[min + max]
    if max == 0 and min != 0:
        answer[0] = dic_win[min]

    return answer

# best code
# def solution(lottos, win_nums):
#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     answer = 0
#     for x in win_nums:
#         if x in lottos:
#             answer += 1
#     print([rank[cnt_0 + answer],rank[answer]])
#     return rank[cnt_0 + answer],rank[answer]

if __name__ == '__main__':
    #lottos = [44, 2, 3, 4, 32, 25]
    #win_nums = [31, 10, 45, 1, 6, 19]
    #lottos = [0, 0, 0, 0, 0, 0]
    #win_nums = [38, 19, 20, 40, 15, 25]
    lottos = [45, 5, 35, 20, 3, 9]
    win_nums = [20, 9, 3, 45, 4, 35]
    solution(lottos, win_nums)

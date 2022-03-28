def solution(rows, columns, swipes):
    # 배열 만들기
    list = []
    temp = []
    for i in range(1, rows * columns+1):
        temp.append(i)
        if i % columns == 0:
            list.append(temp)
            temp = []
    
    # 합 구하기
    answer = []
    # 1 아래, 3 오른쪽, 4 왼쪽, 2 위
    for i in range(len(swipes)):
        if swipes[i][0] == 1:
            # 내려가다보면 시작점과 끝점의 차이만큼 만 더해줌
            diff = (swipes[i][4]) - (swipes[i][2])
            sum_temp = []
            
            for dif in range(diff+1):
                sum_temp.append(list[swipes[i][3]-1][swipes[i][4]-1-dif])
            answer.append(sum(sum_temp))
        if swipes[i][0] == 3:
            diff = (swipes[i][3]) - (swipes[i][1])
            sum_temp = []
            for dif in range(diff+1):
                print(dif)
                sum_temp.append(list[swipes[i][3]-1][swipes[i][4]-1-dif])
            print(sum_temp)
            
    print(answer)
    return answer

if __name__ == "__main__":
    rows = 4
    columns = 3
    
    # 1 아래, 3 오른쪽, 4 왼쪽, 2 위
    swipes = [
                [1,1,2,4,3],
                [3,2,1,2,3],
                [4,1,1,4,3],
                [2,2,1,3,3]
                ]
    solution(rows, columns, swipes)
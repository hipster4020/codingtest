# my code  failed
# def solution(s):
#     temp = ""
    
#     for i in range(len(s)-1):
#         count = 1
#         if s[i] == s[i+1]:
#             count += 1
            
#         temp+= count

#     print(temp)
#     answer = len(temp)
#     return answer

# different code
def solution(s):
    answer = 10000
    for n in range(1, len(s)//2+2):
        res = ""
        count = 1
        temp = s[:n]
        
        for i in range(n, len(s)+n, n):
            if temp == s[i:i+n]:
                count += 1
            else:
                if count == 1:
                    res += temp
                else:
                    res += str(count) + temp
                temp = s[i:i+n]
                count = 1
    print(res)
    answer = min(answer, len(res))
    print(answer)
    return answer
if __name__ == "__main__":
    s = "aabbaccc"
    solution(s)
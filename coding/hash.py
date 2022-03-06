from collections import Counter

def solution(participant, completion):
    print(Counter(participant))
    print(Counter(completion))
    result = Counter(participant) - Counter(completion)
    print(list(result.keys()))
    return list(result.keys())[0]
    
if __name__ == "__main__":
    participant1 = ["leo", "kiki", "eden"]
    participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"] 
    participant3 = ["mislav", "stanko", "mislav", "ana"]
    completion1 = ["eden", "kiki"]
    completion2 = ["josipa", "filipa", "marina", "nikola"]
    completion3 = ["stanko", "ana", "mislav"]
    
    solution(participant1, completion1)
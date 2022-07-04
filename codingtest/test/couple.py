from re import I


def main(rounds):
    answer = -1
    success = []
    choice = []
    for i in rounds:
        choice.append("a" + i[0] + i[0] + "a")
        choice.append("b" + i[1] + i[1] + "b")
        choice.append("c" + i[2] + i[2] + "c")
        choice.append("d" + i[3] + i[3] + "d")
        
    for c in choice:
        temp = c[2:]+c[:2]
        if c[0] == c[1]:
            print("1")
            answer += 1
            pass
        elif c in success:
            print(c)
            print(success)
            answer += 1
            pass
        elif temp in choice:
            success.append(c)
    print(answer) 
    print(f"success : {success}") 

    
if __name__ == "__main__":
    rounds = [["b", "a", "a", "d"], ["b", "c", "a", "c"], ["b", "a", "d", "c"]]
    main(rounds)
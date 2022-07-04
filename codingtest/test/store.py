def main(beds, tables, cost):
    answer = 0
    room = []
    for bed in beds:
        room.append(bed[0])
        room.append(bed[1])
    for k, v in enumerate(tables):
        if room[k] < v[0]:
            room.append(v[0])
        if room[k+1] < v[1]:
            print(room[k+1])
            print(v[1])
            room[k+1] = v[1]

    
    print(room)
    
if __name__ == "__main__":
    beds = [[2, 3, 40000], [2, 5, 20000]]
    tables = [[1, 1, 30000]]
    cost = 10
    main(beds, tables, cost)
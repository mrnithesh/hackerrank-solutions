if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    sorted_scores=sorted(set(score for name, score in records))
    second_lowest=sorted_scores[1]
    result=[name for name, score in records if score==second_lowest]
    result.sort()
    for i in result:
        print (i)

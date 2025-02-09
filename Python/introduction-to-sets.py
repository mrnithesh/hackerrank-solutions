def average(array):
    distinct=set(array)
    distinct_sum=0
    for i in distinct:
        distinct_sum+=i
    average=distinct_sum/len(distinct)
    return average
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
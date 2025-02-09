if __name__=="__main__":
    m=int(input())
    set_a=set()
    set_b=set()
    set_a.update(list(map(int,input().split())))
        
    n=int(input())
    set_b.update(list(map(int,input().split())))
    result=sorted(set_a.symmetric_difference(set_b))
    for i in result:
        print(i)
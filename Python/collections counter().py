from collections import Counter
if __name__=="__main__":
    N=int(input())
    a=list(map(int,input().split()))
    inventory=Counter(a)
    total_customers=int(input())
    total_sales=0
    for i in range(total_customers):
        size, amount=map(int,input().split())
        if inventory[size]!=0:
            total_sales+=amount
            inventory[size]-=1
    print(total_sales)
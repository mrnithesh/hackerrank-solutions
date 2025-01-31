if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner=max(arr)
    newarr=[score for score in arr if score!=winner]
    print(max(newarr))

if __name__=="__main__":
    N=int(input())
    words={}
    for _ in range(N):
        word=input()
        words[word]=words.get(word,0)+1
    print(len(words))
    print(*words.values())
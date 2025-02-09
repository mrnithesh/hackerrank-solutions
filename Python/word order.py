from collections import Counter
if __name__=="__main__":
    """
    #dictionary key:value based approach

    N=int(input())
    words={}
    for _ in range(N):
        word=input()
        words[word]=words.get(word,0)+1
    print(len(words))
    print(*words.values())
    
    
    """
    #counter based approach
    
    N=int(input())
    words=[]
    for _ in range(N):
        words.append(input())
    count=Counter(words)
    print(len(count))
    print(*count.values())
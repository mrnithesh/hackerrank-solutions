def minion_game(string):
    stuart=0
    kevin=0
    vowels=['A','E','I','O','U']
    length=len(string)
    for i in range(len(string)):
        if (string[i] in vowels):
            kevin+=length-i
        else :
            stuart+=length-i
            
    if (stuart>kevin):
        print(f"Stuart {stuart}")
    elif (kevin>stuart):
        print(f"Kevin {kevin}")
    elif (kevin==stuart):
        print("Draw")
        
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
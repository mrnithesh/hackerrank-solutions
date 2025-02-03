import textwrap

def wrap(string, max_width):
    wraped= textwrap.wrap(string,max_width)
    return "\n".join(wraped)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
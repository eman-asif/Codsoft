def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def Mode(a,b):
    return a%b


def main():
    a,b = map(int,input('Enter two numbers:' ).split())
    c = input('Enter the symbol of operation to perform')
    if c == '+':
        print(add(a,b))
    elif c == '-':
        print(subtract(a,b))
    elif c == '*':
        print(multiply(a,b))
    elif c == '/':
        print(divide(a,b))
    elif c == '%':
        print(Mode(a,b))
main()
    
    

def(str):
    stack = []
    ans = 0
    for i in range(len(str)):
        if(str[i] == '('):
            stack.append(str[i])
        while(len(stack) > 0 and)
s='{[({[]}]}'
def check(s):
    stack=[]
    openings=['{','[','(']
    brackets={
        '[':']',
        '{':'}',
        '(':')'
    }
    for i in s:
        if i in openings:
            stack.append(i)
        else:
            if stack:
                top=stack.pop()
                if brackets[top]!=i:
                    return 'No'
            else:
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'   
print(check(s))         
    
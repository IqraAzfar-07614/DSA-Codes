Q2) Balanced Braces - Checks if the given brackets are balanced in the sequence or not - returns False if not balanced, returns True if balanced
#Uses only 1 stack and stack ADT operations
#Counters of any sort are not allowed to count the brackets

s=input()

def push(lst, item):
    lst.append(item)
    
def pop(lst):
    return lst.pop()

def top(lst):
    return lst[-1]

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
    
def balanced_braces(s):
    if len(s) % 2 == 1: #returns False if length of sequence is odd as it must be unbalanced for odd
        return False
    else:
        opening_braces = ['(', '[', '{']
        stack = []
        for x in s:
            if x in opening_braces: #pushes opening braces in the stack
                push(stack, x)
            else:
                if is_empty(stack): #if stack is empty, then the braces are not balanced as there must've been some opening brace for it to reach a closing brace, thus returns False
                    return False
                brace = pop(stack) #takes the top value from stack (pops) for comparison and checks for each case, if it does not match, any of them, false is returned as there is no opening brace for the closing brace at hand 
                if brace == '(': 
                    if x != ')': 
                        return False
                if brace == '[':
                    if x != ']':
                        return False
                if brace == '{':
                    if x != '}':
                        return False
        if not is_empty(stack): #if stack is still not empty after running through the loop, then the braces must not be balanced, thus returns False, but if it is empty at this point, the braces are balanced
            return False
        else:
            return True


print(balanced_braces(s))

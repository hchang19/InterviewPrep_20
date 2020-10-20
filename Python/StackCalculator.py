# Using a stack, implement a basic calulator that takes in Infix equation 
# as an input and return the value. 

#Convert infix notation into Postfix notation
#Example: 
# Infix eq: 1 + 2  
# Postfix eq: 2 1 +

def convertInfix(InfixExpr: str) -> str:

    helper_stack = []
    valid_operands = {'(' : 3, ')': 3, '^': 2, '*': 1, '/': 1, '+': 0, '-': 0}
    result = ""
    print(InfixExpr.split())
    #loop through each element of the posfix expression
    for key in InfixExpr.split():
        
        #check if key is a number 
        if(key.isnumeric()):
            result += key + ' '
        
        elif(key == '('):
            helper_stack.append(key)

        elif(key == ')'):
            if(len(helper_stack) == 0):
                print("The provided Infix equation is invalid")
                return "Invalid EQ"
            
            else:
                curr_key = helper_stack.pop()
                while(curr_key != '('):
                    result += curr_key + ' '
                    
                    curr_key = helper_stack.pop()
        
        #check if the key is a valid operand
        elif(key in valid_operands):

            if len(helper_stack) == 0:
                helper_stack.append(key)
            else:

                #compare level of the operand. Append it to the result string
                #until operand is ( or less than the current operation level
                while len(helper_stack) != 0:
                    curr_op = helper_stack[-1]

                    if(valid_operands[curr_op] < valid_operands[key] or curr_op == '('):
                        break
                    else:
                        result += helper_stack.pop() + ' '
                helper_stack.append(key)
                
        else:
            print("The provided Infix equation is invalid")
            return "Invalid EQ"
        
        print(result)
        print(helper_stack)
                

    #Get the remaining operators
    while len(helper_stack) != 0:
        result += helper_stack.pop() + ' '

    return result

print(convertInfix('( 1 + 2 ) * ( 2 + 3 )'))
#Takes in the Infix expression than return the resulting
#integer

#Steps


#Examples
#Infix eq: 1 + 2 + 3 + 4 * 5
#Postfix Notation: 1 2 + 3 + 4 5 * +

#Infix eq: 1*2+3*4+5
#Postfix: 1 2 * 3 4 * + 5 +

#Time complexity: O(n)
#Space complexity: O(n)
# It is guaranteed that each item is separated by a space 
def calculatePostfix(infixExpr: str) -> int:
    return 0

def calculateInfix(InfixExpr: str) -> int:
    
    return 0


from typing import List

def FizzBuzz(n):
    for i in range(1, n+1):
        divBy3 = (i % 3 == 0)
        divBy5 = (i%5 == 0)

        if(divBy3 and divBy5):
            print('FizzBuzz')
        elif(divBy3):
            print('Fizz')
        elif(divBy5):
            print('Buzz')
        else:
            print(i)

def FizzBuzzAlt(n):
    ret = []
    for i in range(1, n+1):
        divBy3 = (i % 3 == 0)
        divBy5 = (i%5 == 0)

        if(divBy3 and divBy5):
            ret.append('FizzBuzz')
        elif(divBy3):
            ret.append('Fizz')
        elif(divBy5):
            ret.append('Buzz')
        else:
            ret.append(i)

    return ret
  
def isPowerOf2(n):


    #first check for edge cases
    if(n == 0):
        return False 
    while(n%2 == 0):
        n/=2
    return n == 1
#Note: For loop is pretty dumb in python

#Problem 2 - Given a String S, replace the vowels and return the new string

#Approach 1 - use a while loop to iterate through
#Note: This is rather slow and effecient. For a string of size N, this takes O(N) time
def removeVowelsAlt1(S):
    ret = ''
    for i in S:
        if(i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u'):
            continue
        ret+= i

    return(ret)

#Approach 2 - use replace to remove the vowels
#This one actually has more time complexity than the original one since the replace functions
#are nested. Furthermore, this is very clunky as well

def removeVowelsAlt2(S):
    return S.replace('a', '').replace('e','').replace('i','').replace('o','').replace('u','')

#Approach 3 - use translate to remove the vowels
def removeVowelsAlt3(S):
    # return S.translate({ord(i):None for i in 'aeiou'})
    return S.translate(S.maketrans('','','aeiou'))



#Problem 3 - Robot Movement

#Approach 1 - count the number of LR and UD pairs. Check if they equal to 0 in the end

#Lets do this with a for loop
def isOriginAlt1(S):
    xaxis=0
    yaxis=0
    for i in S:
        if i == 'L':
            xaxis += 1
        elif i == 'R':
            xaxis -= 1
        elif i == 'U':
            yaxis += 1
        elif i == 'D':
            yaxis -= 1
        else:
            return 'Invalid Input'

    return xaxis == 0 and yaxis == 0

#User a table to implement a switch statement of sort
#The concept work but more research needs to be done reagrding the lambda
#another way is to define function and have them called

# def isOriginAlt2(S):
#     xaxis=0
#     yaxis=0

#     switchTable={
#         'R': lambda xaxis:xaxis+1,
#         'L': lambda xaxis:xaxis-1,
#         'U': lambda yaxis:yaxis+1,
#         'D': lambda yaxis:yaxis-1
#     }

    
#     for i in S:
#         switchTable.get(i, lambda :'Invalid String Input')

#Problem 4
#approach one is to iterate through the string and make all the character to lower case
#but it is better to just use the built in function 

def toLowerCase(S):
    return(S.lower())


#Problem 5
#Reverse a String
#Simple implementation from python library
def reverseString(S):
    return S[::-1]

def reverse(x):
    s = [1,-1][x < 0]
   
    print(s)

def validParenthese(s):
    stack = []
    if(len(s) == 0):
        return True
    for char in s:
        print(char)
        if char == "{" or char == "(" or char == "[":
            stack.append(char)
        else:
            if(len(stack) == 0):
                return False
            tempChar = stack.pop()
            if(char == "}" and tempChar == "{"):
                continue
            elif(char == "]" and tempChar == "["):
                continue
            elif(char == ")" and tempChar == "("):
                continue
            else:
                return False

    return len(stack) == 0
    
def backspaceCompare(S: str, T: str) -> bool:
    sIndex, tIndex = len(S)-1, len(T)-1
    sState = tState = 0
        
    while(sIndex >= 0 and tIndex >= 0):
        
        while(sIndex >= 0):
           
            if(S[sIndex] == "#"):
                sState += 1
                sIndex -= 1
            elif(sState > 0):
                sState -=1 
                sIndex -=1
            else:
                break
        
        print(sIndex)
        while(tIndex >= 0):
            if(T[tIndex] == "#"):
                tState += 1
                tIndex -= 1
            elif(tState > 0):
                tState -=1 
                tIndex -=1
            else:
                break
        
        print(tIndex)
    
        if(tIndex >= 0 and sIndex>= 0 and (T[tIndex] != S[sIndex])):
            return False
            
            
        tIndex -= 1
        sIndex -= 1
    
        return True




def main():
   print(backspaceCompare("a#c", "b"))








main()

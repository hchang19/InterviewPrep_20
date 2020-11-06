#pg 90 

#check if all characters in the element is unique
#O(n^2) approach
def isUnique1(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if(str[i] == str[j]):
                return False
    return True

def isUnique2(str):
    key = set()
    for char in str:
        if char in key:
            return False
        key.add(char)
    
    return True

#check if one permutation of one string is in another
#brute force approach
def isPermutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        keys = {}
        for char in str1:
            keys[char] += 1
        for char in str2:
            keys[char] -= 1

        for key in keys:
            if(keys[key] != 0):
                return False
        return True

def URLify(str):
    str = str.strip()
    str = str.replace(' ', '%20')
    print(str)



import re

def palindromePermutation(str):
    str = str.lower()
    str = [x for x in sorted(str) if x.isalpha()]
    print(str)
    stack = []

    for char in str:
        if(len(stack) == 0 ):
            stack.append(char)
        elif(stack[-1] == char):
            stack.pop()
        else:
            stack.append(char)
            
    
    if(len(str)%2 == 1):
        return len(stack) == 1
    else:
        return len(stack) == 0

from itertools import zip_longest

def oneAway(str1, str2):
    keys = list(zip_longest(str1, str2))
    errorCount = 0
    print(keys)

oneAway("abcdefghi", "bcdefghi")

test_array = "helloworld"

def modifyArray(arr):
    
    arr.pop(3)
    return
modifyArray(test_array)
print(test_array)
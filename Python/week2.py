
import collections
import itertools

def firstDuplicate(a):
    data = {}
    for(i, val) in enumerate(a):
        if(val in data):
            return i
        else:
            data[val] = 1
    return -1

def firstNotRepeatingCharacter(s):
    data = {}
    for char in s:
        if data.get(char):
            data[char] += 1
        else:
            data[char] = 1
    
    for char in data:
        if data[char] ==1:
            return char



def rotateImage(a):
    data = list(zip(*a))
    print([list(l)[::-1] for l in data])


def listTest(a):
    print(a[2:4])



def checkValidRows(grid):
    for row in grid:
        if(isNotValid(row)):
            return False
    
    return True

def checkSmallGrids(grid):
    for i in range(0,9,3):
        columns = list(zip(*grid[i:i+3]))
        for j in range(0,9,3):
            smallGrid = [x for c in columns[j:j+3] for x in list(c)]
            if(isNotValid(listc)):
                return False
    
    return True

def checkValidColumns(grid):
    columns = list(zip(*grid))
    for c in columns:
        if(isNotValid(list(c))):
            return False
    
    return True

#Return True if the array provided is not valid
def isNotValid(arr):
    result = [item for item, count in collections.Counter(arr).items() if item != '.' and count > 1 ]
    return result > 0


testData1 = [".",".",".",".",".",".","5",".","."]
testData2=['2','3','5','7','.','.','.']
testData = [0,1,2,3,4,5,6,7]
grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
rotateImageData = [[1, 2, 3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]
firstDuplicateData = ["Moon","Earth","Jupiter","Neptune","Earth","Venus"]

def isCryptSolution(crypt, solution):
    # base case to test with
    #return False if the crypt is not valid
    #return False if solution has no key

    if(len(crypt) != 3 or len(solution) == 0):
        return False

    solution_key = {}
    #Add the pair into hash map for easy access and search
    for pair in solution:
        solution_key[pair[0]] = pair[1]
    
    print(solution_key)
    
    result = 0
    for i in range(3):
        decrypt = ''.join([solution_key[c] for c in crypt[i]])
        if(not decrypt.isnumeric or decrypt[0] == '0'):
            return False
        if(i == 2):
            result -= int(decrypt)
            continue
        else:
            result += int(decrypt)

    return result


solution =[ ["O","0"], 
            ["M","1"], 
            ["Y","2"], 
            ["E","5"], 
            ["N","6"], 
            ["D","7"], 
            ["R","8"], 
            ["S","9"]]
testAny = [True, False, True, True]
dic = {ord(c): d for c, d in solution}
crypt= ["SEND", "MORE", "MONEY"]
v = list(map(lambda x: x.translate(dic),crypt))

print(any(testAny))



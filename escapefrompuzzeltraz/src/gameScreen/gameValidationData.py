import random


def getWinningKey():
    return winningKey


def generateCode():
    letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    code = ""
    for i in range(5):
        rand_index = random.randint(0, len(letters) -1)
        code += letters[rand_index]
    
    return code

# Stores the final winning key
winningKey = generateCode()
print(winningKey)
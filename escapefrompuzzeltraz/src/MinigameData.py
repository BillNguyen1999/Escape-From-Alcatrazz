import random
class MinigameData():
    def __init__(self):
        self.minigameNum = 0
        self.board = []
        self.enemies = []
        self.minigames = []
        self.player = 0
        self.height = 0
        self.width = 0
        self.lives = 3
        self.key = 0
        self.won = False
        self.playing = True
        self.running = True
        


def makeMinigame1():
        mg = MinigameData()
        mg.minigameNum = 1
        mg.height = 8
        mg.width = 8
        mg.board = [[1,1,1,0,1,1,0,1],
        [1,1,1,0,1,1,1,1],
        [1,1,0,0,1,1,0,1],
        [1,0,1,0,0,0,1,1],
        [1,1,1,0,1,1,1,1],
        [1,1,0,1,1,1,0,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,0,1,1,0,1]
        ]
        mg.player = playerObject()
        mg.enemies = [enemyObject([[4,0],[4,1], [4,2], [3,2],[4,2],[4,1]]), 
        enemyObject([[4,4],[5,4],[6,4],[7,4],[7,5],[6,5],[5,5],[4,5]]),
        enemyObject([[0,7], [1,7], [2,7], [3,7], [4,7], [5,7],[6,7],[7,7], [6,7], [5,7], [4,7], [3,7], [2,7], [1,7]])
        ]
        mg.item = item(1,5)
        mg.key = "a"

        return mg

class item:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.w = 10

class playerObject: #for use in mg1 and any others that require it
    def __init__(self):
        self.x = 0
        self.y = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.w = 10

    def updatePlayer(self, gameData):
        if(self.left and validMove(self.x - 1, self.y, gameData)):
            self.x -= 1
        if(self.right and validMove(self.x + 1, self.y, gameData)):
            self.x += 1
        if(self.up and validMove(self.x, self.y - 1, gameData)):
            self.y -= 1
        if(self.down and validMove(self.x, self.y + 1, gameData)):
            self.y +=1

class enemyObject:
    def __init__(self, path):
        
        self.x = path[0][0]
        self.y = path[0][1]
        self.w = 30
        self.path = path
        

    def updateEnemy(self):
        
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        
        temp = self.path.pop(0)
        self.path.append(temp)

def validMove(x, y, data):
    if(data.width <= x or x < 0):
        return False
    if(data.height <= y or y < 0):
        return False
    if(data.board[x][y] == 0):
        return False
    return True


    


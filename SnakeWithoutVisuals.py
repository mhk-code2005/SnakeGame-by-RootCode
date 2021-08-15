class Board(object):
    def __init__(self,n):
        self.n=n
        board=[]
        for i in range(n):
            k=[]
            for t in range(n):
                k.append(' * ')
            board.append(k)
        self.board=board

    def __str__(self):
        Str=''
        for i in self.board:
            Str+=''.join(i)+'\n'
        return Str

    def getCoord(self,n1,n2):
        return self.board[n1][n2]
    
    def getBoard(self):
        return self.board

    def updateBoard(self, coordList,symbol, appleCoord):
        #coordlist: liste of snake coordinates
        #symbol='S'
        for coord in coordList:
            self.board[coord[0]][coord[1]]=symbol

        for i in range(self.n):
            for b in range(self.n):
                if (i,b) in coordList:
                    if (i,b)==coordList[0]:
                        self.board[i][b]=' H ' 
                    else:
                        self.board[i][b]=symbol
                elif (i,b)==appleCoord:
                    self.board[i][b]=' A '
                else:
                    self.board[i][b]=' * '

    def OutBoard(self,coordlist):
        head=coordlist[0]
        i,b=head[0], head[1]
        if i<0 or i>self.n or b<0 or b>self.n:
            return True
        return False

    def createApple(self, coordlist):
        symbol=' A '
        import random as rn
        x,y=rn.randint(0,self.n-1), rn.randint(0,self.n-1)
        while (x,y) in coordlist:
            x,y=rn.randint(0,self.n), rn.randint(0,self.n)
        self.board[x][y]=' A '
        return (x,y)


class snake(object):
    def __init__(self,coord=[(5,5),(5,4),(5,3)]):
        self.coord=coord
        self.symbol='~- '

    def getSnakeCoords(self):
        return self.coord

    def getSymb(self):
        return self.symbol

    def isAppleEaten(self, coord):
        if coord==self.coord[0]:
            return True
        return False


    def move(self, initWay,apple, turnWay=None):
        copyCord=self.getSnakeCoords()[:]
        t=copyCord[-1]
        copyCord.remove(copyCord[len(copyCord)-1])
        for index in range(len(self.coord)): 
                if index==0:
                    if turnWay==None:
                        headTurn=initWay
                    else:
                        headTurn=turnWay
                    if headTurn=='right':
                            self.coord[0]=(self.coord[0][0],self.coord[0][1]+1)
                    if headTurn=='left':
                            self.coord[0]=(self.coord[0][0],self.coord[0][1]-1)
                    if headTurn=='down':
                            self.coord[0]=(self.coord[0][0]+1,self.coord[0][1])               
                    if headTurn=='up':
                            self.coord[0]=(self.coord[0][0]-1,self.coord[0][1])
        self.coord[1:len(self.coord)]=copyCord
        if apple==self.coord[0]:
            self.coord.append(t)
            
    def didSnakeOverlap(self):
        for i in self.coord:
            if self.coord.count(i)>1:
                return True
                






class AD:
    def __init__(self):
        ##                            x
        self.board=[[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0]]
        ##         y
        self.solutions=[]

    def put_queen(self,y):
        """ put a D-stone on the next empty field """
        if y>7: ## Break Criteria
            self.solutions.append(ChessBoard(self.board))
            return None
        else:
            for x in range(0,8):
                if self.board[y][x]==0:
                    self.board[y][x]='D'
                    self.lock(x,y)
                    self.put_queen(y+1)
                    self.delete(x,y)

    def delete(self,x,y):
        for i in range(0,8):
            # decrease counters / skip D or X
            if self.board[y][i] not in ('D','X'):
                self.board[y][i]-=1
            if self.board[i][x] not in ('D','X'):
                self.board[i][x]-=1
        for i in range(1,8):
            if x-i>=0 and y-i>=0:
                if self.board[y-i][x-i] not in ('D','X'):
                    self.board[y-i][x-i] -=1 ## top left
            if x+i<=7 and y+i<=7:
                if self.board[y+i][x+i] not in ('D','X'):
                    self.board[y+i][x+i] -=1 ## bottom right
            if x+i<=7 and y-i>=0:
                if self.board[y-i][x+i] not in ('D','X'):
                    self.board[y-i][x+i] -=1 ## top right
            if x-i>=0 and y+i<=7:
                if self.board[y+i][x-i] not in ('D','X'):
                    self.board[y+i][x-i] -=1 ## bottom left

        self.board[y][x]=0

    def lock(self,x,y):
        for i in range(0,8):
            if self.board[y][i] not in ('D','X'):
                self.board[y][i]+=1
            if self.board[i][x] not in ('D','X'):
                self.board[i][x]+=1
        for i in range(1,8):
            if x-i>=0 and y-i>=0:
                if self.board[y-i][x-i] not in ('D', 'X'):
                    self.board[y-i][x-i] +=1 ## top left
            if x+i<=7 and y+i<=7:
                if self.board[y+i][x+i] not in ('D', 'X'):
                    self.board[y+i][x+i] +=1 ## bottom right
            if x+i<=7 and y-i>=0:
                if self.board[y-i][x+i] not in ('D', 'X'):
                    self.board[y-i][x+i] +=1 ## top right
            if x-i>=0 and y+i<=7:
                if self.board[y+i][x-i] not in ('D', 'X'):
                    self.board[y+i][x-i] +=1 ## bottom left

    def print_board(self):
        for x in range(0,8):
            print(self.board[x])
        print
        
class ChessBoard:
    """ """
    def __init__(self, board):
        self.board=[[],[],[],[],[],[],[],[]]
        for i in range(0,8):
            for j in range(0,8):
             if board[i][j]=='D':
                 self.board[i].append("X")
             else:
                 self.board[i].append('0')
                
    def printloesung(self):
        for x in range(0,8):
            print(self.board[x])
        print

Prog=AD()
Prog.print_board()
Prog.put_queen(0)

for i, solution in enumerate(Prog.solutions):
    print("Solution #%d"%(i+1))
    solution.printloesung()
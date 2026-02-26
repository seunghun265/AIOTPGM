table = []

def printList(twoDL):
    for row in range(len(twoDL)):
        for col in range(len(twoDL[0])):
            print(twoDL[row][col], end=" ")
        print()
        
def init(twoDl):
    for row in range(len(twoDl)):
        for col in range(len(twoDl[0])):
            if(row + col)%2 == 0 :
                table[row][col] = 1
            
table = [[0]*10 for _ in range(10)]
    
init(table)
printList(table)

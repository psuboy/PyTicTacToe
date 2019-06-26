#Tic Tac Toe Game:
def printTheBoard(board):
    #print top row:
    print(' ' + board['TL'] + ' | ' + board['TM'] + ' | ' + board['TR'] + ' ')
    print('-----------')
    print(' ' + board['ML'] + ' | ' + board['MM'] + ' | ' + board['MR'] + ' ')
    print('-----------')
    print(' ' + board['LL'] + ' | ' + board['LM'] + ' | ' + board['LR'] + ' ')

def playSelection(board,board2,marker):
    print('Enter the box where you want to play: ')
    print(' valid selections are: TL, TM, TR, ML, MM, MR, LL, LM, or LR')
    selection = input().upper()
    if selection in board.keys():
        if board[selection] == ' ':
            board[selection] = marker
            board2[selection] = .1
        else:
            print('that field is already taken')
            playSelection(board,board2, marker)
    else:
        print('you did not enter a valid selection')
        playSelection(board,board2,marker)

#This function checks to see if the computer can win on this play.
def checForSituation(board,val):
    # Check diagonal
    if addThree(board, 'TL', 'MM', 'LR') == val:
        if board['TL'] == 0:
            return 'TL'
        elif board['MM'] == 0:
            return 'MM'
        else:
            return 'LR'
    if addThree(board, 'TR', 'MM', 'LL') == val:
        if board['TR'] == 0:
            return 'TR'
        elif board['MM'] == 0:
            return 'MM'
        else:
            return 'LL'
    #check vertical
    if addThree(board, 'TR', 'MR','LR') == val:
        if board['TR'] == 0:
            return 'TR'
        elif board['MR'] == 0:
            return 'MR'
        else:
            return 'LR'
    if addThree(board, 'TM', 'MM','LM') == val:
        if board['TM'] == 0:
            return 'TM'
        elif board['MM'] == 0:
            return 'MM'
        else:
            return 'LM'
    if addThree(board, 'TL', 'ML','LL') == val:
        if board['TL'] == 0:
            return 'TL'
        elif board['ML'] == 0:
            return 'ML'
        else:
            return 'LL'
    #check horizontal
    if addThree(board, 'TL', 'TM','TR') == val:
        if board['TL'] == 0:
            return 'TL'
        elif board['TM'] == 0:
            return 'TM'
        else:
            return 'TR'
    if addThree(board, 'ML', 'MM','MR') == val:
        if board['ML'] == 0:
            return 'ML'
        elif board['MM'] == 0:
            return 'MM'
        else:
            return 'MR'
    if addThree(board, 'LL', 'LM','LR') == val:
        if board['LL'] == 0:
            return 'LL'
        elif board['LM'] == 0:
            return 'LM'
        else:
            return 'LR' 
    return 'negative'



def computerPlay(board, board2, computerPiece):
    #what piece does the human use?
    if computerPiece == 'O':
        playerPiece == 'X'
    else:
        playerPiece =='O'
    #check to see if you can win
    move = checForSituation(board2,2)
    if move != 'negative':
        board[move] = computerPiece
        board2[move] = 1
        return
    #check for Defensive plays:
    #check for empty corner
    #check for middle
    if board['MM'] == ' ':
        board['MM'] = computerPiece
        board2['MM'] = 1
        return
    #select the first blank box and mark it.
    for k,v in board.items():
        if v == ' ':
            board[k] = computerPiece
            board2[k] = 1
            return


def addThree(board,first,second,third):
    return board[first] + board[second] + board[third]

#This functilon checks to see if the game has been one by X or O.  It does not use the mumerical board which would be way easier....
#TODO update this function to use numberical board.
def checkForTheWin(Board): 
    #check diaginal
    if Board['TL'] != ' ' and Board['TL'] == Board['MM'] and Board['TL'] == Board['LR']:
        return Board['TL']
    if Board['TR'] != ' ' and Board['TR'] == Board['MM'] and Board['TR'] == Board['LL']:
        return Board['TR']
    #check Vertical
    if Board['TL'] != ' ' and Board['TL'] == Board['ML'] and Board['TL'] == Board['LL']:
        return Board['TL']
    if Board['TM'] != ' ' and Board['TM'] == Board['MM'] and Board['TM'] == Board['LM']:
        return Board['TM']
    if Board['TR'] != ' ' and Board['TR'] == Board['MR'] and Board['TR'] == Board['LR']:
        return Board['TR']
    #check Horizontal
    if Board['TL'] != ' ' and Board['TL'] == Board['TM'] and Board['TL'] == Board['TR']:
        return Board['TL']
    if Board['ML'] != ' ' and Board['ML'] == Board['MM'] and Board['ML'] == Board['MR']:
        return Board['ML']
    if Board['LR'] != ' ' and Board['LR'] == Board['LM'] and Board['LR'] == Board['LL']:
        return Board['LR']
    return 'No Winner'



#theBoard is the X/O board
theBoard = {'TL':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR':' ','LL':' ','LM':' ','LR':' '}
# numBoard is the mumerical representation of the board... 1 = cumputer move, .1 for the human moves
numBoard = {'TL':0,'TM':0,'TR':0,'ML':0,'MM':0,'MR':0,'LL':0,'LM':0,'LR':0}

print('Welcome to Tic Tac Toe.  Starting a new game.  Enter X to play X, or anything else to play O: ')
playerPiece = input().upper()
print('You are playing as '+ playerPiece)
# The number of moves (represented by i in the for loop) should be less than or equal to 9. if it is 9 or more that means the board is full.
for i in range(0,9):

    if i % 2 == 0:
        move = 'X'
    else:
        move = 'O'
    print('Your turn ' + move + ' It is move number ' + str(i+1))
    printTheBoard(theBoard)

    if playerPiece == move:
        playSelection(theBoard, numBoard, move)
    else:
        computerPlay(theBoard,numBoard, move)
    result = checkForTheWin(theBoard)
    # TODO trouble shooting ...deleteprint('this is result' + result)
    if result == 'No Winner':
        continue
    else: 
        print('game over ' + result + ' is the winner!')
        break
printTheBoard(theBoard)

#TODO change the write out player piece = x to You selected X/OT
#TODO AI ideas:  set up a second board that gets updated with theBoard...  
    # This board will use 1s for the computer and .1s for the human player.  We can then do simple addition to look for the 
        #Win, block or or other placements...adding the numbers will tell us if we hit some of these conditions. 
#TODO change from the selection of an X or O to asking if they want to go first or second.  
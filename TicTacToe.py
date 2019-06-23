#Tic Tac Toe Game:
def printTheBoard(board):
    #print top row:
    print(' ' + board['TL'] + ' | ' + board['TM'] + ' | ' + board['TR'] + ' ')
    print('-----------')
    print(' ' + board['ML'] + ' | ' + board['MM'] + ' | ' + board['MR'] + ' ')
    print('-----------')
    print(' ' + board['LL'] + ' | ' + board['LM'] + ' | ' + board['LR'] + ' ')

def playSelection(board,marker):
    print('Enter the box where you want to play: ')
    print(' valid selections are: TL, TM, TR, ML, MM, MR, LL, LM, or LR')
    selection = input().upper()
    if selection in board.keys():
        if board[selection] == ' ':
            board[selection] = marker
        else:
            print('that field is already taken')
            playSelection(board,marker)
    else:
        print('you did not enter a valid selection')
        playSelection(board,marker)

def computerPlay(board, computerPiece):
    #what piece does the human use?
    if computerPiece == 'O':
        playerPiece == 'X'
    else:
        playerPiece =='O'
    #check for win
    #check for Defensive plays:
    #check for empty corner
    #check for middle
    if board['MM'] == ' ':
        board['MM'] = computerPiece
        return
    #select the first blank box and mark it.
    for k,v in board.items():
        if v == ' ':
            board[k] = computerPiece
            return

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

theBoard = {'TL':' ','TM':' ','TR':' ','ML':' ','MM':' ','MR':' ','LL':' ','LM':' ','LR':' '}
# The number of moves should be less than or equal to 9. if it is 9 or more that means the board is full.

print('Welcome to Tic Tac Toe.  Starting a new game.  Enter X to play X, or anything else to play O: ')
playerPiece = input().upper()
print('You are playing as '+ playerPiece)

for i in range(0,9):

    if i % 2 == 0:
        move = 'X'
    else:
        move = 'O'
    print('Your turn ' + move + ' It is move number ' + str(i+1))
    printTheBoard(theBoard)

    if playerPiece == move:
        playSelection(theBoard, move)
    else:
        computerPlay(theBoard, move)
    result = checkForTheWin(theBoard)
    # TODO trouble shooting ...deleteprint('this is result' + result)
    if result == 'No Winner':
        continue
    else: 
        print('game over ' + result + ' is the winner!')
        break
printTheBoard(theBoard)

#TODO change the write out player piece = x to You selected X/OT
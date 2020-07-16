import random
import time

gridList = 'A1 A2 A3 A4 A5 B1 B2 B3 B4 B5 C1 C2 C3 C4 C5 D1 D2 D3 D4 D5 E1 E2 E3 E4 E5'.split()
#list to check for hits over two rows
rightColumn = [4, 9, 14, 19, 24]
rightColumns = [3, 8, 13, 18, 23, 4, 9, 14, 19]
leftColumn = [0, 5, 10, 15, 20]
leftColumns = [5, 10, 15, 20, 1, 6, 11, 16, 21]
topRows = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
topRow = [0, 1, 2, 3, 4]
bottomRows = [15, 16, 17, 18, 19, 20, 21, 22, 23, 34]
bottomRow = [20, 21, 22, 23, 24]
columnA = [0, 5, 10, 15, 20]
columnB = [1, 6, 11, 16, 21]
columnD = [3, 8, 13, 18, 23]
columnE = [4, 9, 14, 19, 24]
row1 = [0, 1, 2, 3, 4]
row2 = [5, 6, 7, 8, 9]
row4 = [15, 16, 17, 18, 19]
row5 = [20, 21, 22, 23, 24]
noAttack = ['X','!','#']
deadEnd = ['X','#']

def chooseOrder():
    #randomly chooses a player to go first
    num = random.randint(0,1)

    if num == 1:
        return 'player'
    else:
        return 'cpu'

def compBoardHider(board):
    #takes computer board, hides ships but shows hits and misses
    shownBoard = ['_'] * 25

    for i in range(len(board)):
        if board[i] == 'S':
            shownBoard[i] = '_'
        if board[i] == 'B':
            shownBoard[i] = '_'
        if board[i] == '!':
            shownBoard[i] = '!'
        if board[i] == '#':
            shownBoard[i] = '#'
        if board[i] == 'X':
            shownBoard[i] = 'X'

    return shownBoard

def gridInputConvert(gridInput):
    #converts player's input in grid format to corresponding number for grid list
    for i in range(len(gridList)):
        if gridInput == gridList[i]:
            placementNumber = i
            return placementNumber

def displayBoard(board, whichBoard):
    #prints either player's or cpu's board
    print('')
    print(whichBoard + ' Board:')
    time.sleep(1)
    print('  1|2|3|4|5')
    print('A ' + board[0] + '|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4])
    print('B ' + board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8] + '|' + board[9])
    print('C ' + board[10] + '|' + board[11] + '|' + board[12] + '|' + board[13] + '|' + board[14])
    print('D ' + board[15] + '|' + board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19])
    print('E ' + board[20] + '|' + board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24])
    print()
    time.sleep(1)

def placeShip(board, coordList, shipLetter):
    #writes passed ship's letter to passed board using ship's coordinate list
    for i in coordList:
        board[i] = shipLetter

    return board

def cpuShipBigCoords():
    #places computer's ships on the board

    board = ['_'] * 25
    
    #randomly picks a grid position for big ship
    placementNumber = random.randint(0, 24)

    #picks an orientation and checks to make sure it isn't off the board
    #0 is up, 1 is right, 2 is down, 3 is left
    
    while True:
        orientationNumber = random.randint(0,3)
        orientationList = []
        
        #establishes list with grid numbers to be checked
        if orientationNumber == 0:
            orientationList = [placementNumber, placementNumber + 5, placementNumber + 10]
        if orientationNumber == 1:
            orientationList = [placementNumber, placementNumber + 1, placementNumber + 2]
        if orientationNumber == 2:
            orientationList = [placementNumber, placementNumber - 5, placementNumber - 10]
        if orientationNumber == 3:
            orientationList = [placementNumber - 2, placementNumber - 1, placementNumber]

        #set up variables to check for correct ship placement
        offBoardCheck = ''
        for i in orientationList:
            offBoardCheck = offBoardCheck + str(i)
        ###print(offBoardCheck)

        rejectPlacement = False
        if offBoardCheck in '345 456 8910 91011 131415 141516 181920 192021'.split():
            rejectPlacement = True
        for i in orientationList:
            if i < 0 or i > 24:
                rejectPlacement = True

        if rejectPlacement == False:
            return orientationList

def cpuShipSmallCoords(board):

    #place smaller ship
    spaceIsFree = False
    while spaceIsFree == False:
        placementNumberS = random.randint(0,24)
        if board[placementNumberS] == '_':
            spaceIsFree = True

    while True:
        orientationNumber = random.randint(0,3)
        orientationList = []

        #establishes list with grid numbers to be checked
        if orientationNumber == 0:
            orientationList = [placementNumberS, placementNumberS + 5,]
        if orientationNumber == 1:
            orientationList = [placementNumberS, placementNumberS + 1,]
        if orientationNumber == 2:
            orientationList = [placementNumberS, placementNumberS - 5,]
        if orientationNumber == 3:
            orientationList = [placementNumberS - 1, placementNumberS]

        #set up variables to check for correct ship placement
        offBoardCheck = ''
        for i in orientationList:
            offBoardCheck = offBoardCheck + str(i)
        ###print(offBoardCheck)

        clip = 0
        rejectPlacement = False
        if offBoardCheck in '45 910 1415 1920'.split():
            rejectPlacement = True
            ###print('split over two rows')
            clip = 1
        if clip == 0:
            for i in orientationList:
                if i < 0 or i > 24:
                    rejectPlacement = True
                    ###print('off board')
                    clip = 1
        if clip == 0:
            for i in orientationList:
                if board[i] != '_':
                    rejectPlacement = True
                    ###print('space occupied')

        if rejectPlacement == False:
        
            return orientationList

def placePlayerShipBigCoords():
    #places computer's ships on the board

    board = ['_'] * 25
    gridList = 'A1 A2 A3 A4 A5 B1 B2 B3 B4 B5 C1 C2 C3 C4 C5 D1 D2 D3 D4 D5 E1 E2 E3 E4 E5'.split()
    orientationOptionList = 'up right down left'.split()
    orientationNumber = 9

    displayBoard(board, 'Your')
    
    #player picks a grid position for big ship
    print('Select a position on the grid for your big ship.')
    playerInputOk = False
    while playerInputOk == False:
        playerInput = input()
        playerInput = playerInput.upper()
        if playerInput not in gridList:
            print('Please input a letter followed by a number from the board. Ex: "A1"')
        else:
            playerInputOk = True

    #converts grid input to number
    placementNumber = gridInputConvert(playerInput)   
    
    ###print('This is the player\'s big ship\'s placement number: ' + str(placementNumber))

    #player picks an orientation
    print('Now choose an orientation for your ship (Note: the ship is 3 spaces long). Please enter up, down, left, or right.')

    while True:
        
        orientationInputCheck = False
        while orientationInputCheck == False:
            stopper = 0
            orientationInput = input()
            orientationInput = orientationInput.lower()
            if orientationInput not in orientationOptionList:
                print('Please type "up", "down", "left", or "right".')
            else:                      
                #converts to number for list, 0 is up, 1 is right, 2 is down, 3 is left
                for i in range(len(orientationOptionList)):
                    if orientationOptionList[i] == orientationInput:
                        orientationNumber = i
                    
                orientationList = []
                    
                #establishes list with grid numbers to be checked
                if orientationNumber == 0:
                    orientationList = [placementNumber, placementNumber - 5, placementNumber - 10]
                if orientationNumber == 1:
                    orientationList = [placementNumber, placementNumber + 1, placementNumber + 2]
                if orientationNumber == 2:
                    orientationList = [placementNumber, placementNumber + 5, placementNumber + 10]
                if orientationNumber == 3:
                    orientationList = [placementNumber - 2, placementNumber - 1, placementNumber]
                ###print('This is the orientationList: ' + str(orientationList))
                
                #set up variables to check for correct ship placement
                offBoardCheck = ''
                for i in orientationList:
                    offBoardCheck = offBoardCheck + str(i)
                ###print('These are the offBoardCheck values: ' + offBoardCheck)

                #make sure ship isn't split over two rows
                if stopper == 0:
                    if offBoardCheck in '345 456 8910 91011 131415 141516 181920 192021'.split():
                        stopper = 1
                        print('Your ship is off the board. Please choose a different orientation.')
                #make sure ship isn't off the board
                if stopper == 0:
                    clip = 0
                    for i in orientationList:
                        if i < 0 or i > 24:
                            if clip == 0:
                                stopper = 1
                                print('Your ship is off the board. Please choose a different orientation.')
                                clip = 1

                if stopper == 0:
                    #return coords

                    return orientationList

def placePlayerShipSmallCoords(board):
    
    displayBoard(board, 'Your')
    orientationOptionList = 'up right down left'.split()
    print('Your big ship is in position! Now choose a space for your small ship.')

    playerInputOk = False
    while playerInputOk == False:
        playerInput = input()
        playerInput = playerInput.upper()

        #converts grid input to number
        placementNumberS = gridInputConvert(playerInput)
        
        if playerInput not in gridList:
            print('Please input a letter followed by a number from the board. Ex: "A1"')
        elif board[placementNumberS] != '_':
            print('That space is already occupied. Please choose a different space.')
        else:
            playerInputOk = True

    ###print('This is the small ship\'s placement number: ' + str(placementNumberS))

    print('Now choose an orientation for your ship (Note: this ship is 2 spaces long). Please enter up, down, left, or right.')

    while True:
        
        orientationInputCheck = False
        while orientationInputCheck == False:
            stopper = 0
            orientationInput = input()
            orientationInput = orientationInput.lower()
            if orientationInput not in orientationOptionList:
                print('Please type "up", "down", "left", or "right".')
            else:                      
                #converts to number for list, 0 is up, 1 is right, 2 is down, 3 is left
                for i in range(len(orientationOptionList)):
                    if orientationOptionList[i] == orientationInput:
                        orientationNumber = i
                        ###print('This is the small ship orientationNumber: ' + str(orientationNumber))
                    
                orientationList = []
                ###print('This is the small ship orientation list empty: ' + str(orientationList))
                
                #establishes list with grid numbers to be checked
                if orientationNumber == 0: #up
                    orientationList = [placementNumberS, placementNumberS - 5]
                if orientationNumber == 1: #right
                    orientationList = [placementNumberS, placementNumberS + 1]
                if orientationNumber == 2: #down
                    orientationList = [placementNumberS, placementNumberS + 5]
                if orientationNumber == 3: #left
                    orientationList = [placementNumberS, placementNumberS - 1]
                ###print('This is the small ship orientation list full: ' + str(orientationList))

                #set up variables to check for correct ship placement
                offBoardCheck = ''
                for i in orientationList:
                    offBoardCheck = offBoardCheck + str(i)
                ###print('These are the offBoardCheck values: ' + offBoardCheck)

                #make sure ship isn't split over two rows
                if stopper == 0:
                    if offBoardCheck in '45 54 910 109 1415 1514 1920 2019'.split():
                        stopper = 1
                        print('Your ship is off the board. Please choose a different orientation.')
                #make sure ship isn't off the board
                if stopper == 0:
                    clip = 0
                    for i in orientationList:
                        if i < 0 or i > 24 and clip == 0:
                            stopper = 1
                            print('Your ship is off the board. Please choose a different orientation.')
                            clip =1
                #make sure small ship isn't intersecting with big ship
                if stopper == 0:
                    clip = 0
                    for i in orientationList:
                        if clip == 0:
                            if board[i] == 'B':
                                print('Your small ship is running into your big ship. Please choose a different orientation.')
                                stopper = 1
                                clip = 1

                if stopper == 0:

                    return orientationList

def getPlayerAttack(board):
    print('Please choose a grid position to attack.')

    #gets player's attack input
    while True:
        attackInput = input()
        attackInput = attackInput.upper()
        attackNumber = gridInputConvert(attackInput)

        if attackInput not in gridList:
            print('Please type a letter followed by a number. Ex: "C3".')
        elif board[attackNumber] in noAttack:
            print('You have already attacked that position. Please choose again.')
        else:
            return attackNumber

def getCompAttack(board):

    check = 0
    
    for i in range(len(board)):
        if check == 0:
            if board[i] == '!':
                ###print('Hit detected at' + str(i))

                #attack right
                if i not in rightColumns:
                    ###print('code 13')
                    if board[i + 1] == '!' and board[i + 2] not in noAttack:
                        ###print('code 13a')
                        return i + 2
                if i not in leftColumn and i not in rightColumn:
                    if board[i - 1] == '!' and board[i - 2] in deadEnd and board[i + 1] not in noAttack:
                        ###print('code 13b')
                        return i + 1
                #attack left
                if i not in leftColumns:
                    ###print('code 14')
                    if board[i - 1] == '!' and board[i - 2] not in noAttack:
                        ###print('code 14a')
                        return i - 2
                if i not in leftColumn and i not in rightColumn:
                    if board[i + 1] == '!' and board[i + 2] in deadEnd and board[i - 1] not in noAttack:
                        ###print('code 14b')
                        return i - 1
                #attack down
                if i not in bottomRows:
                    ###print('code 15')
                    if board[i + 5] == '!' and board[i + 10] not in noAttack:
                        ###print('code 15a')
                        return i + 10
                if i not in bottomRow and i not in topRow:
                    if board[i - 5] == '!' and board[i - 10] in deadEnd and board[i + 5] not in noAttack:
                        ###print('code 15b')
                        return i + 5
                #attack up
                if i not in topRows:
                    ###print('code 16')
                    if board[i - 5] == '!' and board[i - 10] not in noAttack:
                        ###print('code 16a')
                        return i - 10
                if i not in bottomRow and i not in topRow:
                    if board[i + 5] == '!' and board[i + 10] in deadEnd and board[i - 5] not in noAttack:
                        ###print('code 16b')
                        return i - 5
                
                #attack adjacent space
                if i == 0:
                    ###print('code 17')
                    if board[1] not in noAttack:
                        return 1
                    elif board[5] not in noAttack:
                        return 5
                elif i in [1, 2, 3]:
                    ###print('code 18')
                    if board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i + 1] not in noAttack:
                        return i + 1
                    elif board[i + 5] not in noAttack:
                        return i + 5
                elif i == 4:
                    ###print('code 19')
                    if board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i + 5] not in noAttack:
                        return i + 5
                elif i in [5, 10, 15]:
                    ###print('code 20')
                    if board[i + 1] not in noAttack:
                        return i + 1
                    elif board[i - 5] not in noAttack:
                        return i - 5
                    elif board[i + 5] not in noAttack:
                        return i + 5
                elif i in [6, 7, 8, 11, 12, 13, 16, 17, 18]:
                    ###print('code 21')
                    if board[i + 1] not in noAttack:
                        return i + 1
                    elif board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i - 5] not in noAttack:
                        return i - 5
                    elif board[i + 5] not in noAttack:
                        return i + 5
                elif i in [9, 14, 19]:
                    ###print('code 22')
                    if board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i - 5] not in noAttack:
                        return i - 5
                    elif board[i + 5] not in noAttack:
                        return i + 5
                elif i == 20:
                    ###print('code 23')
                    if board[i - 5] not in noAttack:
                        return i - 5
                    elif board[i + 1] not in noAttack:
                        return i + 1
                elif i in [21, 22, 23]:
                    ###print('code 24')
                    if board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i + 1] not in noAttack:
                        return i + 1
                    elif board[i - 5] not in noAttack:
                        return i - 5
                elif i == 24:
                    ###print('code 25')
                    if board[i - 1] not in noAttack:
                        return i - 1
                    elif board[i - 5] not in noAttack:
                        return i - 5
                else:
                    ###print('Stopping attack selection algorithm.')
                    check = 1

    #if no hits, attack random
    ###print('No hit detected.')
    while True:
        clip = 0
        randomAttack = random.randint(0,24)
        
        #the below checks will prevent the computer from attacking a space that cannot hold a ship (single space)
                
        #corners
        if randomAttack == 0 and board[1] in deadEnd and board[5] in deadEnd:
            clip = 1
        if randomAttack == 4 and board[3] in deadEnd and board[9] in deadEnd:
            clip = 1
        if randomAttack == 20 and board[15] in deadEnd and board[21] in deadEnd:
            clip = 1
        if randomAttack == 24 and board[19] in deadEnd and board[23] in deadEnd:
            clip = 1

        #sides
        if randomAttack in [1, 2, 3] and board[randomAttack - 1] in deadEnd and board[randomAttack + 1] in deadEnd and board[randomAttack + 5] in deadEnd:
            clip = 1
        if randomAttack in [21, 22, 23] and board[randomAttack - 1] in deadEnd and board[randomAttack + 1] in deadEnd and board[randomAttack - 5] in deadEnd:
            clip = 1
        if randomAttack in [5, 10, 15] and board[randomAttack - 5] in deadEnd and board[randomAttack + 5] in deadEnd and board[randomAttack + 1] in deadEnd:
            clip = 1
        if randomAttack in [9, 14, 19] and board[randomAttack - 5] in deadEnd and board[randomAttack + 5] in deadEnd and board[randomAttack - 1] in deadEnd:
            clip = 1

        #middle
        if randomAttack in [6,7,8,11,12,13,16,17,18] and board[randomAttack - 1] in deadEnd and board[randomAttack + 1] in deadEnd and board[randomAttack + 5] in deadEnd and board[randomAttack - 5] in deadEnd:
            clip = 1

        
        if board[randomAttack] == 'X' or board[randomAttack] == '#':
            clip = 1

        
        if clip == 0:
            return randomAttack
                
                #elif i - 1 not in rightColumn and if i + 1 not in leftColumn and if i + 2 not in leftColumn:
                #    if board[i + 1] == '!' and if board[i + 2] == 'X' and if board[i - 1] == '_':
                #        return i - 1
                #elif i not in rightColumn and if i not in leftColumn:
                #    if board[i - 1] == '!' and if board[i - 2] == 'X' and if board[i - 1] == '_':
                #        return i - 1
                
        
def checkAttackResult(attackNumber, board):

    #result for big ship hit
    if board[attackNumber] == 'B':
        ###print('big')
        return 'big'
    if board[attackNumber] == 'S':
        ###print('small')
        return 'small'
    if board[attackNumber] == '_':
        ###print('miss')
        return 'miss'

def startNewGame():
    #Checks if player wants to start another game
    time.sleep(2)
    print('Would you like to play again? Please enter "yes" or "no".')
    options = ['yes', 'no']
    while True:
        check = input()
        check = check.lower()

        if check not in options:
            print('Please enter "yes" or "no".')
        elif check == 'yes':
            return True
        else:
            return False
        

#GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE 
#GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE
#GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE GAME LOOP STARTS HERE 

playAgain = True

print('Welcome to BATTLEBOAT!')
time.sleep(2)
print('Can you defeat the great Winston?')
time.sleep(2)
print('Let\'s find out...')
time.sleep(2)

while playAgain == True:
    #The game is reset

    #draws a board
    blankBoard = ['_'] * 25

    #set ship hit counts to 0
    compShipBigHitCount = 0
    compShipSmallHitCount = 0
    playerShipSmallHitCount = 0
    playerShipBigHitCount = 0

    print('Winston sets his pieces...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Winston is ready.')
    #get coords of cpu's big ship, write to board
    compShipBigCoords = cpuShipBigCoords()
    cpuBoard = placeShip(blankBoard, compShipBigCoords, 'B')

    #get coords of cpu's small ship, write to board
    compShipSmallCoords = cpuShipSmallCoords(cpuBoard)
    cpuBoard = placeShip(cpuBoard, compShipSmallCoords, 'S')
    
    ###displayBoard(cpuBoard, 'Computer\'s')

    blankBoard = ['_'] * 25
    cpuDisplayBoard = ['_'] * 25

    #player places big ship
    playerShipBigCoords = placePlayerShipBigCoords()
    playerBoard = placeShip(blankBoard, playerShipBigCoords, 'B')
    
    #player places small ship
    playerShipSmallCoords = placePlayerShipSmallCoords(playerBoard)
    playerBoard = placeShip(playerBoard, playerShipSmallCoords, 'S')

    time.sleep(1)
    displayBoard(playerBoard, 'Your')
    time.sleep(2)
    print('Your boats are set! Prepare for battle!')
    time.sleep(2)

    #determines order
    turn = chooseOrder()
    if turn == 'cpu':
        print('The winds favor Winston. He attacks first!')
        time.sleep(2)
    else:
        print('The sun is in Winston\'s eyes. You have the advantage! Attack!')
        time.sleep(2)

    playerWin = False
    cpuWin = False

    gameIsRunning = True
    cpuTurnCounter = 0
    roundCounter = 1

    #This is the player and computer's turn exchange loop
    while gameIsRunning == True:
        print('Round ' + str(roundCounter))
        roundCounter = roundCounter + 1

        #skip players turn for testing
        ###if turn == 'player':
            ###print('Skipping player\'s turn.')
            ###turn = 'cpu'

        #player's turn
        if turn == 'player':
            print('It\'s your turn!')
            time.sleep(1)
            cpuDisplayBoard == compBoardHider(cpuBoard)
            displayBoard(cpuDisplayBoard, 'Winston\'s')
            time.sleep(1)
            playersAttackNumber = getPlayerAttack(cpuBoard)
            result = checkAttackResult(playersAttackNumber, cpuBoard)

            if result == 'big':
                print('It\'s a hit!')
                time.sleep(1)
                compShipBigHitCount = compShipBigHitCount + 1
                if compShipBigHitCount == 3:

                    for i in compShipBigCoords:
                        cpuBoard[i] = '#'

                    print('You sunk his big boat!')
                    time.sleep(1)
                    cpuDisplayBoard = compBoardHider(cpuBoard)
                    displayBoard(cpuDisplayBoard, 'Winston\'s')

                else:
                    cpuBoard[playersAttackNumber] = '!'
                    cpuDisplayBoard = compBoardHider(cpuBoard)
                    displayBoard(cpuDisplayBoard, 'Winston\'s')

            if result == 'small':
                print('It\'s a hit!')
                time.sleep(1)
                compShipSmallHitCount = compShipSmallHitCount + 1
                if compShipSmallHitCount == 2:

                    for i in compShipSmallCoords:
                        cpuBoard[i] = '#'

                    print('You sunk his small ship!')
                    time.sleep(1)
                    cpuDisplayBoard = compBoardHider(cpuBoard)
                    displayBoard(cpuDisplayBoard, 'Winston\'s')

                else:
                    cpuBoard[playersAttackNumber] = '!'
                    cpuDisplayBoard = compBoardHider(cpuBoard)
                    displayBoard(cpuDisplayBoard, 'Winston\'s')


            if result == 'miss':
                print('You missed!')
                time.sleep(1)
                cpuBoard[playersAttackNumber] = 'X'
                cpuDisplayBoard = compBoardHider(cpuBoard)
                displayBoard(cpuDisplayBoard, 'Winston\'s')

            if compShipSmallHitCount + compShipBigHitCount == 5:
                playerWin = True
            else:
                turn = 'cpu'

        if playerWin == True:
            break

        #computer's turn
        ###print('Cpu turn #' + str(cpuTurnCounter))

        if turn == 'cpu':

            print('It\'s Winston\'s turn!')
            time.sleep(1)
            displayBoard(playerBoard, 'Your')
            time.sleep(1)
            print('Winston attacks...')
            time.sleep(2)
            cpuTurnCounter = cpuTurnCounter + 1
            
            compAttackNumber = getCompAttack(playerBoard)
            ###print('Attack number: ' + str(compAttackNumber))
            result = checkAttackResult(compAttackNumber, playerBoard)

            if result == 'big':
                print('Winston hit your boat!')
                time.sleep(1)
                playerShipBigHitCount = playerShipBigHitCount + 1
                if playerShipBigHitCount == 3:

                    for i in playerShipBigCoords:
                        playerBoard[i] = '#'

                    print('Your big boat was sunk!')
                    displayBoard(playerBoard, 'Your')

                else:
                    playerBoard[compAttackNumber] = '!'
                    displayBoard(playerBoard, 'Your')

            if result == 'small':
                print('Winston hit your boat!')
                time.sleep(1)
                playerShipSmallHitCount = playerShipSmallHitCount + 1
                if playerShipSmallHitCount == 2:

                    for i in playerShipSmallCoords:
                        playerBoard[i] = '#'

                    print('Your small boat was sunk!')
                    displayBoard(playerBoard, 'Your')

                else:
                    playerBoard[compAttackNumber] = '!'
                    displayBoard(playerBoard, 'Your')

            if result == 'miss':
                print('Winston missed!')
                time.sleep(2)
                playerBoard[compAttackNumber] = 'X'
                displayBoard(playerBoard, 'Your')

            if playerShipSmallHitCount + playerShipBigHitCount == 5:
                cpuWin = True
            else:
                turn = 'player'

        if cpuWin == True:
            break

        print('Hit enter to begin the next turn.')
        forfeit = input()
        if forfeit == 'forfeit':
            cpuWin = True
            break
        else:
            continue

    ###if turn == 'player':
        ###print('Skipping CPU\'s turn.')
        ###turn = 'cpu'
        
    if cpuWin == True:
        print('Winston wins. Naturally.')
    else:
        print('You have defeated the great Winston! Well done!')

    playAgain = startNewGame()

if cpuWin == True:
    print('Winston shakes your hand, smirking slightly, and says "I look forward to our next match!" as he walks out the door.')
else:
    print('Winston begrudgingly shakes your hand, and says "Luck always favors a novice!" as he walks out the door.')


    
            





                
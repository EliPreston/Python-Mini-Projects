# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


def is_ascending(items):
    if len(items) < 2:
        return True
    
    index = 1
    while index < len(items):

        if items[index] <= items[index - 1]:
            return False
        index += 1
    return True

def riffle(items, out=True):
    riffledList = []
    if len(items) == 0:
        return riffledList
    
    i = 0
    j = int(len(items)/2)
    while j < len(items):
        if out:
            riffledList.append(items[i])
            riffledList.append(items[j])
        elif not(out):
            riffledList.append(items[j])
            riffledList.append(items[i])
        i += 1
        j += 1
    return riffledList


def only_odd_digits(n):
    for i in str(n):
        if int(i) % 2 == 0:
            return False
    return True


def is_cyclops(n):
    n = str(n)
    if n.count('0') > 1 or len(n) % 2 == 0:
        return False

    mid = len(n) // 2
    if n[mid] == '0':
        return True
    return False

def domino_cycle(tiles):

    if len(tiles) == 0:
        return True
    if len(tiles) == 1:
        if tiles[0][0] == tiles[0][1]:
            return True
        return False
    
    for i in range(1, len(tiles)):
        y = tiles[i-1]
        x = tiles[i]

        if y[1] != x[0]:
            return False
    
    if tiles[0][0] == tiles[len(tiles)-1][1]:
        return True
    return False


def colour_trio(colours):

    colourList = ['r', 'y', 'b']

    def combineColours(substr, colourList):
        if substr[0] == substr[1]:
            return substr[0]
        else:
            for colour in colourList:
                if not(colour in substr):
                    return colour
    
    while len(colours) > 1:

        intermediateColours = ''
        for i in range(1, len(colours)):
            current = colours[i-1:i+1]
            intermediateColours += combineColours(current, colourList)
        colours = intermediateColours
    
    return colours

def count_dominators(items):

    if len(items) == 0:
        return 0

    dominators = 0
    currentMax = items[-1]

    for i in range(len(items)-1, -1, -1):

        if items[i] >= currentMax:
            dominators += 1
            currentMax = items[i]

    return dominators


# def extract_increasing(digits):

# def words_with_letters(words, letters):

def taxi_zum_zum(moves):

    initialPos =[0, 0]
    moveDirectionIndex = 1

    for i in moves:
        if i == 'R':
            moveDirectionIndex += 1
            if moveDirectionIndex == 4:
                moveDirectionIndex = 0
        elif i == 'L':
            moveDirectionIndex -= 1
            if moveDirectionIndex == -1:
                moveDirectionIndex = 3

        elif i == 'F':
            if moveDirectionIndex == 1:
                initialPos[1] += 1
            elif moveDirectionIndex == 2:
                initialPos[0] += 1
            elif moveDirectionIndex == 0:
                initialPos[0] -= 1
            elif moveDirectionIndex == 3:
                initialPos[1] -= 1

    return (initialPos[0], initialPos[1])


def give_change(amount, coins):
    
    coinsNeeded = []

    for i in coins:

        x = amount // i
        if x > 0:
            amount -= (x*i)
            for coin in range(x):
                coinsNeeded.append(i)
    return coinsNeeded

# def safe_squares_rooks(n, rooks):


def winning_card(cards, trump=None):    

    ranks = {
        'two': 2, 'three': 3, 'four': 4, 
        'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9, 'ten': 10, 
        'jack': 11, 'queen': 12, 'king': 13, 
        'ace': 14
        }

    currentWinner = cards[0]
    currentWinnerRank = ranks[cards[0][0]]

    if trump == None:
        trump = cards[0][1]
    else:
        trumpNotFound = True
        for i in range(len(cards)):
            if cards[i][1] == trump:
                currentWinner = cards[i]
                currentWinnerRank = ranks[cards[i][0]]
                trumpNotFound = False
                break
        if trumpNotFound:
            trump = currentWinner[1]

    for i in cards:
        currentRank = ranks[i[0]]
        currentSuit = i[1]

        if currentSuit == trump:
            if currentRank > currentWinnerRank:
                currentWinner = i
                currentWinnerRank = currentRank
        
    return currentWinner

# def knight_jump(knight, start, end):

# def seven_zero(n):
    



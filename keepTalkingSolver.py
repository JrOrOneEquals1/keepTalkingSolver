wordDict = {"ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"],
            "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
            "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"],
            "blank": ["wait", "right", "okay", "middle", "blank"],
            "nothing": ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"],
            "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"],
            "what": ["uhhh", "what"],
            "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"],
            "left": ["right", "left"],
            "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"],
            "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"],
            "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"],
            "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"],
            "press": ["right", "middle", "yes", "ready", "press"],
            "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"],
            "you are": ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"],
            "your": ["uh uh", "you are", "uh huh", "your"],
            "you're": ["you", "you're"],
            "ur": ["done", "u", "ur"],
            "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"],
            "uh huh": ["uh huh"],
            "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh"],
            "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"],
            "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
            "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"],
            "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"],
            "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"],
            "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"]}
wordNums = {"yes": 'Middle left: ',
            "first": 'Top right: ',
            "display": 'Bottom right: ',
            "okay": 'Top right: ',
            "says": 'Bottom right: ',
            "nothing": 'Middle left: ',
            "": 'Bottom left: ',
            "blank": 'Middle right: ',
            "no": 'Bottom right: ',
            "led": 'Middle left: ',
            "lead": 'Bottom right: ',
            "read": 'Middle right: ',
            "red": 'Middle right: ',
            "reed": 'Bottom left: ',
            "leed": 'Bottom left: ',
            "hold on": 'Bottom right: ',
            "you": 'Middle right: ',
            "you are": 'Bottom right: ',
            "your": 'Middle right: ',
            "you're": 'Middle right: ',
            "ur": 'Top left: ',
            "there": 'Bottom right: ',
            "they're": 'Bottom left: ',
            "their": 'Middle right: ',
            "they are": 'Middle left: ',
            "see": 'Bottom right: ',
            "c": 'Top right: ',
            "cee": 'Bottom right: '}
flashList = {'vowel': {0: {'red': 'blue',
                           'blue': 'red',
                           'green': 'yellow',
                           'yellow': 'green'},
                       1: {'red': 'yellow',
                           'blue': 'green',
                           'green': 'blue',
                           'yellow': 'red'},
                       2: {'red': 'green',
                           'blue': 'red',
                           'green': 'yellow',
                           'yellow': 'blue'}},
             "no vowel": {0: {'red': 'blue',
                              'blue': 'yellow',
                              'green': 'green',
                              'yellow': 'red'},
                          1: {'red': 'red',
                              'blue': 'blue',
                              'green': 'yellow',
                              'yellow': 'green'},
                          2: {'red': 'yellow',
                              'blue': 'green',
                              'green': 'blue',
                              'yellow': 'red'}}}
morseList = {'12': 'a',
             '2111': 'b',
             '2121': 'c',
             '211': 'd',
             '1': 'e',
             '1121': 'f',
             '221': 'g',
             '1111': 'h',
             '11': 'i',
             '1222': 'j',
             '212': 'k',
             '1211': 'l',
             '22': 'm',
             '21': 'n',
             '222': 'o',
             '1221': 'p',
             '2212': 'q',
             '121': 'r',
             '111': 's',
             '2': 't',
             '112': 'u',
             '1112': 'v',
             '122': 'w',
             '2112': 'x',
             '2122': 'y',
             '2211': 'z'}
morseFreq = {'shell': '3.505',
             'halls': '3.515',
             'trick': '3.522',
             'slick': '3.532',
             'boxes': '3.535',
             'leaks': '3.542',
             'strobe': '3.545',
             'bistro': '3.552',
             'flick': '3.555',
             'bombs': '3.565',
             'break': '3.572',
             'brick': '3.575',
             'steak': '3.582',
             'sting': '3.592',
             'vector': '3.595',
             'beats': '3.600'}

symbolList = [['o', 'a', 'y', 'lightning', 'weird', 'h', 'backwards c'], ['e', 'o', 'backwards c', 'swirl', 'empty star', 'h', 'q mark'], ['copy', 'butt', 'swirl', 'k', 'r', 'y', 'empty star'], ['g', 'p', 'b', 'weird', 'k', 'q mark', 'smiley'], ['trident', 'smiley', 'b', 'c', 'p', 'snake', 'star'], ['g', 'e', 'puzzle', 'ae', 'trident', 'n', 'omega']]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
even = ['0', '2', '4', '6', '8']
odd = ['1', '3', '5', '7', '9']
vowels = ['a', 'e', 'i', 'o', 'u']
global red, blue, black
red = [['c'], ['b'], ['a'], ['a', 'c'], ['b'], ['a', 'c'], ['a', 'b', 'c'], ['a', 'b'], ['b']]
blue = [['b'], ['a', 'c'], ['b'], ['a'], ['b'], ['b', 'c'], ['c'], ['a', 'c'], ['a']]
black = [['a', 'b', 'c'], ['a', 'c'], ['b'], ['a', 'c'], ['b'], ['b', 'c'], ['a', 'b'], ['c'], ['c']]
firstLetters = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'l', 'n', 'o', 'p', 'r', 's', 't', 'w']

ports = input('Is there a parallel port? ').lower()
litIndicators = input("What are the lit indicators? ").lower().split(' ')
batteries = int(input('How many batteries? '))
serial = input('What is the serial number? ').lower()

parallelPort = False
hasVowel = False
serialList = list(serial)

if 'y' in ports:
    parallelPort = True

for char in serialList:
    if char in even:
        lastDigitEven = True
    elif char in odd:
        lastDigitEven = False
    elif char in vowels:
        hasVowel = True

def who():
    while True:
        try:
            print(wordDict[input(wordNums[input('First word: ')])])
            break
        except KeyError:
            print('That is not a valid word')
    while True:
        try:
            print(wordDict[input(wordNums[input('First word: ')])])
            break
        except KeyError:
            print('That is not a valid word')
    while True:
        try:
            print(wordDict[input(wordNums[input('First word: ')])])
            break
        except KeyError:
            print('That is not a valid word')

def wire():
    colors = list(input("Enter colors without spaces (r=red, w=white, b=blue, y=yellow, d=black): "))
    if len(colors) == 3:
        if 'r' not in colors:
            print('second')
        elif colors[2] == 'w':
            print('last')
        elif colors.count('b') > 1:
            print('last blue')
        else:
            print('last')
    elif len(colors) == 4:
        if colors.count('r') > 1 and not lastDigitEven:
            print('last red')
        elif colors[3] == 'y' and colors.count('r') == 0 or colors.count('b') == 1:
            print('first')
        elif colors.count('y') > 1:
            print('last')
        else:
            print('first')
    elif len(colors) == 5:
        if colors[4] == 'd' and not lastDigitEven:
            print('fourth')
        elif colors.count('r') == 1 and colors.count('y') > 1:
            print('first')
        elif colors.count('d') == 0:
            print('second')
        else:
            print('first')
    elif len(colors) == 6:
        if colors.count('y') == 0 and not lastDigitEven:
            print('third')
        elif colors.count('y') == 1 and colors.count('w') > 1:
            print('fourth')
        elif colors.count('r') == 0:
            print('last')
        else:
            print('fourth')

def hold():
    print('hold')
    print('Blue: 4')
    print('Yellow: 5')
    print('Otherwise: 1')

def button():
    answer = input('Full color and word: ').lower().split()
    color = answer[0]
    word = answer[1]
    if color == 'blue' and word == 'abort':
        hold()
    elif batteries > 1 and word == 'detonate':
        print('release')
    elif color == 'white' and 'car' in litIndicators:
        hold()
    elif batteries > 2 and 'frk' in litIndicators:
        print('release')
    elif color == 'yellow':
        hold()
    elif color == 'red' and word == 'hold':
        print('release')
    else:
        hold()

def order(li, symbols):
    for item in li:
        if item in symbols:
            print(item, end=' ')
    print()

def symbol():
    first = input('First symbol: ')
    second = input('Second symbol: ')
    third = input('Third symbol: ')
    fourth = input('Fourth symbol: ')
    symbols = [first, second, third, fourth]
    for li in symbolList:
        count = 0
        for item in li:
            if item in symbols:
                count += 1
        if count == 4:
            order(li, symbols)

def simon():
    print("Enter 'done' when you are done")
    while True:
        flashes = input('What are the full flash colors? ').split(' ')
        if flashes == 'done':
            break
        strikes = input('How many strikes? ')
        vowel = 'no vowel'
        if hasVowel:
            vowel = 'vowel'
        for color in flashes:
            print(flashList[vowel][int(strikes)][color], end=' ')
        print()

def memory():
    positions = []
    numbers = []
    display = int(input("What is the display number? "))
    if display == 1 or display == 2:
        print('Pos 2')
        positions.append(2)
        numbers.append(input('What was the number? '))
    elif display == 3:
        print('Pos 3')
        positions.append(3)
        numbers.append(input('What was the number? '))
    elif display == 4:
        print('Pos 4')
        positions.append(4)
        numbers.append(input('What was the number? '))


    display = int(input("What is the display number? "))
    if display == 1:
        print('Num 4')
        numbers.append(4)
        positions.append(input('What was the position? '))
    elif display == 2 or display == 4:
        print('Pos ' + str(positions[0]))
        positions.append(positions[0])
        numbers.append(input('What was the number? '))
    elif display == 3:
        print('Pos 1')
        positions.append(1)
        numbers.append(input('What was the number? '))


    display = int(input("What is the display number? "))
    if display == 1:
        print('Num ' + str(numbers[1]))
        numbers.append(numbers[1])
        positions.append(input('What was the position? '))
    elif display == 2:
        print('Num ' + str(numbers[0]))
        numbers.append(numbers[0])
        positions.append(input('What was the position? '))
    elif display == 3:
        print('Pos 3')
        positions.append(3)
        numbers.append(input('What was the number? '))
    elif display == 4:
        print('Num 4')
        numbers.append(4)
        positions.append(input('What was the position? '))


    display = int(input("What is the display number? "))
    if display == 1:
        print('Pos ' + str(positions[0]))
        numbers.append(input('What was the number? '))
    elif display == 2:
        print('Pos 1')
        numbers.append(input('What was the number? '))
    elif display == 3 or display == 4:
        print('Pos ' + str(positions[1]))
        numbers.append(input('What was the number? '))


    display = int(input("What is the display number? "))
    if display == 1:
        print('Num ' + str(numbers[0]))
    elif display == 2:
        print('Num ' + str(numbers[1]))
    elif display == 3:
        print('Num ' + str(numbers[3]))
    elif display == 4:
        print('Num ' + str(numbers[2]))

def morse():
    morseCode = input('What is the morse code in 1\'s (short) and 2\'s (long)? ').split(' ')
    word = ''
    for letter in morseCode:
        word += morseList[letter]
    try:
        print(morseFreq[word])
    except KeyError:
        print('Unknown word: ' + word)
        print(morseFreq)

def getComplicatedCut(wireInfo):
    if 'n' in wireInfo:
        return 'c'
    elif 'r' in wireInfo and 'b' in wireInfo and 's' in wireInfo and 'l' in wireInfo:
        return 'd'
    elif 'r' in wireInfo and 'b' in wireInfo and 's' in wireInfo:
        return 'p'
    elif 'r' in wireInfo and 'b' in wireInfo and 'l' in wireInfo:
        return 's'
    elif 'r' in wireInfo and 's' in wireInfo and 'l' in wireInfo:
        return 'b'
    elif 'b' in wireInfo and 'l' in wireInfo and 's' in wireInfo:
        return 'p'
    elif 'r' in wireInfo and 's' in wireInfo:
        return 'c'
    elif 'r' in wireInfo and 'l' in wireInfo:
        return 'b'
    elif 'r' in wireInfo and 'b' in wireInfo:
        return 's'
    elif 's' in wireInfo and 'l' in wireInfo:
        return 'b'
    elif 'b' in wireInfo and 's' in wireInfo:
        return 'd'
    elif 'b' in wireInfo and 'l' in wireInfo:
        return 'p'
    elif 'r' in wireInfo:
        return 's'
    elif 'b' in wireInfo:
        return 's'
    elif 'l' in wireInfo:
        return 'd'
    elif 's' in wireInfo:
        return 'c'
    else:
        print('You are missing that one')
        return 'dk'

def complicated():
    wires = int(input('How many wires? '))
    for i in range(wires):
        wireInfo = input('Enter wire info (r=red, b=blue, s=star, l=led, n=none): ').split()
        cut = getComplicatedCut(wireInfo)
        if cut == 'c':
            print('cut')
        elif cut == 'd':
            print("don't cut")
        elif cut == 's':
            if lastDigitEven:
                print('cut')
            else:
                print("don't cut")
        elif cut == 'p':
            if parallelPort:
                print('cut')
            else:
                print("don't cut")
        elif cut == 'b':
            if batteries > 1:
                print('cut')
            else:
                print("don't cut")
        else:
            print('Don\'t know')

def sequences():
    global red, blue, black
    redNum = 0
    blueNum = 0
    blackNum = 0
    print('Enter \'done\' when you are done')
    while True:
        answer = input("Enter full color and letter: ")
        if answer == 'done':
            break
        answer = answer.split(' ')
        color = answer[0]
        letter = answer[1]
        if color == 'red':
            if letter in red[redNum]:
                print('cut')
            else:
                print("don't cut")
            redNum += 1
        elif color == 'blue':
            if letter in blue[blueNum]:
                print('cut')
            else:
                print("don't cut")
            blueNum += 1
        elif color == 'black':
            if letter in black[blackNum]:
                print('cut')
            else:
                print("don't cut")
            blackNum += 1

mazeMove1 = {'11': 'rd',
             '12': 'ud',
             '13': 'ud',
             '14': 'ud',
             '15': 'rud',
             '16': 'ru',
             '21': 'rl',
             '22': 'rd',
             '23': 'ru',
             '24': 'r',
             '25': 'rl',
             '26': 'l',
             '31': 'ld',
             '32': 'lu',
             '33': 'ld',
             '34': 'lur',
             '35': 'ld',
             '36': 'ru',
             '41': 'rd',
             '42': 'ru',
             '43': 'rd',
             '44': 'lu',
             '45': 'rd',
             '46': 'ul',
             '51': 'rl',
             '52': 'rl',
             '53': 'rl',
             '54': 'r',
             '55': 'l',
             '56': 'r',
             '61': 'l',
             '62': 'ld',
             '63': 'uld',
             '64': 'lud',
             '65': 'ud',
             '66': 'lu'}
mazeMove2 = {'11': 'r',
             '12': 'rd',
             '13': 'ud',
             '14': 'urd',
             '15': 'ud',
             '16': 'u',
             '21': 'uld',
             '22': 'lu',
             '23': 'dr',
             '24': 'lu',
             '25': 'd',
             '26': 'ur',
             '31': 'l',
             '32': 'rrd',
             '33': 'lu',
             '34': 'dr',
             '35': 'ud',
             '36': 'ul',
             '41': 'rd',
             '42': 'lu',
             '43': 'rdr',
             '44': 'lu',
             '45': 'rd',
             '46': 'ru',
             '51': 'lrd',
             '52': 'ru',
             '53': 'lr',
             '54': 'd',
             '55': 'lu',
             '56': 'lr',
             '61': 'l',
             '62': 'ld',
             '63': 'lud',
             '64': 'ud',
             '65': 'ud',
             '66': 'lu'}
mazeMove3 = {'11': 'rdr',
             '12': 'u',
             '13': 'rd',
             '14': 'ud',
             '15': 'ud',
             '16': 'ru',
             '21': 'lr',
             '22': 'd',
             '23': 'lud',
             '24': 'ud',
             '25': 'ru',
             '26': 'lr',
             '31': 'ld',
             '32': 'ud',
             '33': 'ud',
             '34': 'ud',
             '35': 'ul',
             '36': 'lr',
             '41': 'd',
             '42': 'ru',
             '43': 'rd',
             '44': 'ud',
             '45': 'ud',
             '46': 'lu',
             '51': 'rd',
             '52': 'ul',
             '53': 'ld',
             '54': 'ud',
             '55': 'ud',
             '56': 'ru',
             '61': 'ld',
             '62': 'ud',
             '63': 'ud',
             '64': 'ud',
             '65': 'ud',
             '66': 'lu'}
mazeMove4 = {'11': 'rd',
             '12': 'ud',
             '13': 'ud',
             '14': 'ud',
             '15': 'rud',
             '16': 'ur',
             '21': 'ld',
             '22': 'ud',
             '23': 'ru',
             '24': 'r',
             '25': 'rl',
             '26': 'rl',
             '31': 'r',
             '32': 'dr',
             '33': 'ul',
             '34': 'rl',
             '35': 'lr',
             '36': 'l',
             '41': 'lr',
             '42': 'lr',
             '43': 'rd',
             '44': 'lud',
             '45': 'lr',
             '46': 'r',
             '51': 'lr',
             '52': 'lr',
             '53': 'l',
             '54': 'lr',
             '55': 'ld',
             '56': 'ul',
             '61': 'ld',
             '62': 'lud',
             '63': 'ud',
             '64': 'uld',
             '65': 'ud',
             '66': 'u'}
mazeMove5 = {'11': 'r',
             '12': 'rd',
             '13': 'rud',
             '14': 'ud',
             '15': 'ud',
             '16': 'u',
             '21': 'rl',
             '22': 'rl',
             '23': 'ld',
             '24': 'ur',
             '25': 'rr',
             '26': 'ur',
             '31': 'lr',
             '32': 'lr',
             '33': 'r',
             '34': 'lr',
             '35': 'lr',
             '36': 'lr',
             '41': 'lr',
             '42': 'lrd',
             '43': 'ul',
             '44': 'ld',
             '45': 'rlu',
             '46': 'rl',
             '51': 'lrd',
             '52': 'ul',
             '53': 'rd',
             '54': 'u',
             '55': 'l',
             '56': 'lr',
             '61': 'ld',
             '62': 'u',
             '63': 'ld',
             '64': 'ud',
             '65': 'ud',
             '66': 'ul'}
mazeMove6 = {'11': 'd',
             '12': 'ud',
             '13': 'udr',
             '14': 'ur',
             '15': 'dr',
             '16': 'ur',
             '21': 'rd',
             '22': 'ud',
             '23': 'ul',
             '24': 'ld',
             '25': 'ul',
             '26': 'lr',
             '31': 'ld',
             '32': 'ud',
             '33': 'u',
             '34': 'rd',
             '35': 'u',
             '36': 'lr',
             '41': 'r',
             '42': 'rd',
             '43': 'ud',
             '44': 'udl',
             '45': 'ud',
             '46': 'ul',
             '51': 'lrd',
             '52': 'ul',
             '53': 'dr',
             '54': 'ud',
             '55': 'ur',
             '56': 'r',
             '61': 'ld',
             '62': 'ud',
             '63': 'ul',
             '64': 'd',
             '65': 'dlu',
             '66': 'ul'}
mazeMove7 = {'11': 'rd',
             '12': 'ud',
             '13': 'ur',
             '14': 'rd',
             '15': 'ud',
             '16': 'ur',
             '21': 'lr',
             '22': 'rd',
             '23': 'ul',
             '24': 'ld',
             '25': 'u',
             '26': 'lr',
             '31': 'lr',
             '32': 'l',
             '33': 'rd',
             '34': 'rud',
             '35': 'ur',
             '36': 'lr',
             '41': 'ld',
             '42': 'ur',
             '43': 'l',
             '44': 'lr',
             '45': 'lr',
             '46': 'lr',
             '51': 'rd',
             '52': 'ul',
             '53': 'rd',
             '54': 'ul',
             '55': 'ld',
             '56': 'lru',
             '61': 'ld',
             '62': 'ud',
             '63': 'ul',
             '64': 'd',
             '65': 'ud',
             '66': 'ul'}
mazeMove8 = {'11': 'd',
             '12': 'urd',
             '13': 'ud',
             '14': 'ud',
             '15': 'ud',
             '16': 'ur',
             '21': 'rd',
             '22': 'lru',
             '23': 'rd',
             '24': 'ur',
             '25': 'd',
             '26': 'ulr',
             '31': 'lr',
             '32': 'l',
             '33': 'lr',
             '34': 'dl',
             '35': 'ur',
             '36': 'lr',
             '41': 'ld',
             '42': 'ur',
             '43': 'lr',
             '44': 'r',
             '45': 'lr',
             '46': 'lr',
             '51': 'rd',
             '52': 'ul',
             '53': 'ld',
             '54': 'lur',
             '55': 'lr',
             '56': 'lr',
             '61': 'ld',
             '62': 'ud',
             '63': 'ud',
             '64': 'ur',
             '65': 'l',
             '66': 'l'}
mazeMove9 = {'11': 'd',
             '12': 'ud',
             '13': 'urd',
             '14': 'ud',
             '15': 'ud',
             '16': 'ur',
             '21': 'rd',
             '22': 'ud',
             '23': 'lur',
             '24': 'd',
             '25': 'ud',
             '26': 'ul',
             '31': 'lr',
             '32': 'rd',
             '33': 'ul',
             '34': 'rd',
             '35': 'ud',
             '36': 'ul',
             '41': 'lr',
             '42': 'l',
             '43': 'rd',
             '44': 'ul',
             '45': 'rd',
             '46': 'ul',
             '51': 'ldr',
             '52': 'ud',
             '53': 'ul',
             '54': 'r',
             '55': 'ld',
             '56': 'ru',
             '61': 'ld',
             '62': 'ud',
             '63': 'ud',
             '64': 'udl',
             '65': 'u',
             '66': 'l'}

def maze():
    column1 = int(input('Enter the first circle\'s column (1-6): '))
    column2 = int(input('Enter the second circle\'s column (1-6): '))
    column3 = int(input('Enter the triangle\'s column (1-6): '))
    row3 = int(input('Enter the triangle\'s row (1-6): '))
    column4 = int(input('Enter the square\'s column (1-6): '))
    row4 = int(input('Enter the square\'s row (1-6): '))
    if column1 in [1, 6] and column2 in [1, 6] and column1 != column2:
        maze = dict(mazeMove1)
    elif column1 in [2, 5] and column2 in [2, 5] and column1 != column2:
        maze = dict(mazeMove2)
    elif column1 in [4, 6] and column2 in [4, 6] and column1 != column2:
        maze = dict(mazeMove3)
    elif column1 == 1 and column2 == 1:
        maze = dict(mazeMove4)
    elif column1 in [4, 5] and column2 in [4, 5] and column1 != column2:
        maze = dict(mazeMove5)
    elif column1 in [3, 5] and column2 in [3, 5] and column1 != column2:
        maze = dict(mazeMove6)
    elif column1 == 2 and column2 == 2:
        maze = dict(mazeMove7)
    elif column1 in [3, 4] and column2 in [3, 4] and column1 != column2:
        maze = dict(mazeMove8)
    elif column1 in [1, 3] and column2 in [1, 3] and column1 != column2:
        maze = dict(mazeMove9)
    path = []
    backLocs = []
    moved = False
    startLoc = str(column4) + str(row4)
    endLoc = str(column3) + str(row3)
    currentLoc = startLoc
    while currentLoc != endLoc:
        moves = list(maze[currentLoc])
        if 'r' in moves:
            moved = True
            newList = list(maze[currentLoc])
            newList.remove('r')
            maze[currentLoc] = ''.join(newList)
            moves.remove('r')
            if len(moves) > 0:
                backLocs.append([currentLoc, path[:]])
            path.append('r')
            currentLoc = str(int(currentLoc) + 10)
            newList = list(maze[currentLoc])
            try:
                newList.remove('l')
            except:
                pass
            maze[currentLoc] = ''.join(newList)
        if 'l' in moves and not moved:
            moved = True
            newList = list(maze[currentLoc])
            newList.remove('l')
            maze[currentLoc] = ''.join(newList)
            moves.remove('l')
            if len(moves) > 0:
                backLocs.append([currentLoc, path[:]])
            path.append('l')
            currentLoc = str(int(currentLoc) - 10)
            newList = list(maze[currentLoc])
            try:
                newList.remove('r')
            except:
                pass
            maze[currentLoc] = ''.join(newList)
        if 'd' in moves and not moved:
            moved = True
            newList = list(maze[currentLoc])
            newList.remove('d')
            maze[currentLoc] = ''.join(newList)
            moves.remove('d')
            if len(moves) > 0:
                backLocs.append([currentLoc, path[:]])
            path.append('d')
            currentLoc = str(int(currentLoc) + 1)
            newList = list(maze[currentLoc])
            try:
                newList.remove('u')
            except:
                pass
            maze[currentLoc] = ''.join(newList)
        if 'u' in moves and not moved:
            moved = True
            newList = list(maze[currentLoc])
            newList.remove('u')
            maze[currentLoc] = ''.join(newList)
            moves.remove('u')
            if len(moves) > 0:
                backLocs.append([currentLoc, path[:]])
            path.append('u')
            currentLoc = str(int(currentLoc) - 1)
            newList = list(maze[currentLoc])
            try:
                newList.remove('d')
            except:
                pass
            maze[currentLoc] = ''.join(newList)
        if not moved:
            try:
                currentLoc = backLocs[-1][0]
                path = backLocs[-1][1][:]
                backLocs.pop()
            except:
                currentLoc = startLoc
                path = []
        moved = False
    pathWords = ''
    for ele in path:
        if ele == 'r':
            pathWords += 'right '
        elif ele == 'l':
            pathWords += 'left '
        elif ele == 'u':
            pathWords += 'up '
        elif ele == 'd':
            pathWords += 'down '
    print(pathWords)

def password():
    letters = []
    print('Say \'done\' to exit')
    while True:
        firstLetter = input('What is the first letter? ').lower()
        if firstLetter == 'done':
            break
        if firstLetter not in firstLetters:
            print('change first')
            continue
        if firstLetter == 'a':
            print('about after again')
        elif firstLetter == 'b':
            print('below')
        elif firstLetter == 'c':
            print('could')
        elif firstLetter == 'e':
            print('every')
        elif firstLetter == 'f':
            print('first found')
        elif firstLetter == 'g':
            print('great')
        elif firstLetter == 'h':
            print('house')
        elif firstLetter == 'l':
            print('large learn')
        elif firstLetter == 'n':
            print('never')
        elif firstLetter == 'o':
            print('other')
        elif firstLetter == 'p':
            print('place plant point')
        elif firstLetter == 'r':
            print('right')
        elif firstLetter == 's':
            print('small sound spell still study')
        elif firstLetter == 't':
            print('their there these thing think three')
        elif firstLetter == 'w':
            print('water where which world would write')

def knob():
    positions = input('Enter the lit positions, without spaces, top row then bottom row, left to right (1=off, 2=on): ')
    if positions == '112122222212' or positions == '212121122122':
        print('up')
    elif positions == '122112222212' or positions == '212121121112':
        print('down')
    elif positions == '111121211222' or positions == '111121111221':
        print('left')
    elif positions == '212222222121' or positions == '212211222121':
        print('right')

while True:
    module = input("What module? ").lower()
    if module.startswith('who'):
        who()
    elif module.startswith('wire'):
        wire()
    elif module.startswith('butt'):
        button()
    elif module.startswith('sym'):
        symbol()
    elif module.startswith('sim'):
        simon()
    elif module.startswith('mem'):
        memory()
    elif module.startswith('mor'):
        morse()
    elif module.startswith('comp'):
        complicated()
    elif module.startswith('seq'):
        sequences()
    elif module.startswith('maz'):
        maze()
    elif module.startswith('pas'):
        password()
    elif module.startswith('kno'):
        knob()
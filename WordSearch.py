import string
import random
import urllib.request

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
size = 14
num_rows = size
num_cols = size
num_words = 20
used = []

def createRandom():
  board=[[random.choice(string.ascii_uppercase) for j in range(num_cols)] for i in range(num_rows)]

  return board;


def createNotRandom():
  board = [["-" for j in range(num_cols)] for i in range(num_rows)]
  return board

def printBoard(board):
  for row in board:
      print(row)


def getWords(word_list):
  global num_words

  words = []
  while len(words) < num_words:
    word = random.choice(word_list)
    if(len(word) < 4):
      continue
    if(len(word) > 8):
      continue
    if(word in words):
      continue
    words.append(word)
  return words


def getWordList():
  global word_site
  global num_words  

  response = urllib.request.urlopen(word_site)
  txt = response.read().decode()
  words = txt.splitlines()
  return words 


def randomRightStart(word):
  x = random.randint(0,num_rows-1)
  y = random.randint(0,num_cols-1-len(word))
  print(x,y)
  return x,y
  

def addWordStraight(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpy+=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    y+=1
   
 # printBoard(board)
  return 0


def randomLeftStart(word):
  x = random.randint(0,num_rows-1)
  y = random.randint(len(word)-1,num_cols-1)
  print(x,y)
  return x,y
  


def addWordBackwords(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpy-=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    y-=1
   
  #printBoard(board)
  return 0


def randomDownStart(word):
  x = random.randint(0,num_rows-1-len(word))
  y = random.randint(0,num_cols-1)
  print(x,y)
  return x,y
  

  
def addWordDown(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpx+=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x+=1
   
  #printBoard(board)
  return 0


def randomUpStart(word):
  x = random.randint(len(word)-1,num_rows-1)
  y = random.randint(0,num_cols-1)
  print(x,y)
  return x,y
  


def addWordUp(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpx-=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x-=1
   
  #printBoard(board)
  return 0


def randomUpRightStart(word):
  x = random.randint(len(word)-1,num_rows-1)
  y = random.randint(0,num_cols-1-len(word))
  print(x,y)
  return x,y
  


def addWordUpRight(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpx-=1
    tmpy+=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x-=1
    y+=1
   
  #printBoard(board)
  return 0



def randomUpLeftStart(word):
  x = random.randint(len(word)-1,num_rows-1)
  y = random.randint(len(word)-1,num_cols-1)
  print(x,y)
  return x,y
  


def addWordUpLeft(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper != board[tmpx][tmpy]):
      return 1
    tmpx-=1
    tmpy-=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x-=1
    y-=1
   
  #printBoard(board)
  return 0


def randomDownLeftStart(word):
  x = random.randint(0,num_rows-1-len(word))
  y = random.randint(len(word)-1,num_cols-1)
  print(x,y)
  return x,y
  


def addWordDownLeft(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpx+=1
    tmpy-=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x+=1
    y-=1
   
  #printBoard(board)
  return 0


def randomDownRightStart(word):
  x = random.randint(0,num_rows-1-len(word))
  y = random.randint(0,num_cols-1-len(word))
  print(x,y)
  return x,y
  


def addWordDownRight(board, word, x, y):
  tmpx = x
  tmpy = y
  for letter in word:
    if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
      return 1
    tmpx+=1
    tmpy+=1

  for letter in word:
    board[x][y] = letter.upper()
    used.append([x,y])
    x+=1
    y+=1
   
  #printBoard(board)
  return 0

def addWord(board, word, num):
    if(num == 0):
      x,y = randomRightStart(word)
      val = addWordStraight(board, word, x, y)
    elif(num == 1):
      x,y = randomLeftStart(word)
      val = addWordBackwords(board, word, x, y)
    elif(num == 2):
      x,y = randomDownStart(word)
      val = addWordDown(board, word, x, y)
    elif(num == 3):
      x,y = randomUpStart(word)
      val = addWordUp(board, word, x, y)
    elif(num == 4):
      x,y = randomUpRightStart(word)
      val = addWordUpRight(board, word, x, y)
    elif(num == 5):
      x,y = randomUpLeftStart(word)
      val = addWordUpLeft(board, word, x, y)
    elif(num == 6):
      x,y = randomDownRightStart(word)
      val = addWordDownRight(board, word, x, y)
    elif(num == 7):
      x,y = randomDownLeftStart(word)
      val = addWordDownLeft(board, word, x, y)
    else:
      x,y = randomRightStart(word)
      val = addWordStraight(board, word, x, y)

    return val


def forceAddStraight(board, word):
  for i in range(num_rows):
    for j in range(num_cols-1-len(word)):
      tmpx = i
      tmpy = j
      tmpnum = 1
      for letter in word:
        if([tmpx,tmpy] in used and letter.upper() != board[tmpx][tmpy]):
          break
        tmpx+=1
        tmpnum+=1
      if(tmpnum == len(word)):
        x = i
        y = j
        for letter in word:
          board[x][y] = letter.upper()
          used.append([x,y])
          x+=1
        return 0
  print("Failed to force add straight :(")
  return 1


def forceAddRight(board, word):
  print("Attempting force add right")
  for i in range(num_rows):
    for j in range(num_cols-1-len(word)):
      val = addWordStraight(board, word, i, j)
      if (val == 0):
        return 0
  return 1


def forceAddDown(board, word):
  print("Attemping force add down")
  #x = random.randint(0,num_rows-1-len(word))
  #y = random.randint(0,num_cols-1)
  for i in range(num_rows-1-len(word)):
    for j in range(num_cols-1):
      val = addWordDown(board, word, i, j)
      if (val == 0):
        return 0
  return 1 


def forceAddDownRight(board, word):
  for i in range(num_rows-1-len(word)):
    for j in range(num_cols-1-len(word)):
      val = addWordDownRight(board, word, i, j)
      if (val == 0):
        return 0
  return 1


def forceAddSomewhere(board, word):
  print("Adding by force!")
  print(word)
  val = forceAddRight(board, word)
  if(val == 0):
    return 0
  val = forceAddDown(board, word)
  if(val == 0):
    return 0
  val = forceAddDownRight(board, word)
  if(val == 0):
    return 0
  return 1



def fillBoard(board, words):
  for word in words:
    print("adding word:")
    print(word)
    num = random.randint(0,7)
    val = addWord(board, word, num)
    attempt = 0
    while (val):
      attempt+=1
      if(attempt > 10):
        print("FAIL!!! - trying by force")
        val = forceAddSomewhere(board, word)
        printBoard(board)
        if(val):
          print("STILL FAILLLLLLLLL")
          printBoard(board)
          exit(0)
          return 1
        continue
      num = random.randint(0,7)
      val = addWord(board, word, num)
    print("ADDED!")
  printBoard(board)
  return 0


def regenRandomBoard(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      board[i][j] = random.choice(string.ascii_uppercase) 


def regenNotRandomBoard(board):
  print("board before...")
  printBoard(board)
  for i in range(len(board)):
    for j in range(len(board[i])):
      board[i][j] = "-"
  print("board after!!!")


def create(board, words):
  while(1):
    print(words)
    regenRandomBoard(board)
    printBoard(board)

    # Fill Board with Words
    val = fillBoard(board, words)
    if (val == 0):
      printBoard(board)
      return 0

    


## START ##
print("***** PROGRAM START! *****")
# Create Board
board = createRandom()
printBoard(board)

# Get Words
word_list = getWordList()
words = getWords(word_list)
print(words)

# Fill Board with Words
#fillBoard(board, words)

create(board, words)
print("SUCCESS")


 

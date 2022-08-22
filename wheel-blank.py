import numbers
from unicodedata import numeric
from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc
import random

players={0:{"Player 1":"","roundtotal":100,"gametotal":0},
         1:{"Player 2":"","roundtotal":1000,"gametotal":0},
         2:{"Player 3":"","roundtotal":1000,"gametotal":0},
        }

player1total = 0
player2total = 0
player3total = 0

#players.update({"roundtotal":5})
#players["roundtotal"] = 6 

roundNum = 0
dictionary = [] #list of words
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""


def read_dictionary_file():
    global dictionary
    d = open(r'dictionary.txt')
    dictionary = d.readlines()

def read_wheel_txt_file():
    global wheellist
    w = open(r'wheeldata.txt')
    wheellist = w.readlines()

    
def game_setup():
    # Read in File dictionary
    # Read in Turn Text Files
    global wheel_list
    global dictionary
        
    read_dictionary_file()
    read_wheel_txt_file()

def getWord():
    read_dictionary_file()
    global dictionary
    global blankWord
    global roundWord
    roundWord = random.choice(dictionary)
    blankWord = '_' * (len(roundWord)-1)
    print(blankWord)
    print(roundWord)
    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    #roundWord,roundUnderscoreWord
    return roundWord, blankWord


def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    global roundNum
    global player_order
    roundNum += 1
    print(f'Round {roundNum}')
    players[0].__setitem__("roundtotal", 0)
    players[1].__setitem__("roundtotal", 0)
    players[2].__setitem__("roundtotal", 0)

    initPlayer = random.choice(players)
    if initPlayer == players[0]: #my attempt at cycling by player
        player_order = [0, 1, 2]
    if initPlayer == players[1]:
        player_order = [1, 2, 0]
    if initPlayer == players[2]:
        player_order = [2, 0, 1]
    print(f'{initPlayer} is up first')

    getWord()
    return initPlayer

def spinWheel(playerNum):
    read_wheel_txt_file()
    global wheellist
    global players
    global vowels
    global blankWord
    spin_value = random.choice(wheellist)
    print(blankWord)
    while True:
        if spin_value == "bankrupt\n":
            players[playerNum-1].__setattr__("roundtotal", 0)
            print(f'Bankrupt! Your round total is now {players[playerNum-1].get("roundtotal")}')
            stillinTurn = False
            break
        elif int(spin_value):
            letter = input(f'For {spin_value} guess a consonant: ')
            if letter in vowels:
                print('Guess a consonant')
            elif letter in roundWord:
                index = roundWord.find(letter)
                blankWord = blankWord[:index] + letter + blankWord[index + 1:]
                print(blankWord)
                print(f'Good job! There were {roundWord.count(letter)} in the word')
                players[playerNum - 1].__setitem__("roundtotal", players[playerNum - 1].get("roundtotal")+ int(spin_value)*int(roundWord.count(letter)))
                print(f'Round total is now: {players[playerNum-1]}')
                stillinTurn =True
                break
            elif letter not in roundWord:
                print(f'There were no {letter} in the word.')
                stillinTurn = False
                break
        else:
            print('You lost a turn')
            stillinTurn = False
            break
   
    return stillinTurn

def buyVowel(playerNum):
    global players
    global vowels
    global blankWord

    players[playerNum - 1].__setitem__("roundtotal", players[playerNum - 1].get("roundtotal") - vowelcost)
    print(f'{players[playerNum - 1]}')
   
    while True:
        guess_vowel = input('What vowel would you like to buy? ')
        if guess_vowel in roundWord and guess_vowel in vowels:
            print(f'Good job! There were {roundWord.count(guess_vowel)} in the word')
            index = roundWord.find(guess_vowel)
            blankWord = blankWord[:index] + guess_vowel + blankWord[index + 1:]
            print(blankWord)
            stillinTurn = True
            break
        elif guess_vowel not in vowels:
            print('That is not a vowel')
        else:
            print('Vowel is not in word')
            stillinTurn = False
    return stillinTurn


def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    word_guess=input('What is your guess for the word?')
    print(roundWord)
    while True: 
        if word_guess in roundWord: #I know it should be "is" not "in" but the guesses are never correct with "is" :(
            print(f'Congrats. You got it right and won the round! {roundWord} was the word')
            players[playerNum - 1].__setitem__("gametotal", players[playerNum - 1].get("roundtotal"))
            print(players[playerNum-1])
            round_end = True
            False
            break
        else:
            print('Sorry. Your guess was incorrect')
            break

    return False, round_end


def wofTurn(playerNum):  
    wofRoundSetup()
    global roundWord
    global blankWord
    global turntext
    global players

    stillinTurn = True
    while stillinTurn:
        print('S = spin the wheel, B = buy a vowel, G = guess the word')
        choice = input('What would you like to do? ')    
    
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            print("Not a correct option") 
            while stillinTurn == False:
                players[playerNum]
                print(f'{players[playerNum]} is now up to guess')
                stillinTurn == True
   
#I can't figure out how to cycle through players
#Also couldn't figure out switching rounds after a correct guess
#Really burnt myself out over this whole project. Dissapointed in myself to say the least.
wofTurn(1) #run this to see what all I could come up with











# def wofRound():
#     global players
#     global round_end
#     global playerNum
#     initPlayer = wofRoundSetup()
#     while round_end == False:
#         print(f'{players[playerNum]} won that round')
   

# def wofFinalRound():
#     global roundWord
#     global blankWord
#     global finalroundtext
#     winplayer = 0
#     amount = 0
    
    # Find highest gametotal player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    # If they do, add finalprize and gametotal and print out that the player won 


# def main():
#     game_setup()    

#     for i in range(0,maxrounds):
#         if i in [0,1]:
#             wofRound()
#         else:
#             wofFinalRound()

# if __name__ == "__main__":
#     main()
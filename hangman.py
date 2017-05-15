#Author: Steven Draugel
#hangman.py
#Purpose: To play hangman.
#Certification of Authenticity: I certify that this is entirely my own work.

from random import randint
from graphics import *

def newGameQuestion(height, width, win):
    #Yes and No buttons for the continue screen.
    text = Text(Point(width / 2, height - 150), "Would you like to play again?")
    text.setTextColor("yellow")
    text.setSize(36)
    text.draw(win)

    yesButton = Rectangle(Point(290, height - 100), Point(440, height - 50))
    yesButton.setFill("Black")
    yesButton.setOutline("Yellow")
    yesButton.draw(win)

    yesText = Text(Point(365, height - 75), "YES")
    yesText.setTextColor("yellow")
    yesText.setSize(24)
    yesText.draw(win)

    noButton = Rectangle(Point(width - 290, height - 100), Point(width - 440, height - 50))
    noButton.setFill("Black")
    noButton.setOutline("Yellow")
    noButton.draw(win)

    noText = Text(Point(width - 365, height - 75), "NO")
    noText.setTextColor("yellow")
    noText.setSize(24)
    noText.draw(win)

    #Gets the position of the mouse for the buttons
    click = win.getMouse()
    answer = False
    
    #Yes
    if click.getX() > 290 and click.getX() < 440 and click.getY() < (height - 50) and click.getY() > (height - 100):
        answer = True
        win.close()
        
    #No
    elif click.getX() > (width - 290) and click.getX() < (width - 440) and click.getY() < (height - 50) and click.getY() > (height - 100):
        answer = False
        win.close()

    return answer

def wordPicker(words):
    #Choses a word from the list of words
    for line in words:
        word = words.split()
        totalWords = len(word)

    wordNum = randint(0, totalWords - 1)
    chosenWord = word[wordNum]
    
    return chosenWord


def wordList():
    #Opens the file containing the list of words
    infile = open("wordList.txt", "r")
    wordList = infile.read()
    word = wordPicker(wordList)

    return word

def hangman(width, height, win):

    word = wordList()
    #Window and background
    deathstarWidth = width / 3
    deathstarHeight = height - (height / 2.5)
    backgroundCenter = Point(deathstarWidth, deathstarHeight)
    center = Point(width / 2, height / 2)
    background = Image(backgroundCenter, "death-star-1.gif")
    background.draw(win)

    #Title
    title = Text(Point(width / 2, 40), "Star Wars Hangman")
    title.setSize(36)
    title.setTextColor("Yellow")
    title.draw(win)


    #X wing 1
    xwing1Center = Point(deathstarWidth, deathstarHeight - 200)
    xwing1 = Image(xwing1Center, "x-wing.gif")
    xwing1.draw(win)
    xwing1Gone = False

    #X wing 2
    xwing2Center = Point(deathstarWidth - 200, deathstarHeight - 175)
    xwing2 = Image(xwing2Center, "x-wing.gif")
    xwing2.draw(win)
    xwing2Gone = False

    #X wing 3
    xwing3Center = Point(deathstarWidth - 250, deathstarHeight + 50)
    xwing3 = Image(xwing3Center, "x-wing.gif")
    xwing3.draw(win)
    xwing3Gone = False

    #X wing 4
    xwing4Center = Point(deathstarWidth - 50, deathstarHeight + 200)
    xwing4 = Image(xwing4Center, "x-wing2.gif")
    xwing4.draw(win)
    xwing4Gone = False

    #X wing 5
    xwing5Center = Point(deathstarWidth + 250, deathstarHeight - 150)
    xwing5 = Image(xwing5Center, "x-wing2.gif")
    xwing5.draw(win)
    xwing5Gone = False

    #X wing 6
    xwing6Center = Point(deathstarWidth + 250, deathstarHeight)
    xwing6 = Image(xwing6Center, "x-wing2.gif")
    xwing6.draw(win)
    xwing6Gone = False

    #X wing 7
    xwing7Center = Point(deathstarWidth + 200, deathstarHeight + 200)
    xwing7 = Image(xwing7Center, "x-wing2.gif")
    xwing7.draw(win)
    xwing7Gone = False

    #Variables
    blanks = " _ "
    strike = 0
    strikeLeft = 7
    usedLetters = []
    answer = blanks
    winner = False
    wordBank = "".join(usedLetters)

    for i in range(len(word) - 1):
        answer = answer + blanks

    #Answer blanks
    display = Text(Point(width / 2, (height / 2) - 250), answer)
    display.setSize(24)
    display.setTextColor("Yellow")
    display.draw(win)

    #Message space
    errorMessage = Text(Point(width - 155, (height / 2) - 25), "")
    errorMessage.setTextColor("Green")
    errorMessage.draw(win)

    #Entry block 
    guessTxt = Text(Point(width - 180, height / 2), "Enter a guess: ")
    guessTxt.setTextColor("Yellow")
    guessTxt.draw(win)
    guessInput = Entry(Point(width - 115, height / 2), 2)
    guessInput.draw(win)
    guessInput.setText("")

    #Input guess button
    button = Rectangle(Point(width - 100, (height / 2) - 10), Point(width - 1, (height / 2) + 50))
    button.setFill("Black")
    button.setOutline("Yellow")
    button.draw(win)
    buttonLabel = Text(Point(width - 50, (height / 2) + 18), "GUESS")
    buttonLabel.setSize(20)
    buttonLabel.setTextColor("Yellow")
    buttonLabel.draw(win)
    xwingCount = 7
    wrongLetter = False

    #Used letter bank text
    wordBankText = Text(Point(width - 100, height - 200), "Used letters: ")
    wordBankText.setTextColor("yellow")
    wordBankText.setSize(16)
    wordBankText.draw(win)

    wordBankGuessText = Text(Point(width - 100, height - 175), " ")
    wordBankGuessText.setTextColor("yellow")
    wordBankGuessText.setSize(16)
    wordBankGuessText.draw(win)

    #Number of strikes left text
    strikeText = Text(Point(width - 190, height - 325), "Strikes Left: ")
    strikeText.setTextColor("yellow")
    strikeText.setSize(12)
    strikeText.draw(win)

    strikesLeft = Text(Point(width - 130, height - 325), "7")
    strikesLeft.setTextColor("yellow")
    strikesLeft.setSize(12)
    strikesLeft.draw(win)


    while strike < 7 and winner == False:
        #passThrough is the click for the GUESS button
        passThrough = win.getMouse()
        
        if passThrough.getX() > (width - 100) and passThrough.getX() < width and passThrough.getY() > ((height / 2) - 10) and passThrough.getY() < ((height / 2) + 50):

            #Counters and guess input control
            guess = guessInput.getText().lower()
            guessInput.setText("")
            blankCount = answer.count(blanks)
            letterCount = word.count(guess)
            usedLetterCount = usedLetters.count(guess)

            #Error message appears if invalid input is registered
            if guess == "" or guess == " ":
                if len(guess) != 1:
                    errorMessage.setText("You entered a blank. Please enter a letter.")
                    

            #Iterates through the word for every guess and updates the answer for each letter that is correct
            elif guess in word and not guess in usedLetters:
                usedLetters.append(guess)
                answer = word
                for letter in word:
                    if not letter in word or not letter in usedLetters:
                        wordBankGuessText.setText(usedLetters)
                        answer = answer.replace(letter, blanks)
                        display.setText(answer)
                        errorMessage.setText(" ")

                if answer == word:
                    winner = True

            elif usedLetterCount > 0:
                errorMessage.setText("You already used that letter. Try again.")
                
            #Updates the graphics for each wrong guess
            else:
                strike = strike + 1
                strikeLeft = strikeLeft - 1
                if strike == 1:
                    xwingCount = xwingCount - 1
                    xwing1.undraw()
                    xwing1Gone = True
                elif strike == 2:
                    xwingCount = xwingCount - 1
                    xwing2.undraw()
                    xwing2Gone = True
                elif strike == 3:
                    xwingCount = xwingCount - 1
                    xwing3.undraw()
                    xwing3Gone = True
                elif strike == 4:
                    xwingCount = xwingCount - 1
                    xwing4.undraw()
                    xwing4Gone = True
                elif strike == 5:
                    xwingCount = xwingCount - 1
                    xwing5.undraw()
                    xwing5Gone = True
                elif strike == 6:
                    xwingCount = xwingCount - 1
                    xwing6.undraw()
                    xwing6Gone = True
                elif strike == 7:
                    xwingCount = xwingCount - 1
                    xwing7.undraw()
                    xwing7Gone = True
                usedLetters.append(guess)
                wrongLetter = True
                errorMessage.setText("That letter is not in the secret word. Try again.")
                wordBankGuessText.setText(usedLetters)
                strikesLeft.setText(strikeLeft)
                

    else:
        if winner == True:
            #Undraws everything to make room for ending screen
            display.undraw()
            guessTxt.undraw()
            buttonLabel.undraw()
            button.undraw()
            guessInput.undraw()
            errorMessage.undraw()
            background.undraw()
            title.undraw()
            wordBankGuessText.undraw()
            wordBankText.undraw()
            strikeText.undraw()
            strikesLeft.undraw()

            #Draws all of the winner screen
            winnerText = Text(Point(width / 2, 75), "You win! May the force be with you.")
            winnerText.setTextColor("yellow")
            winnerText.setSize(36)
            winnerText.draw(win)
            winnerBackground = Image(backgroundCenter, "explosion.gif")
            winnerBackground.draw(win)
            secretWordRevealMessage = Text(Point(width / 2, (height / 2) - 230), "The secret word was:")
            secretWordRevealMessage.setTextColor("yellow")
            secretWordRevealMessage.setSize(24)
            secretWordRevealMessage.draw(win)
            secretWordReveal = Text(Point(width / 2, (height / 2) - 200), word)
            secretWordReveal.setTextColor("yellow")
            secretWordReveal.setSize(24)
            secretWordReveal.draw(win)
            newGame = newGameQuestion(height, width, win)

        else:
            #Undraws everything to make room for ending screen
            background.undraw()
            button.undraw()
            buttonLabel.undraw()
            errorMessage.undraw()
            guessTxt.undraw()
            guessInput.undraw()
            title.undraw()
            display.undraw()
            wordBankGuessText.undraw()
            wordBankText.undraw()
            strikeText.undraw()
            strikesLeft.undraw()

            #Draws all of the loser screen
            loserText = Text(Point(width / 2, 75), "You lose! Welcome to the dark side")
            loserText.setTextColor("yellow")
            loserText.setSize(36)
            loserText.draw(win)
            secretWordRevealMessage = Text(Point(width / 2, (height / 2) - 230), "The secret word was:")
            secretWordRevealMessage.setTextColor("yellow")
            secretWordRevealMessage.setSize(24)
            secretWordRevealMessage.draw(win)
            secretWordReveal = Text(Point(width / 2, (height / 2) - 200), word)
            secretWordReveal.setTextColor("yellow")
            secretWordReveal.setSize(24)
            secretWordReveal.draw(win)
            loserBackground = Image(center, "darth-vader-3.gif")
            loserBackground.draw(win)
            newGame = newGameQuestion(height, width, win)
                
    return newGame

def main():
    #Sets the window size, can be edited as none of the other variables are hard coded. Just don't go too small
    #or buttons will overlap
    width = 1200
    height = 750
    win = GraphWin("Hangman", width, height)
    win.setBackground("black")

    #Scrolling directions
    directions0a = Text(Point(width / 2, height / 2), "A long time ago in a galaxy far,")
    directions0a.setTextColor("Deep Sky Blue")
    directions0a.setSize(20)
    directions0a.setStyle("bold")
    directions0a.draw(win)
    directions0b = Text(Point((width / 2) - 125, (height / 2) + 40), "far away......")
    directions0b.setTextColor("Deep Sky Blue")
    directions0b.setSize(20)
    directions0b.setStyle("bold")
    directions0b.draw(win)
    title = Text(Point(width / 2, height), "Directions ")
    title.setTextColor("yellow")
    title.setSize(36)
    title.setStyle("bold")
    title.draw(win)
    directions1 = Text(Point(width / 2, height + 40), "This is Star Wars Hangman. All the words are ")
    directions1.setTextColor("yellow")
    directions1.setSize(20)
    directions1.setStyle("bold")
    directions1.draw(win)
    directions2 = Text(Point(width / 2, height + 80), "either planets in Star Wars or notable characters.")
    directions2.setTextColor("yellow")
    directions2.setSize(20)
    directions2.setStyle("bold")
    directions2.draw(win)
    directions3 = Text(Point(width / 2, height + 120), "Some character have names that contain numbers.")
    directions3.setTextColor("yellow")
    directions3.setSize(20)
    directions3.setStyle("bold")
    directions3.draw(win)
    directions4 = Text(Point(width / 2, height + 500), "Enjoy!")
    directions4.setTextColor("yellow")
    directions4.setSize(20)
    directions4.setStyle("bold")
    directions4.draw(win)

    #Scroll the opening crawl directions
    for i in range(42):
        directions0a.move(0, -20)
        directions0b.move(0, -20)
        title.move(0, -20)
        directions1.move(0, -20)
        directions2.move(0, -20)
        directions3.move(0, -20)
        directions4.move(0, -20)
        time.sleep(.5)
 
    directions0a.undraw()
    directions0b.undraw()
    title.undraw()
    directions1.undraw()
    directions2.undraw()
    directions3.undraw()
    directions4.undraw()
    newGame = hangman(width, height, win)
    
    
    if newGame == True:
        main()

    else:
        win.close()
    
main()


#Pseudo Code:
#1. Print the directions
#2. Call the game and use a function to randomly choose a secret word from a file 
#3. Display a blank for each letter in the secret word
#4. Ask the user to guess a letter
#5. Use conditionals to check if the letter is in the word, if it is change the blanks to the letter
#6. If they get the letter wrong add it to a used letter bank on the screen
#7. Display 7 strikes and take one off for each incorrect guess
#8. Update the picture to graphically show a consequence for an incorrect guess
#9. If the get they word right, display a game won screen and ask if they want to play again
#10. If the get the word wrong, display a game lost screen and ask if they want to play again
#11. Make a yes and no button on both the win and lost screen
#12. No button ends the game and closes the window
#13. Yes button closes the window and reopens the game again

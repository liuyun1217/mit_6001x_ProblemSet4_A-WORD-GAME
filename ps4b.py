from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = ''
    # For each word in the wordList
    for i in wordList:
        if isValidWord(i, hand, wordList):
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            thisScore = getWordScore(i, n)
                # Find out how much making that word is worth
            if thisScore > maxScore:
                maxScore = thisScore
                bestWord = i
            # If the score for that word is higher than your best score
        else:
          bestWord == ''
                # Update your best score, and best word accordingly
        
            

    # return the best word you found.
    if bestWord == '':
        return ''
    else:
        return bestWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    totalScore = 0
    while sum(hand.values()) != 0:
        print "Current Hand: ",
        displayHand(hand)
        
        # Ask user for input
        word = compChooseWord(hand, wordList, n)
#        # If the input is a single period:
#        if word == ".":
#            # End the game (break out of the loop)
#            print "Goodbye! Total score: "+ str(totalScore)
#            break
#            
#        # Otherwise (the input is not a single period):
#        else:
#            # If the word is not valid:
#            if not isValidWord(word, hand, wordList):
#                print "Invalid word, please try again."
#                # Reject invalid word (print a message followed by a blank line)
#            
#            # Otherwise (the word is valid):
#            else:
        totalScore = totalScore + getWordScore(word, n)
        if word =='':
            break
        else:
                    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print "\""+str(word)+"\""+" earned "+str(getWordScore(word, n))+" points. Total: " + str(totalScore)
                    # Update the hand 
            hand = updateHand(hand, word)
    print "Total score: "+str(totalScore)+" points."
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
#    gameFlag = ''
#    gameCount = 0
#    while gameFlag != 'e':  
#        
#    
#    
#    
#        gameFlag = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
#        if gameFlag =='n':
#            hand = dealHand(n)
#            playHand(hand, wordList, HAND_SIZE)
#        elif gameFlag =='r':
#            if gameCount < 1:
#                print "You have not played a hand yet. Please play a new hand first!"
#            else:
#                playHand(hand, wordList, HAND_SIZE)
#        elif gameFlag =='e':
#                break
#
# Build data structures used for entire session and play game
#
    userSelect = ''
    gameFlag = ''
    gameCount = 0
    
    while gameFlag != 'e':
        gameFlag = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if gameFlag =='e':
            break  
        else:
            while True:
                if gameFlag =='r':
                    if gameCount < 1:
                        print "You have not played a hand yet. Please play a new hand first!"
                        break
                    else:
                        userSelect = raw_input("Enter u to have yourself play, c to have the computer play: ")
                        if userSelect =='u': 
                            playHand(hand, wordList, HAND_SIZE)
                            gameCount += 1 
                            break
                        elif userSelect == 'c':
                            compPlayHand(hand, wordList,HAND_SIZE) 
                            break
                        else:
                            print "Invalid command."
                
                
                        
                elif gameFlag =='n':
                    userSelect = raw_input("Enter u to have yourself play, c to have the computer play: ")                
                    
                    if userSelect =='u': 
                        hand = dealHand(HAND_SIZE)
                        playHand(hand, wordList, HAND_SIZE)
                        gameCount += 1
                        break
                    elif userSelect == 'c':
                        hand = dealHand(HAND_SIZE)
                        compPlayHand(hand, wordList,HAND_SIZE)
                        gameCount += 1
                        break
                    else:
                        print "Invalid command."                        
                      
        
                else:
                    print "Invalid command."
                    break
            


    
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)



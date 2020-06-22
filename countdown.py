#=============#
#   Imports   #
#=============#
import random
import time



def RandVowel():
    """
    Chooses a letter randomly, using
    probability weighting.
    
    This function selects an element
    of the vowels array using the 
    probabilty weights found in the 
    probabilities array. Each weight
    is based on the weights used
    in Countdown, found on the website:
    http://www.thecountdownpage.com/letters.htm
    
    Returns
    -------
    rand_vowel : str
        A randomly selected vowel character
    
    """
    
    vowels = ["a", "e", "i", "o", "u"]
    probabilities = [
    15, 21, 13, 13, 5
    ]
    
    rand_vowel = random.choices(vowels, weights=probabilities)
    return rand_vowel
    



   

def RandConsonant():
    """
    Chooses a letter randomly, using
    probability weighting.
    
    This function selects an element
    of the consonants array using the
    probability weights from the
    probabilities array. Each weight 
    is based on the weights used in 
    Countdown, found on the website:
    http://www.thecountdownpage.com/letters.htm
    
    Returns
    -------
    rand_consonant : str
        A randomly selected consonant
        
    """
    
    consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", 
    "m", "n", "p", "q", "r", "s", "t", "v", "x",
    "y", "z"
    ]
    probabilities = [2, 3, 6, 2, 3, 2, 1, 1, 5, 4, 8, 4, 1, 9, 9, 9, 1, 1, 1, 1]
    
    rand_consonant = random.choices(consonants, weights=probabilities)
    return rand_consonant
    
   



   
    
def select_characters():
    """
    Selects 9 characters, randomly,
    depending on the user choice.
    
    This function uses the RandConsonant()
    and RandVowel() functions to generate 
    9 characters, depending on the user 
    input. It will repeat 9 times, telling
    the user how many letters they have left
    to choose. Once all characters have been
    selected, they are returned.
    
    Returns
    -------
    recieved_characters : list
        A list which contains the 9 
        selected characters.
    
    """
    
    recieved_characters = ""
    
    counter = 0
    while counter < 9:
        user_character_choice = input(" ==== Please choose a Vowel [v] or a Consonant [c] ==== \n>> ")
        
        if user_character_choice == "v":
            rand_vowel = RandVowel()
            
            recieved_characters = recieved_characters + rand_vowel[0]
            
            counter = counter + 1
            
            print("\n ========  You have: " + str(9 - counter) + " letters left to choose  ========\n")
            
        elif user_character_choice == "c":
            rand_consonant = RandConsonant()
            
            recieved_characters = recieved_characters + rand_consonant[0]
            
            counter = counter + 1
            
            print("\n ========  You have: " + str(9 - counter) + " letters left to choose  ========\n")
            
        else:
            print("\n == Input not a Vowel [v] or Consonant [c] try again ==\n")
            
            
            
    print("Your letters are: " + recieved_characters) 
    
    type(recieved_characters)
    
    return recieved_characters








def dictionary_reader():
    """
    Opens a text file and creates
    a list from each word in the file.
    
    This function opens the text file
    which contains the words which are
    acceptable words during the game.
    Each word is iterated through and
    placed into a list. The final list
    is returned.
    
    Returns
    -------
    words_contents : list
        A list containing
        every acceptable
        word for the game.
        
    """
    
    words = open("words.txt", "r")
    words_contents = []
    
    for line in words:
        words_contents.append(line.strip())
        
    words.close()    
    return words_contents
    








def is_word_in_chars(user_word: str, user_chars: str) -> bool:
    """
    Determine whether a given word is
    contained within a given set of
    characters.
    
    This function determines how many
    times a character occurs in a word
    and compares it to how many times
    it occurs in a given set of characters.
    If the number of occurrences is equal or
    if the occurrences in the word is less 
    than in the character set (but not equal
    to zero) than that character must occur
    in both and is an allowed character.
    A True bool is appended to the
    occurence_array. If the character occurs
    more times in the word than in the set,
    then it is not an allowed character and
    a False bool is appended to the
    occurence_array. After each character in
    the given word is iterated through, the
    occurence_array is checked for any Falses.
    If a False occurs, than the word given can
    not be made up from the characters given.
    
    Parameters
    ----------
    user_word : str
        A word the user has inputted.
    user_chars : str
        The characters the user has access to.
        
    Returns
    -------
    bool : 
        True if successful, False if not.
    
    """

    occurence_array = []
    
    for char in user_word:
    
        # iterates through each char in the word, counting 
        # occurences of each char in both the word and the
        # characters available to player.
        
        occurence_in_user_chars = user_chars.count(char)
        occurence_in_user_word = user_word.count(char)
        
        # if char occurs more in the available chars or occurs
        # the same amount of times, True is placed into array.
        
        if occurence_in_user_chars >= occurence_in_user_word:
            occurence_array.append(True)
        else:
            occurence_array.append(False)
    
    # if a False is present in occurrence array, then a 
    # letter appears more times than allowed, or 
    # isn't in the available chars at all.
    
    if False in occurence_array:
        return False
            
    else:
        return True
        
        
  








  
def find_best_word(word_file, user_chars: str, user_word: str):
    """
    Finds words which are both contained in the
    user character set and are the longest possible
    words. These words would have been the highest
    scoring words using the characters that the
    user has access to.
    
    Parameters
    ----------
    word_file : list
        A list containing all possible words.
    user_chars : str
        The characters the user has access to.
    user_word : str
        The word the user inputted.
        
    Returns
    -------
    best_words : list
        A list containing the best words possible.
        
    """
    
    current_word = ""
    longest_word = ""
    longer_words = []
    best_words = []
    
    for word in word_file:
        current_word = word
        word_in_chars = is_word_in_chars(word, user_chars)
        
        if len(current_word) > len(user_word) and word_in_chars == True:
            longer_words.append(current_word)
            
            if len(current_word) > len(longest_word):
                longest_word = current_word
            
    for word in longer_words:
        if len(word) == len(longest_word):
            best_words.append(word)
            
    return(best_words)
        
 











 
        
        
def word_lookup(word_file, user_chars: str):
    """
    A function which checks whether a
    user inputted word exists within
    the word file. If it exists, then
    a score is calculated and the best
    possible words are displayed.
    
    Parameters
    ----------
    word_file : list
        A list containing all possible words.
    user_chars : str
        The characters the user has access to.
        
    """

    while True:
        user_word = input("\n ==== Please input a word using your 9 characters: ====\n>> ")
           
        word_in_chars = is_word_in_chars(user_word, user_chars)
        
        if word_in_chars == True:
            break
            
        elif word_in_chars == False:
            print("\n ========  Word is not in your set of letters  ========\n\n ====================  Try Again.  ====================\n")
            
            print("Your letters are: " + user_chars)

    if user_word in word_file:
        print("\nYour word was: " + user_word + " which got you " + str(len(user_word)) + " points.\n")
        best_words = find_best_word(word_file, user_chars, user_word)
        
        if best_words:
            print("""
 =====================================================
  ____            _    __          __           _     
 |  _ \          | |   \ \        / /          | |    
 | |_) | ___  ___| |_   \ \  /\  / /__  _ __ __| |___ 
 |  _ < / _ \/ __| __|   \ \/  \/ / _ \| '__/ _` / __| 
 | |_) |  __/\__ \ |_     \  /\  / (_) | | | (_| \__ \
 
 |____/ \___||___/\__|     \/  \/ \___/|_|  \__,_|___/
                                                      
 =====================================================                                         

    """)
            
            print(" ========== Better words could have been: ===========")
            for word in best_words:
                print(word)
                time.sleep(0.1)
        elif not best_words:
            print("You chose one of the best words, well done!")
        
    else:
        print("Your word does not exist in the dictionary, you get 0 points")
       










    
def main():
    print("""

 ======================================================
   _____                  _      _                     
  / ____|                | |    | |                    
 | |     ___  _   _ _ __ | |_ __| | _____      ___ __  
 | |    / _ \| | | | '_ \| __/ _` |/ _ \ \ /\ / / '_ \ 
 | |___| (_) | |_| | | | | || (_| | (_) \ V  V /| | | |
  \_____\___/ \__,_|_| |_|\__\__,_|\___/ \_/\_/ |_| |_|
  
                     By Alex Rundle                       
 ======================================================                                                     

    """)
    word_lookup(dictionary_reader(), select_characters())
    
    
if __name__ == "__main__":
    main()
    
import random,string

WORDLIST_FILENAME = "words.txt"
 
def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):#-----------------------problemy es funckiayi paymanumna!!!!!!!!!!!!!!!
    return all(i in letters_guessed for i in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    word=""
    for i in secret_word:
        if i in letters_guessed:
            word+=i
        else:
            word+="_ "
    return word

def get_available_letters(letters_guessed):
    d=list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in d:
            d.remove(i)
    d=''.join(d)
    return d

def f(warning, letters):
    if x in word:
        if x in letters:
            if warning>0:
                warning-=1
                print("Oops! You've already guessed that letter. You have", warning, "warnings left: ",get_guessed_word(word, letters))
            else:
                guess-=1
                print("Oops! That letter is not in my word: !!", get_guessed_word(word, letters))
        else:
            letters+=x
            print("Good guess: ", get_guessed_word(word, letters))
    
def hangman(secret_word):
    guess=6
    warning=3
    letters=[]
    word=secret_word
    unique=''.join(set(word))
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(word), "letters long.")
    print("You have", warning, "warnigns left.")
    while is_word_guessed(word, letters) == False:
        print("-------------")
        print("You have", guess, "guesses left.")
        print("Available letters:", get_available_letters(letters))
        d=input("Please guess a letter: ")
        x=d.lower()
        if x in word:
            if x in letters:
                if warning>0:
                    warning-=1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left: ",get_guessed_word(word,letters))
                else:
                    guess-=1
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))
            else:
                letters+=x
                print("Good guess: ", get_guessed_word(word, letters))
        elif x in letters:
            if warning>0:
                warning-=1
                print("Oops! You've already guessed that letter. You now have", warning ,"warnings :",get_guessed_word(word, letters))
            else:
                guess-=1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))            
        elif x not in string.ascii_lowercase:
            if warning>0:
                warning-=1
                print("Oops! That is not a valid letter. You have", warning, "warnings left: ", get_guessed_word(word, letters))
            else:
                guess-=1
                print("Oops! That is not a valid letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))
        elif x not in word:
            if x in ['a','e','i','o','u']:
                letters+=x
                guess-=2
            else:
                letters+=x
                guess-=1
            print("Oops! That letter is not in my word: ", get_guessed_word(word, letters))

        if guess<0:
            print("Sorry, you ran out of guesses. The word was else: ", word)
            break
        elif is_word_guessed(word, letters) == True:
            print("Congratulations, you won!")
            total_score=guess*len(unique)
            print("Your total score for this game is: ",total_score)
            
def match_with_gaps(my_word, other_word):
    h = 0
    word = ''.join(my_word.split())
    if len(word) == len(other_word):
      for i, word1 in enumerate(word):
        if word1 == other_word[i] or word1 == '_':
          h += 1
          if h == len(other_word):
            return True
    return False

def show_possible_matches(my_word):
    match = ''
    for i in wordlist:
      if match_with_gaps(my_word, i):
        match += i + " "
    if len(match) == 0:
      return "No matches found."
    else:
      return match

def hangman_with_hints(secret_word):
    guess=6
    warning=3
    letters=[]
    word=secret_word
    unique=''.join(set(word))
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(word), "letters long.")
    print("You have", warning, "warnigns left.")
    while is_word_guessed(word, letters) == False:
        print("-------------")
        print("You have", guess, "guesses left.")
        print("Available letters:", get_available_letters(letters))
        d=input("Please guess a letter: ")
        x=d.lower()
        if x == '*':
            print(show_possible_matches(get_guessed_word(word, letters)))
        elif x in word:
            if x in letters:
                if warning>0:
                    warning-=1
                    print("Oops! You've already guessed that letter. You have", warning, "warnings left: ",get_guessed_word(word,letters))
                else:
                    guess-=1
                    print("Oops! You've already guessed that letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))
            else:
                letters+=x
                print("Good guess: ", get_guessed_word(word, letters))
        elif x in letters:
            if warning>0:
                warning-=1
                print("Oops! You've already guessed that letter. You now have", warning ,"warnings :",get_guessed_word(word, letters))
            else:
                guess-=1
                print("Oops! You've already guessed that letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))            
        elif x not in string.ascii_lowercase:
            if warning>0:
                warning-=1
                print("Oops! That is not a valid letter. You have", warning, "warnings left: ", get_guessed_word(word, letters))
            else:
                guess-=1
                print("Oops! That is not a valid letter. You have no warnings left, so you lose a letter: ", get_guessed_word(word, letters))
        elif x not in word:
            if x in ['a','e','i','o','u']:
                letters+=x
                guess-=2
            else:
                letters+=x
                guess-=1
            print("Oops! That letter is not in my word: ", get_guessed_word(word, letters))

        if guess<0:
            print("Sorry, you ran out of guesses. The word was else: ", word)
            break
        elif is_word_guessed(word, letters) == True:
            print("Congratulations, you won!")
            total_score=guess*len(unique)
            print("Your total score for this game is: ",total_score)

if __name__ == "__main__":
##    secret_word = choose_word(wordlist)
##    hangman(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
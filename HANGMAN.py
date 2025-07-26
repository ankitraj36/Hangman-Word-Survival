import random  # Import the random module for selecting a random word for the game

# List of ASCII art stages showing the gallows and the hangman for different numbers of wrong guesses.
# The 'r' before triple quotes means raw strings, which helps in displaying backslashes properly in ASCII art.
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
========
''',
r'''
  +---+
  |   |
      |
      |
      |
      |
========
''']

print(r'''
 _
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                    
                   ''')
# List of possible words for the player to guess
word_list = [
    "APPLE", "ORANGE", "BANANA", "MANGO", "GRAPE", "PEACH", "CHERRY", "KIWI",
    "PAPAYA", "PLUM", "LYCHEE", "PEAR", "FIG", "LEMON", "LIME", "GUAVA",
    "DATES", "PRUNE", "OLIVE", "APRICOT", "COCONUT", "AVOCADO", "POMEGRANATE",
    "MELON", "WATERMELON", "RASPBERRY", "BLUEBERRY", "BLACKBERRY", "STRAWBERRY",
    "CRANBERRY", "BOYSENBERRY", "CURRANT", "TANGERINE", "NECTARINE", "PASSIONFRUIT",
    "JACKFRUIT", "PERSIMMON", "STARFRUIT", "DRAGONFRUIT", "SOURSOP", "RAMBUTAN",
    "MULBERRY", "QUINCE", "PINEAPPLE", "CANTALOUPE", "HONEYDEW", "LONGAN",
    "SAPOTA", "TAMARIND", "ELDERBERRY", "GOOSEBERRY", "UMBRA", "DAMSON",
    "PLANTAIN", "FEIJOA", "UGLI", "SALAK", "JAMBUL", "LANZONES", "LOQUAT",
    "PITAYA", "KIWANO", "BAEL", "MARIONBERRY", "MIRACLE", "GAC", "CAMU",
    "MANGOSTEEN", "ACKEE", "TAMARILLO", "INDIANFIG", "BLACKCURRANT", "REDCURRANT",
    "MORA", "SNAKEFRUIT", "ROSEAPPLE", "MUSKMELON", "SANTOL", "SUGARAPPLE",
    "BREADFRUIT", "MAMMEE", "LANGSAT", "SAPODILLA", "LUCUMA", "CUPUACU",
    "CHERIMOYA", "MOUNTAINAPPLE", "BIGNAY", "CALAMANSI", "CLEMENTINE",
    "JAPANESEPLUM", "YUZU", "HUCKLEBERRY", "NARANJILLA", "JOSTABERRY", "BARBERRY",
    "MAKOPA", "CHOKEBERRY", "GOLDENBERRY", "SASKATOON", "TAYBERRY", "WHITECURRANT",
    "TORONJA", "ZIZIPHUS"
]


# Randomly select a word from the list, converting it to lowercase for consistent comparison
chosen_word = random.choice(word_list).lower()
print("Your Chosen Word:", chosen_word)  # For testing: print chosen word (remove/comment in real game)

# Number of remaining lives (wrong guesses allowed). Highest index in stages is the "full" hangman.
lives = len(stages) - 1

# Keep track of letters correctly guessed by the player
correct_letters = []

# Keep track of letters guessed incorrectly by the player
wrong_letters = []

# Flag to indicate whether the game is over (win or lose)
game_over = False

# Game loop: continue to play until the game is over
while not game_over:
    print(stages[lives])  # Display the current hangman ASCII art based on remaining lives
    print("Wrong guesses:", " ".join(wrong_letters))  # Show all wrong letters guessed so far

    # Build a string showing the current state of the guessed word, with underscores for unknown letters
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter + " "  # If guessed, show the letter
        else:
            display += "_ "         # If not guessed, show an underscore

    print("Current Word:", display.strip())  # Show the player their progress

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Validate the guess: must be a single alphabetical character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter!")
        continue  # Skip the rest of the loop and ask for input again

    # Check if the letter was already guessed (either right or wrong)
    if guess in correct_letters or guess in wrong_letters:
        print("You already guessed that letter, try a different one.")
        continue  # Do not penalize or repeat logic for duplicate guesses

    # Check if the guessed letter is in the word
    if guess in chosen_word:
        correct_letters.append(guess)  # Add to the list of correct letters
        print("Correct!")              # Give feedback
    else:
        wrong_letters.append(guess)    # Add to the wrong guesses
        lives -= 1                     # Lose a life for a wrong guess
        print("Wrong!")                # Inform player

        # If no lives remain, the player loses
        if lives == 0:
            print(stages[lives])                         # Show final hangman
            print("You Lose! The word was:", chosen_word.upper())  # Reveal the word
            break                                        # Exit the loop/game

    # Check win condition: All letters in the word have been guessed
    if all([letter in correct_letters for letter in chosen_word]):
        print("🎉 YOU WIN!")              # Celebrate victory
        print("The word was:", chosen_word.upper())  # Reveal the word
        game_over = True                 # End the game loop



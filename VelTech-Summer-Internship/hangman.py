import random
def choose_word(word_list):
    return random.choice(word_list).upper()
def display_board(missed_letters, correct_letters, secret_word):
    print("\n====================")
    print("Missed Letters:", " ".join(missed_letters))
    blanks = ""
    for letter in secret_word:
        if letter in correct_letters:
            blanks += letter + " "
        else:
            blanks += "_ "
    print("Word:", blanks)
    print("====================")
def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        elif guess in already_guessed:
            print("You have already guessed that letter.")
        else:
            return guess
def check_game_over(correct_letters, missed_letters, secret_word):
    won = True
    for letter in secret_word:
        if letter not in correct_letters:
            won = False
            break
    if won:
        print("\nCongratulations! You guessed the word:", secret_word)
        return True
    if len(missed_letters) >= 7:
        print("\nGame Over!")
        print("The word was:", secret_word)
        return True
    return False
def play_again():
    return input("\nDo you want to play again? (yes/no): ").lower().startswith('y')
def play():
    word_list = [
        "python",
        "jupyter",
        "programming",
        "function",
        "analytics",
        "explore",
        "network",
        "foundation"
    ]
    secret_word = choose_word(word_list)
    missed_letters = []
    correct_letters = []
    while True:
        display_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters.append(guess)
            print("Correct Guess!")
        else:
            missed_letters.append(guess)
            print("Wrong Guess!")
        game_over = check_game_over(
            correct_letters,
            missed_letters,
            secret_word
        )
        if game_over:
            if play_again():
                missed_letters = []
                correct_letters = []
                secret_word = choose_word(word_list)
            else:
                print("Thanks for playing!")
                break
play()

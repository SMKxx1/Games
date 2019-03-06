import random

def main():
    welcome = ['Welcome to Hangman! A word will be chosen at random and',
               'you must try to guess the word correctly letter by letter',
               'before you run out of attempts. Good luck!'
               ]

    for line in welcome:
        print(line, sep='\n')

    play_again = True

    while play_again:

        words = ["manufacturing", "chairs", "mathematics", "attempt", "explanation",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo","mission",
                 "monkey","folks","simplest","cookies","sjbn","independent","neighborhood"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-")
        joined_word = None


        attempts = 10

        while attempts != 0 and "-" in word_guessed:
            print("\nYou have {} attempts remaining".format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nPlease select a letter between A-Z" + "\n> ")).lower()
            except:
                print("That is not valid input. Please try again.")
                continue                
            else: 
                if not player_guess.isalpha():
                    print("That is not a letter. Please try again.")
                    continue
                elif player_guess == 'exit':
                    exit()
                elif len(player_guess) > 1:
                    print("That is more than one letter. Please try again.")
                    continue
                elif player_guess in guessed_letters:
                    print("You have already guessed that letter. Please try again.")
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(attempts)

        if "-" not in word_guessed:
            print("\nCongratulations! {} was the word".format(chosen_word))
        else:
            print("\nUnlucky! The word was {}.".format(chosen_word))

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

main()

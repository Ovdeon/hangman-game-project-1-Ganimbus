# Welcome interface
print("Welcome to Hangman game!")
name = input("Please, insert your name: ")
print(name, ",there are some rules you should know before playing. Please read them in the README file :) ")
print("Guess the characters")


def play_game():
    winner = False
    word = "abc2323sd"
    hidden_word = "_"*len(word)
    guessed_chars = []
    guessed_series = []
    attempts = 6
    print(graphical_interface(attempts))
    print(f"Number of tries: {attempts}")
    print(hidden_word)
    while attempts > 0 and not winner:
        char = input("Which character do you choose?")
        if len(char) == 1 and char.isalnum():
            if char in guessed_chars:
                print("The character has already been chosen")
            elif char not in word:
                print(char, " does not belong to the word")
                attempts -= 1
                print(f"Number of tries: {attempts}")
                guessed_chars.append(char)
            else:
                print("Great. The char is in the word")
                guessed_chars.append(char)
                word_as_list = list(hidden_word)
                index = [i for i, letter in enumerate(word) if letter == char]
                for index_ in index:
                    word_as_list[index_] = char
                hidden_word = "".join(word_as_list)
                if "_" not in hidden_word:
                    winner = True
        elif len(char) == len(word) and char.isalnum():
            if char in guessed_series:
                print("Don´t repeat")
            elif char != word:
                print("It's not correct")
                attempts -= 1
                guessed_series.append(char)
                print(f"Number of tries: {attempts}")
            else:
                winner = True
                hidden_word = word
        else:
            print("Invalid attempt")
        print(graphical_interface(attempts))
        print(hidden_word)
    if winner:
        print("You managed to guess all the characters. Congratulations!")
    else:
        print("You ran out of attempts. Better luck next time.")


def graphical_interface(attempts):
    phases = [  # phase 6
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \.
                   ___________________
                """,
        # phase 5
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   ___________________
                """,
        # phase 4
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   ___________________
                """,
        # phase 3
        """
                   --------
                   |      |
                   |      O
                   |      |/
                   |      |
                   |     
                   ___________________
                """,
        # phase 2
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   ___________________
                """,
        # phase 1
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   ___________________
                """,
        # phase 0
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   ___________________
                """
    ]
    print(phases[attempts])


play_game()

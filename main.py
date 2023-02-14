# Welcome interface
word = "abc2323sd"
print("Welcome to Hangman game!")
name = input("Please, insert your name: ")
print(name, ",there are some rules you should know before playing. Please read them in the README file :) ")
print("Let's play HANGMAN!")
print("Guess the characters")


def graphical_interface(attempts):
    phases = [  # phase 6
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
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
    return phases[attempts]

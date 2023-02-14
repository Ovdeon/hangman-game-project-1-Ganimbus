# Project

Hello new developers; Now is the time to start working on your project.
Hangman game! is the name of the project; If you want to know how to play this game, check the link below.

https://www.youtube.com/watch?v=leW9ZotUVYo

## Instructions
- Read all the bank of words or phrases from the JSON file. Select one and start the game.
- You will always receive numbers and letters, not symbols(except blank characters)
- Use everything you have learned so far, and try new things. Not include classes.
- Try to create the best user experience in your terminal.

## Bonus
- write tests.

### What was your creative process:

First, my impression of the game is that I determine the word to guess from the words.json list and the user who runs the code will be the one to guess.

As a starting point the user will be welcomed, asked to enter a name. After that, The player is advised to read the rules.

#### Rules:
- The game consists of guessing a series of alphanumeric characters.
- The game starts by showing the number of characters, but hiding them.
- The player will indicate a character and if it is within the series, it will be shown, otherwise the player will lose one of his attempts. 
- There are only 6 attempts to get all the characters.
- If the attempts are exhausted before guessing the word, the player loses.
- The player wins if he/she gets the word right before running out of tries.

A very simple graphical interface will be used within the code to make the game more entertaining. A series of dashes will be displayed whose number is exact to the series to be guessed.

.isalpha() is used so that only alphanumeric values can be inserted.





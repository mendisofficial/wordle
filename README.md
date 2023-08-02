# wordle

Welcome to Wordle! This is a Python-based command-line Wordle game.

## How to Play

1. Clone the repository or download the `wordle.py` and `words.txt` files to your local machine.
2. Make sure you have Python installed on your computer.
3. Run the game by executing the following command in your terminal or command prompt:

   ```bash
   python wordle.py
   ```

## Gameplay

1. You will be presented with the following options:
    Enter '1' to play the game.
    Enter '2' to see the instructions.

2. If you choose '1' to play the game, you will be prompted to select the level:
    Enter '1' for Easy (10 attempts).
    Enter '2' for Medium (8 attempts).
    Enter '3' for Hard (4 attempts).

3. Once the level is chosen, the game will begin, and you will be asked to guess a 5-letter word. After each guess, you will receive feedback in the following format:
    'O' indicates a correct letter in the correct position.
    'X' indicates a correct letter in the wrong position.
    '_' indicates a letter that is not in the word.

4. Keep guessing until you correctly guess the word or run out of attempts.

5. If you wish to exit the game at any time, you can enter 'exit' during your turn.

## Words List

The game uses the words listed in the words.txt file. Each line in the file contains a 5-letter word that the game will randomly select as the secret word for the player to guess.

Have fun playing Wordle!
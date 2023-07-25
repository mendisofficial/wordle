import random

class WordleGame:
    def __init__(self, word_list):
        self.words = word_list
        self.secret_word = self.generate_secret_word()
        self.attempts = 0
        self.max_attempts = 0
        self.guessed_words = set()

    def generate_secret_word(self):
        return random.choice(self.words)

    def check_guess(self, guess):
        if len(guess) != 5:
            print("Invalid guess. Please enter a 5-letter word.")
            return False

        if guess == self.secret_word:
            print("Congratulations! You guessed the word correctly!")
            return True

        if guess in self.guessed_words:
            print("You have already guessed that word. Please try a different word.")
            return False

        if guess not in self.words:
            print("The word is not in the list. Please try again.")
            return False

        attempts_left = self.max_attempts - self.attempts - 1
        feedback = self.get_feedback(guess)
        formatted_guess = ' '.join(guess.upper())
        formatted_feedback = ' '.join(feedback)
        print(f"{formatted_guess}  {formatted_feedback}  ({attempts_left} attempts left)")

        self.attempts += 1
        self.guessed_words.add(guess)

        if guess == self.secret_word:
            print(f"Congratulations! You guessed the word correctly. The secret word was: {self.secret_word}")
            return True

        if self.attempts >= self.max_attempts:
            print(f"Game over! You ran out of attempts. The secret word was: {self.secret_word}")
            return True

        return False

    def get_feedback(self, guess):
        feedback = ''
        secret_word = list(self.secret_word)

        for i in range(len(guess)):
            if i >= len(secret_word):
                break

            if guess[i] == secret_word[i]:
                feedback += 'O'
                secret_word[i] = '-'
            elif guess[i] in secret_word:
                feedback += 'X'
                secret_word[secret_word.index(guess[i])] = '-'
            else:
                feedback += '_'

        return feedback

    def play(self):
        print("Welcome to Wordle!")
        print("Enter '1' to play.")
        print("Enter '2' to see the instructions.")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.select_level()
        elif choice == '2':
            self.show_instructions()
        else:
            print("Invalid choice. Please try again.")

    def select_level(self):
        print("Select the level:")
        print("1. Easy (10 attempts)")
        print("2. Medium (8 attempts)")
        print("3. Hard (4 attempts)")
        level_choice = input("Enter the level choice: ")

        if level_choice == '1':
            self.max_attempts = 10
        elif level_choice == '2':
            self.max_attempts = 8
        elif level_choice == '3':
            self.max_attempts = 4
        else:
            print("Invalid level choice. Please try again.")
            self.select_level()

        self.play_game()

    def play_game(self):
        print("Guess the 5-letter word.")
        print("Enter 'exit' to quit.")

        while True:
            guess = input("Enter your guess: ").lower()

            if guess == 'exit':
                print("Thanks for playing!")
                break

            if self.check_guess(guess):
                break

        self.reset_game()

    def show_instructions(self):
        print("Instructions:")
        print("You need to guess a 5-letter word.")
        print("After each guess, you will receive feedback:")
        print(" - 'O' indicates a correct letter in the correct position.")
        print(" - 'X' indicates a correct letter in the wrong position.")
        print(" - '_' indicates a letter that is not in the word.")
        print("Enjoy playing Wordle!")
        print("Press '1' to start the game.")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.select_level()
        else:
            print("Invalid choice. Please try again.")

    def reset_game(self):
        self.secret_word = self.generate_secret_word()
        self.attempts = 0
        self.guessed_words = set()

def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file if len(line.strip()) == 5]
    return words

word_list = load_words_from_file('words.txt')
game = WordleGame(word_list)
game.play()
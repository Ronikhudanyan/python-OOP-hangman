import random
from words import word_list
from display import game_display



class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.word_completion = list('_' * len(self.chosen_word))
        self.guessed = False
        self.guessed_letters = []
        self.guessed_words = []
        self.lives = 11
        # game_display = game_display
        print("Whats gooooood, lets play some hang mayn! you have 10 lives to begin")
        # print(game_display(self.lives))
        print(game_display)
        print(self.word_completion)
        print("\n")
        while not self.guessed and self.lives > 0:
            guess = input("Alright man dont let me down, guess a letter or a word!").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in self.guessed_letters:
                    print("you already tried", guess, "! guess again!")
                elif guess not in self.chosen_word:
                    print(guess, "look at this loser", guess, "aint in the word! try again")
                    self.lives -= 1
                    self.guessed_letters.append(guess)
                else:   
                    print("Good job,", guess, "is in the word!")
                    self.guessed_letters.append(guess)
                    word_as_list = list(self.word_completion)
                    indices = [i for i, letter in enumerate(self.chosen_word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    self.word_completion = "".join(word_as_list)
                    if "_" not in self.word_completion:
                        self.guessed = True
            elif len(guess) == len(self.chosen_word) and guess.isalpha():
                if guess in self.guessed_words:
                    print("MY LIFE IS ON THE LINE! you already guessed", guess)
                elif guess != self.chosen_word:
                    print(guess, "is not the word.")
                    self.lives -= 1
                    self.guessed_words.append(guess)
                else:
                    self.guessed = True
                    self.word_completion = self.chosen_word
            else:
                print("Thats not even a real guess...")
            # print(game_display(self.lives))
            print("make it count you only have", self.lives, "lives left!")
            print(self.word_completion)
            print("\n")
        if self.guessed:
            print("Look at you! you know how to guess letters! congrats, you WON!")
        else:
            print("BRUH you had this in the bag what happened? The word was " + self.chosen_word + ". try again later loser!")
    
    
            # def game_display(lives):
            #     lives = self.lives
                # levels = [
                #         """
                #         -----
                #         |   |
                #         |
                #         |
                #         |
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         |
                #         |
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         |  -+-
                #         |
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-
                #         |
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |   | 
                #         |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |   | 
                #         |  |
                #         |
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |   | 
                #         |  | 
                #         |  | 
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |   | 
                #         |  | | 
                #         |  | 
                #         |
                #         --------
                #         """,
                #         """
                #         -----
                #         |   |
                #         |   0
                #         | /-+-\ 
                #         |   | 
                #         |   | 
                #         |  | | 
                #         |  | | 
                #         |
                #         --------
                #         """
                # ]
                # return levels[lives]
    
def controller():
    word = random.choice(word_list).upper()
    Word(word)
while input("Play Again? (Y/N) ").upper() == "Y":
    word = random.choice(word_list).upper()
    Word(word)


if __name__ == "__main__":
    controller()


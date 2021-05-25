import random

from phrasehunter.phrase import Phrase

class Game():

    max_guesses = 5

    def __init__(self):
        self.phrases = [
            "a piece of cake",
            "beating around the bush",
            "throw in the towel",
            "dropping like flies",
            "raining cats and dogs"
        ]
        self.missed = 0
        self.active_phrase = None
        self.guesses = []
    
    def get_random_phrase(self):
        return Phrase(random.choice(self.phrases))

    def welcome(self):
        print("Welcome! Let's play a game!")
        print("I'm thinking of a phrase. Can you guess what it is?")

    def get_guess(self):
        choice = input("Input a letter: ")
        if not (choice.isalpha() and len(choice) == 1):
            print("Invalid input. Please input a single letter.")
            input("Press any key to continue.")
            return None
        
        choice = choice.lower()
        if choice in self.guesses:
            print("You have already tried that letter!")
            input("Press any key to continue.")
            return None

        self.guesses.append(choice)
        return choice


    def game_over(self, win):
        if win:
            print(f"You guessed it! My phrase was '{self.active_phrase}'. Nice! :D")
        else:
            print(f"You ran out of lives. The correct answer is '{self.active_phrase}'. Too bad. :(")

    def start(self):
        self.active_phrase = self.get_random_phrase()
        self.guesses = []
        self.missed = 0

        self.welcome()

        while True:

            print()
            print("◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇")
            print()
            self.active_phrase.display()
            print()
            print("◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇")
            
            choice = self.get_guess()
            if not choice:
                continue

            print()
            num_correct = self.active_phrase.check_letter(choice)
            if num_correct > 0:
                print(f"There were {num_correct} instance(s) of the letter '{choice}' in my phrase.")
                
                if self.active_phrase.check_complete():
                    self.game_over(True)
                    break
            else:
                self.missed += 1
                print(f"There were no instance of the letter '{choice}' in my phrase.")
                
                if self.missed > Game.max_guesses:
                    self.game_over(False)
                    break
                else:
                    print(f"You have {Game.max_guesses-self.missed} out of {Game.max_guesses} lives remaining!")
                    input("Press any key to continue.")

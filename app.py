from phrasehunter.game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        print()
        game.start()

        print()
        choice = input("Game over! Press 'N' to start a new game: ")
        if not choice.upper() == 'N':
            break
        else:
            print("Goodbye! Have a nice day!")
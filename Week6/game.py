import random
import matplotlib.pyplot as plt

class DiceGame:
    def __init__(self):
        self.earnings = 0
        self.game_active = True


    def roll_dice(self):
        if self.game_active:
            dice_value = random.randint(1, 6)
            print(f"Dice rolled: {dice_value}")
            
            if dice_value in [1, 2]:
                print("Game Over! Dice was 1 or 2.")
                self.game_active = False
            else:
                self.earnings += 4
                print(f"Current earnings: ${self.earnings}")
            
        else:
            print("Game has ended, please quit or restart.")


    def quit_game(self):
        if self.game_active:
            self.earnings += 10
            print(f"Quit game. Final earnings: ${self.earnings}")
        self.game_active = False


    def stay_in_game(self):
        self.earnings += 4
        print(f"Stayed in game. Current earnings: ${self.earnings}")


    def test_game(self, runs):
        earnings_list = []
        for i in range(runs):
            self.earnings = 0
            self.game_active = True
            while self.game_active:
                dice_value = random.randint(1, 6)
                if dice_value in [1, 2]:
                    self.game_active = False
                else:
                    self.earnings += 4
            earnings_list.append(self.earnings)
    
        plt.bar(range(1, runs + 1), earnings_list)
        plt.title(f"Earnings Over {runs} Test Runs")
        plt.xlabel("Game Number")
        plt.ylabel("Earnings")
        plt.show()



def start_game():
    game = DiceGame()
    print("Welcome to the Dice Game!")

    print("\nChoose an action:")
    print("1. Stay in the game")
    print("2. Quit the game")
    print("3. Run test")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':

        game.stay_in_game()
        
        while game.game_active:
            print("\nChoose an action:")
            print("1. Roll the dice")
            print("2. Quit the game")
            choice = input("Enter your choice (1/2): ")

            if choice == '1':
                game.roll_dice()
            elif choice == '2':
                game.quit_game()
            else:
                print("Invalid choice. Please select 1 or 2.")


    elif choice == '2':
        game.quit_game()
    elif choice == '3':
        runs = int(input("Enter number of test runs: "))
        game.test_game(runs)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    

    print(f"Game over. Your final earnings: ${game.earnings}")



if __name__ == "__main__":
    start_game()

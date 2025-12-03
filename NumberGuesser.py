import numpy as np

class NumberGuessingGame:
    def __init__(self):
        print("Welcome to the Number Guessing Game!")
        self.play_game()

    def input_range(self):
        print("Enter the range of numbers you wanna play with in:")
        while True:
            try:
                low = int(input("Enter the lower bound: "))
                high = int(input("Enter the upper bound: "))
                if low >= high:
                    print("Lower bound must be less than upper bound. Try again.")
                else:
                    return low, high
            except ValueError:
                print("Please enter valid integers.")

    def generate_random_number(self, low, high):
        self.number =  np.random.randint(low, high)
        return self.number
    
    def play_game(self):
        """Main gameplay logic"""
        while True:
            low, high = self.input_range()
            self.generate_random_number(low,high)
            attempts = 0

            print(f"\nI have chosen a number between {low} and {high}. Can you guess it?")

            while True:
                try:
                    guess = int(input("Your guess: "))
                    attempts += 1
                    if guess < self.number:
                        print("Too low!")
                    elif guess > self.number:
                        print("Too high!")
                    else:
                        print(f"Congratulations! You guessed it in {attempts} attempts.\n")
                        break
                except ValueError:
                    print("Please enter a valid integer.")

            if not self.play_again():
                break

    def play_again(self):
        """Ask if the player wants to play again"""
        while True:
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                print("Thanks for playing!")
                return False
            else:
                print("Please enter 'y' or 'n'.")



if __name__ == "__main__":
    NumberGuessingGame()

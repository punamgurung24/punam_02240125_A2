
import random
from punam_02240125_A2_PB import PokemonCardManager


class MainMenu:
    def __init__(self):
        self.score_tracker = ScoreTracker()
        self.games = {
            1: GuessNumberGame,
            2: RockPaperScissors,
            3: TriviaGame,
            4: PokemonCardGame
        }

    def display(self):
        while True:
            print("""
Select a function (0-5):
1. Guess Number game
2. Rock paper scissors game
3. Trivia Pursuit Game
4. Pokemon Card Binder Manager
5. Check Current Overall score
0. Exit program
""")
            choice = input("Enter your choice: ")
            if choice == '0':
                print("Exiting...")
                break
            elif choice == '5':
                print(f"Current total score: {self.score_tracker.get_score()}")
            else:
                try:
                    choice = int(choice)
                    game_class = self.games.get(choice)
                    if game_class:
                        game = game_class()
                        score = game.play()
                        self.score_tracker.add_score(score)
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Please enter a valid number.")

class ScoreTracker:
    def __init__(self):
        self.total_score = 0

    def add_score(self, score):
        self.total_score += max(score, 0)

    def get_score(self):
        return self.total_score


class GuessNumberGame:
    def __init__(self):
        self.secret = random.randint(1, 30)
        self.max_attempts=5
        self.max_score= 20

    def play(self):
        print("Welcome to the Guess the Number game!")
        print("please guess the number between 1 and 30")
        attempts = 0
        while attempts < self.max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 30:
                    print("invalid guess, please enter a number between 1 and 30.")
                    continue
                attempts += 1
                if guess < self.secret:
                    print("Too low!")
                elif guess > self.secret:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed it in {attempts} attempts.")
                    score = self.max_score - (attempts - 1) * (self.max_score // self.max_attempts)
                    return score
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Sorry, you've used all {self.max_attempts} attempts. The correct number was {self.secret}.")
        return 0
    
                
                
                    
class RockPaperScissors:
    def play(self):
        options = ["rock", "paper", "scissors"]
        score = 0
        print("welcome to Rock Paper Scissors game!")
        print("gain 1 point for each win and no points for a tie and loss.")
        while True:
            user = input("Enter rock, paper, or scissors (or 'exit'): ").lower()
            if user == 'exit':
                break
            if user not in options:
                print("Invalid choice. please choose rock, paper, or scissors.")
                continue
            computer = random.choice(options)
            print(f"Computer chose {computer}")
            if user == computer:
                print("It's a tie. no points awarded.")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissors" and computer == "paper"):
                print("You win!")
                score += 1
            else:
                print("You lose! no points awarded.")
                score -= 1
        return max(score, 0)  # Ensure score is not negative    

class TriviaGame:
    def __init__(self):
        self.categories = {
            "Science": [
                ("Which planet in our solar system is known as the Red planet?", ["Jupiter", "Mars", "Venus"], "Mars"),
                ("What part of the human body controls balance?", ["heart", "inner ear", "lungs"], "inner ear"),
                ("what gas do the plants absorb from the atmosphere?", ["oxygen", "carbon dioxide", "nitrogen"], "carbon dioxide")
            ],
            "Math": [
                ("75 - 45 = ?", ["30", "40", "25"], "30"),
                ("What is 12 x 8?", ["96", "88", "108"], "96"),
                ("what is the value of pi approximately?", ["3.14", "3.16", "3.12"], "3.14")
            ],
            "General Knowledge": [
                ("What is the currency of Japan?", ["Won", "Yuan", "Yen"], "Yen"),
                ("Which ocean is the largest?", ["Atlantic ocean", "Indian ocean", "Pacific ocean"], "Pacific ocean"),
                ("What is the capital of France?", ["Berlin", "Madrid", "Paris"], "Paris")
            ]
        }
        self.max_score = 6

    def play(self):
        print("Select a category:")
        categories = list(self.categories.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        try:
            category_choice = int(input("Enter your choice (1-3): "))
            if category_choice < 1 or category_choice > len(categories):
                print("Invalid category choice.")
                return 0
            selected_category = categories[category_choice - 1]
            questions = self.categories[selected_category]
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")
            return 0

        score = 0
        points_per_question = self.max_score // len(questions)
        for q, options, correct in questions:
            print(f"{q}")
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
            try:
                ans = int(input("Your choice (1-3): "))
                if options[ans - 1] == correct:
                    print("Correct!")
                    score += points_per_question
                else:
                    print(f"Wrong! Correct answer is {correct}")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a number between 1 and 3.")
        
        print(f"Your score: {score}/{self.max_score}")
        return score


class PokemonCardGame:
    def play(self):
        print("Launching Pokemon Card Binder Manager...")
        manager = PokemonCardManager()
        manager.menu()
        # Since the PokemonCardManager doesn't return a score, we'll return 0
        return 0


if __name__ == '__main__':
    MainMenu().display()
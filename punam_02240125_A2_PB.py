class PokemonCardManager:
    def __init__(self):
        self.cards = {}
        self.max_pokedex = 1025
        self.page_size = 64
        
    def get_page_position(self, pokedex_number):
       index = pokedex_number - 1
       page = index // self.page_size + 1
       position = index % self.page_size
       row = position // 8 + 1
       column = position % 8 + 1
       return page, row, column
    
    def add_card(self, number):
      if number < 1 or number > self.max_pokedex:
        return "Invalid Pokedex number."
      if number in self.cards:
        page, row, column = self.cards[number]
        return f"Card already exists at Page {page}, Row {row}, Column {column}."
      page, row, column = self.get_page_position(number)
      self.cards[number] = (page, row, column)
      return f"Card added at Page {page}, Row {row}, Column {column}."
    
    def reset_binder(self):
     while True:
        confirmation = input("Are you sure you want to reset the binder? Type 'YES' to confirm or 'NO' to cancel: ").strip().upper()
        if confirmation == "YES":
            self.cards.clear()
            print("Binder has been reset successfully.")
            break
        elif confirmation == "NO":
            print("Reset operation canceled.")
            break
        else:
            print("Invalid input. Please type 'YES' to confirm or 'NO' to cancel.")

    def view_binder(self):
     if not self.cards:
        print("The binder is empty.")
        return
     total = len(self.cards)
     percent = (total / self.max_pokedex) * 100
     for number in sorted(self.cards):
        page, row, column = self.cards[number]
        print(f"Pokedex #{number}: Page {page}, Row {row}, Column {column}")
        print(f"Total cards: {total}, Completion: {percent:.2f}%")
     if total == self.max_pokedex:
        print("Congratulations! You have caught them all!") 

    def menu(self):
        while True:
            print("\nPokemon Card Binder Manager")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            choice = input("Select an option: ")
            
            if choice == "1":
                try:
                    number = int(input("Enter Pokedex number: "))
                    result = self.add_card(number)
                    print(result)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "2":
                self.reset_binder()
            elif choice == "3":
                self.view_binder()
            elif choice == "4":
                print("Thank you for using Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid selection. Please try again.")

if __name__ == "__main__":
    manager = PokemonCardManager()
    manager.menu()



































    

    
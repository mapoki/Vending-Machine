# You are tasked to code the vending machine logic out using Python Programming Language. In 
# your code, you can have a few drinks as your items with any price (no coin). The customer should 
# be able to insert any notes to buy his preferred drinks. The outcome is to release the least amount 
# of notes back to the customer. 

class VendingMachine:
    def __init__(self):

        # Define ringgit malaysia notes
        self.notes = [1 ,5, 10, 20, 50, 100]

        # List of dictionaries representing different beverage items
        # This approach allows for easy management and retrieval information of each beverage item
        # Define drink id, name and price
        self.beverage_items= [
            {
                "DrinkID"   : 0,
                "DrinkName" : "Water",
                "DrinkPrice": 1,
            },
            {
                "DrinkID"   : 1,
                "DrinkName" : "Coca Cola",
                "DrinkPrice": 2,
            },
            {
                "DrinkID"   : 2,
                "DrinkName" : "Sprite",
                "DrinkPrice": 2,
            },
            {
                "DrinkID"   : 3,
                "DrinkName" : "A&W",
                "DrinkPrice": 2,
            },
            {
                "DrinkID"   : 4,
                "DrinkName" : "H&E",
                "DrinkPrice": 2,
            },
            {
                "DrinkID"   : 5,
                "DrinkName" : "Somersby",
                "DrinkPrice": 4,
            },
            {
                "DrinkID"   : 6,
                "DrinkName" : "Pepsi",
                "DrinkPrice": 3,
            },
        ]


    def main_menu(self):
        # Beverage Vending Machine
        print("===============================================")
        print("Beverage Vending Machine")
        print("===============================================")

        # To display list of beverages number, name and price
        for i in self.beverage_items:
            print(f"Drink No.: {i['DrinkID']}\tName: {i['DrinkName']}\tPrice: RM{i['DrinkPrice']}")

    # Function to check if drink number exist in the menu
    def select_drink(self, drink_no, paid_amount):
        beverage = self.select_drink_by_id(drink_no)
        if beverage:
            self.payment(beverage, paid_amount)
        else:
            print("Invalid Drink No.")

    def select_drink_by_id(self, drink_id):
        try:
            for item in self.beverage_items:
                if item['DrinkID'] == int(drink_id):
                    return item
        except ValueError:
            return None

    # Function to verify if amount paid is sufficient
    def payment(self, beverage, paid_amount):
        try:
            if paid_amount >= beverage['DrinkPrice']:
                change_amount = paid_amount - beverage['DrinkPrice']
                print(f"You have paid for {beverage['DrinkName']}. Your change is RM {int(change_amount)}")
                self.return_change(change_amount)
            else:
                print("Insufficient Amount Paid")
        except TypeError:
            print("Invalid note amount. Please enter a valid number.")

    # Function to return the least amount of notes back to customer
    def return_change(self, amount):
        print("Remaining Change: ")
        remaining_amount = amount
        for note in (self.notes):
            while remaining_amount >= note:
                num_notes = remaining_amount // note
                remaining_amount -= num_notes * note
                print(f"RM{note} x {int(num_notes)}")

    def start(self):
        self.main_menu()

        userSelection   = input("Select the drink number you want to buy: ")
        userAmount      = input("Insert notes: RM ")
        self.select_drink(userSelection, userAmount)

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.start()

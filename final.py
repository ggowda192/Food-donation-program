class FoodDonationProgram:
    def __init__(self):
        self.cond = True
#encapsulates the program in a class
    def is_it_ok(self, food_item):
        days_until_exp = food_item["days_until_exp"]
        visual_impairment = food_item["visual_impairment"]
        return days_until_exp > -1 and visual_impairment.lower() == "no"
#function checks if the food is good to donate an returns true if it satisfies 2 conditions
    def run_program(self):
        while self.cond:
            #program only runs when cond is true
            leftover_food_list = [
                {"item": "Spaghetti", "quantity": 2, "days_until_exp": -6, "visual_impairment": "No"},
                {"item": "Salad", "quantity": 1, "days_until_exp": 4, "visual_impairment": "Yes"},
                {"item": "Pizza", "quantity": 3, "days_until_exp": 2, "visual_impairment": "No"},
                {"item": "Soup", "quantity": 4, "days_until_exp": 2, "visual_impairment": "No"},
            ]
#innitializes the list in the run function
            for food_item in leftover_food_list:
                if self.is_it_ok(food_item):
                    print(f"{food_item['item']} is okay to donate.")
                else:
                    print(f"{food_item['item']} is not okay for donation.")
#decides swhat to tell user based of of the results of the i_it_ok function
            prog = input("Do you want to run the program again? (yes/no): ")
            if prog.lower() == "no":
                self.cond = False
            else:
                self.cond = True
#asks the user if they want to continue and decide value of cond based of the user input
# use the class and run the program
food_donation_program = FoodDonationProgram()
food_donation_program.run_program()
#sources (for synax) dad Satish and https://www.w3schools.com/python/python_classes.asp

Answers dotcom

Fundamentals Of Coding and Cloud-Naan Mudhalvan-CODES(Challenges)




Codes for Challenges
Unit I

Challenge 1.1

 Implement a recursive function to calculate the factorial of a given number





# 1.1 Implement a recursive function to calculate the factorial of a given number

def recur_factorial(n): 

   if n == 1: 

       return n 

   else: 

       return n*recur_factorial(n-1) 

# take input from the user 

num = int(input("Enter a number: ")) 

# check is the number is negative 

if num < 0: 

   print("Sorry, factorial does not exist for negative numbers") 

elif num == 0: 

   print("The factorial of 0 is 1") 

else: 

   print("The factorial of",num,"is",recur_factorial(num))



Challenge 1.2

Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.

 # 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements.


 

year = 2023

 

# To get year (integer input) from the user

# year = int(input("Enter a year: "))

 

# divided by 100 means century year (ending with 00)

# century year divided by 400 is leap year

if (year % 400 == 0) and (year % 100 == 0):

    print("{0} is a leap year".format(year))

 

# not divided by 100 means not a century year

# year divided by 4 is a leap year

elif (year % 4 ==0) and (year % 100 != 0):

    print("{0} is a leap year".format(year))

 

# if not divided by both 400 (century year) and 4 (not century year)

# year is not leap year

else:

    print("{0} is not a leap year".format(year))



Unit 2

Challenge 2.1

Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.





# 2.1 Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.
class BankAccount:

    def __init__(self, account_number, account_holder_name, initial_balance=0.0):

        self.__account_number = account_number

        self.__account_holder_name = account_holder_name

        self.__account_balance = initial_balance

 

    def deposit(self, amount):

        if amount > 0:

            self.__account_balance += amount

            print(f"Deposited ${amount:.2f} into account {self.__account_number}")

        else:

            print("Invalid deposit amount. Please deposit a positive amount.")

 

    def withdraw(self, amount):

        if amount > 0:

            if self.__account_balance >= amount:

                self.__account_balance -= amount

                print(f"Withdrew ${amount:.2f} from account {self.__account_number}")

            else:

                print("Insufficient balance. Cannot withdraw.")

        else:

            print("Invalid withdrawal amount. Please withdraw a positive amount.")

 

    def display_balance(self):

        print(f"Account {self.__account_number} balance: ${self.__account_balance:.2f}")

 

 

# Testing the BankAccount class

if __name__ == "__main__":

    # Create a BankAccount instance

    account1 = BankAccount("123456", "John Doe", 1000.0)

 

    # Deposit money

    account1.deposit(500.0)

 

    # Withdraw money

    account1.withdraw(200.0)

 

    # Display balance

    account1.display_balance()

 

Challenge 2.2

 Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.





#2.2 Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.

# Define the Player class

class Player:

    def play(self):

        print("The player is playing cricket.")

# Define the Batsman class, derived from Player

class Batsman(Player):

    def play(self):

        print("The batsman is batting.")

# Define the Bowler class, derived from Player

class Bowler(Player):

    def play(self):

        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes

batsman = Batsman()

bowler = Bowler()

# Call the play() method for each object

batsman.play()

bowler.play()



UNIT 3

Challenge3.1

Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.





#include <iostream>

#include <vector>

#include <string>

 

std::vector<int> linear_search_product(const std::vector<std::string>& product_list, const std::string& target_product) {

    std::vector<int> indices;

 

    for (int i = 0; i < product_list.size(); ++i) {

        if (product_list[i] == target_product) {

            indices.push_back(i);

        }

    }

 

    return indices;

}

 

int main() {

    std::vector<std::string> products = {"apple", "banana", "apple", "orange", "apple"};

    std::string target = "apple";

    std::vector<int> result = linear_search_product(products, target);

 

    if (result.empty()) {

        std::cout << "Product not found." << std::endl;

    } else {

        std::cout << "Product found at indices: ";

        for (int index : result) {

            std::cout << index << " ";

        }

        std::cout << std::endl;

    }

 

    return 0;

}

 

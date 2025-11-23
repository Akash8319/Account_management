# Account_management
using some techinal terms for making account management.

__init__  --- self, Name, Balance, Account_no	---Constructor method. Initializes the object attributes and an empty history list.
debit ---	self, amount  ---	Withdraws money. Prints an error if amount <= 0 or if amount > balance.
credit ---	self, amount ---	Deposits money. Increases self.balance.
get_balance	self ---	Returns the current integer value of the balance.
__str__	self ---	Returns a formatted string: "Account Holder: {name}..."

Here user give account number, Name, Balance
After that  all transations store here..
And give Total Amount

how to run method:
# user: account(Name, Opening_Balance, Account_Number)
user = account("Akash", 5000, "HDFC123456")

# Add money
user.credit(1000) 

# Withdraw money
user.debit(500)   

# Check Balance
current_bal = user.get_balance()

Rs. 200000 was Credited
total balance = 210000
Rs. 5000 was debited
total balance = 205000
Insufficient Balance
Rs. 500000 was Credited
total balance = 705000
Account Holder: Akash, Account No: SBI00254012, Balance: Rs. 705000

Rs. 100000 was Credited
total balance = 300000


#  Python Banking System Simulation

A robust Python script demonstrating Object-Oriented Programming (OOP) principles through a simulated banking environment. This project models bank accounts with features for deposits, withdrawals, balance tracking, and account validation.


## Overview

This project serves as a fundamental example of how **Classes** and **Objects** work in Python. It encapsulates user data (Name, Account Number, Balance) and behaviors (Debits, Credits) into a single `account` class. It is designed to handle multiple unique user instances simultaneously.

## Features

* **Account Initialization:** Create unique accounts with a Name, Starting Balance, and Account Number.
* **Secure Debiting:**
    * Validates that withdrawal amount is positive.
    * **Overdraft Protection:** Prevents withdrawing more funds than currently available.
* **Crediting:** Adds funds to the account seamlessly.
* **State Management:** Tracks the balance in real-time after every transaction.
* **String Representation:** Custom `__str__` method for instant account summaries.


## Getting Started

### Prerequisites
* Python 3.6 or higher installed on your system.

### Installation
1.  Clone this repository or download the `account-management.py` file.
2.  Open your terminal or command prompt.
3.  Navigate to the directory containing the file.

### Running the Script
Execute the file using the python command:
```bash
python account-management.py
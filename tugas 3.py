# Define a dictionary of valid accounts and their corresponding service costs
ACCOUNTS = {
    "1234": 100.0,
    "5678": 50.0,
    "9012": 75.0
}

# Get the customer's account number from input
account_number = input("Enter your account number: ")

# Check if the account number is valid
if account_number in ACCOUNTS and ACCOUNTS[account_number] > 0:
    # If valid, produce the invoice containing account number and service cost
    print(f"Invoice for account number {account_number}: ${ACCOUNTS[account_number]:.2f}")
else:
    # If invalid, produce an error message
    print("Error: Invalid account number or status code")

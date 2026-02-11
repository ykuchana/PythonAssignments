balance = 0
kyc_documents = {}

def line_filler():
    print('-' * 100)

def empty_filler():
    print()

def check_balance():
    global balance
    print(f"Your savings account balance: {balance}")

def deposit(amt):
    if amt < 0:
        print("Amount cannot be deposited to your account. Amount should be higher than zero.")
    else:
        global balance
        balance += amt
        print(f"An amount of {amt} was deposited to your account.")
        print(f"The updated balance of your account is {balance}")

def withdraw(amt):
    global balance
    if amt > balance:
        print(f"To withdraw, please enter lower amount than {balance}.")
    elif amt <= 0:
        print("Cannot withdraw negative or zero amount.")
    else:
        balance -= amt
        print(f"You have successfully withdrawn {amt} from account.")
        print(f"The updated balance of your account is {balance}")

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    global kyc_documents
    if len(kyc_documents) == 0:
        print("KYC is not done or pending. Kindly update your KYC to enjoy our services without interruption.")
    else:
        print("Your KYC documents are as listed below:")
        for doc in kyc_documents:
            print(f"{doc}: {kyc_documents[doc]}")

line_filler()
empty_filler()
print(" Welcome to Bank of Giri. ".center(100, " "))
empty_filler()
line_filler()

if __name__ == "__main__":
    while True:
        print("We provide the below services in our bank.")
        print("1. Check you balance")
        print("2. Deposit an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")

        line_filler()
        choice = input("Enter any one choice mentioned above (1 - 4): ")
        line_filler()

        if choice == "1":
            check_balance()
            line_filler()
        elif choice == "2":
            amt = float(input("Enter an amount to deposit into your account: "))
            deposit(amt)
            line_filler()
        elif choice == "3":
            amt = float(input("Enter an amount to withdraw from your account: "))
            withdraw(amt)
            line_filler()
        elif choice == "4":
            check_kyc()
            line_filler()
        elif choice == "5":
            kyc_docs = {}
            n_documents = int(input("Enter number of documents you want to update: "))
            empty_filler()
            for d in range(n_documents):
                key = input("Enter the type of document: ")
                value = input("Enter the document number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            empty_filler()
            print("KYC updated. Thank you!")
            line_filler()
        elif choice == "6":
            break
        else:
            print("Invalid input. Please try again.")
            line_filler()
    empty_filler()
    print("Thank you for banking with us! Have a great day!".center(100, " "))
    empty_filler()
    line_filler()
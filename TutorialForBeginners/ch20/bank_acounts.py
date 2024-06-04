# create our classes
class BalanceException(Exception):
    pass


class BankAccount:
    # initialize the class with some default in vales
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName

        print(f"\nAccount'{self.name} created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nBalance of account {self.name} is ${self.balance:.2f}")

    def depositAmount(self, depositAmount):
        self.balance += depositAmount
        print("Deposit complete")
        # call getBalance to find the amount
        self.getBalance()

    # create a method that will check balance before processing withdraw
    def balanceCheck(self, amount):
        # get amount and see if there is enough to complete else raise error
        if self.balance >= amount:
            # there is enough to complete the withdraw
            return
        else:
            raise BalanceException(
                f"\nInsufficient funds available to complete withdraw. Only '{self.balance:2f} available'"
            )

    def withdrawAmount(self, withdrawAmount):
        # use of the try/except to test for possible error due to funds available
        try:
            # check if there is enough to complete the transaction
            self.balanceCheck(withdrawAmount)
            self.balance -= withdrawAmount
            print(f"\nYou have withdrawn {withdrawAmount}")
            print("Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")

    def transferMoney(self, amount, account):
        try:
            print("\n**********\nBeginning Transfer:\n")
            self.balanceCheck(amount)
            self.withdrawAmount(amount)
            account.depositAmount(amount)
            print("\nTransfer complete.")
            print("\n*********\n")
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")


# create a new class with inheritance from the original calss
class IntrestRewards(BankAccount):
    # pass in the parent we are inheriting from but no new properties.
    # def __init__(self, initialAmount, acctName):
    #     super().__init__(initialAmount, acctName)

    # this will override the deposit amount
    def deposit(self, depositAmount):
        self.balance = self.balance + (depositAmount * 1.05)
        print("Deposit compete.")

        # call balance
        self.getBalance()


class SavingsAccount(IntrestRewards):
    # This will add a new property
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)

        # add a new property onto the new class
        # this will subtract $5 anytime there is a withdraw
        self.fee = 5

    # override the withdraw method
    def withdrawAmount(self, withdrawAmount):
        # use of the try/except to test for possible error due to funds available
        try:
            # check if there is enough to complete the transaction
            self.balanceCheck(withdrawAmount)
            self.balance -= withdrawAmount + self.fee
            print(
                f"\nYou have withdrawn {withdrawAmount} and have been charged a ${self.fee:.2f}"
            )
            print("Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interupted: {error}")

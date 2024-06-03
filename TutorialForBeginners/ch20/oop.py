# use of import * means import everything
from bank_acounts import *

Bob = BankAccount(100000, "Bob")
Sam = BankAccount(1000, "Sam")

# run the file to generate the initial creation/deposit messages

Bob.getBalance()

Bob.depositAmount(5000)

Bob.getBalance()


Bob.withdrawAmount(75000000000000)

Bob.withdrawAmount(244)

Bob.transferMoney(99999999999999999, Sam)
Bob.transferMoney(12345, Sam)

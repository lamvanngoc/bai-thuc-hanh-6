class Bank:
    Account_type = 'Savings'
    location = 'Guntur'
    def __init__(self, name, Account_Number,balance):
        self.name=name
        self.Account_Number=Account_Number
        self.balance=balance
        self.Account_type=Bank.Account_type
        self.location=Bank.location
    def __repr__(self):
        print('Welecome to the SBI ATM Machine')
        print('-------------------------------')
        account_pin = int(input('Please enter your pin number'))
        if (account_pin==123):
            Account(self)
        else:
            print('Pin Incorrect. Please try again')
            Error(self)
        return ' '.join([self.name,self.Account_Number])

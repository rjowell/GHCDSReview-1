class BankAccount:

  def deposit(self,amountToDepost):
    self.balance += amountToDepost

  def withdraw(self,amountToDepost):
    self.balance -= amountToDepost
  
  def __init__(self,_name,_phoneNumber,_address,_eMail,_isChecking):
    self.phone = _phoneNumber
    self.eMail = _eMail
    self.name = _name
    self.address = _address
    self.balance = 0
    self.checking = _isChecking


'''
Account Class
-Name
-Phone Number
-Account Number
-Address
-Email
-All new accounts start with a balance of 0
-Type Of Account.: Credit, Checking, Savings
'''
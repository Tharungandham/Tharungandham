#bank withdrawl
class InsufficientFunds(Exception):
  pass
class BankWithdraw:
  def __init__(self):
    self.balance=0
  def deposit(self,damount):
    try:
      if damount>=0:
        self.balance+=damount
        print("your account credited with :",self.balance)
      else:
        raise ValueError("please deposite the correct amount")
    except Exception as e:
        print("inbuilt exception :",e)
  def withdraw(self):
    try:
      amount=float(input("enter the amount to withdraw :"))
      if amount<=self.balance:
        self.balance-=amount
        print("remaining balance :",self.balance)
      else:
        raise InsufficientFunds("insufficient funds in your account")
    except Exception as e:
        print("inbuilt exception :",e)
if __name__=="__main__":
  bw=BankWithdraw()
  bw.deposit(5000)
  bw.withdraw()

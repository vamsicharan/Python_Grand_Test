



class Bank_Account:
    def __init__(self,name,balance,pin,account_status,Atm_req = None,Check_book = None):
        self.name = name
        self.balance = balance
        self.__pin = pin 
        self.account_status = account_status 
        self.Atm_req = Atm_req
        self.Check_book = Check_book

    
    


    def pin_validation(self,user_pin):   
        return user_pin == self.__pin
    
    def Check_balance(self,user_pin):
        if self.pin_validation(user_pin): 


            if True:
                print(f"Your current balance is {self.balance}")
                
            else:
                print("Your account was inactive ")    
        else:
            print("you have entered wrong password !") 
            
    def deposit(self,d_amount):
        if self.pin_validation(user_pin):
            if d_amount > 0 :
                self.balance += d_amount
                print(f"{d_amount} has been deposited to your account successfully")
            else:
                print("please enter deposit amount more than zero")    
        else:
            print("you have entered wrong password")               
 
class Savings_Acc(Bank_Account):
    def __init__(self,name,balance,pin,account_status):
        super().__init__(name,balance,pin,account_status)
    
    def with_draw(self,w_amount,w_limit):
        if self.pin_validation(user_pin):
            if self.account_status != "frozen":
                if w_amount <= self.balance and w_amount <= w_limit:
                    self.balance -= w_amount
                    print(f"Your withdrawl of {w_amount} is successful. Your new balance is {self.balance}")
                else:
                    print("Insufficient Balance")
            else:
                print("your account has been frozen please make it as active account ")        
        else:
            print("you have entered wrong password ")            
        
    
       
    
    def Atm_request(self):
        pass
    
    def freeze_account(self):
        pass
    def unfreeze_account(self):
        pass
    
class Business_Acc(Bank_Account):
    def __init__(self,name,balance,pin,account_status):
        super().__init__(name,balance,pin,account_status)
    
    def withdraw_amount(self,w_amount,Overdraft_limit):
        if self.pin_validation(user_pin):
            if w_amount <= (self.balance + Overdraft_limit):
                self.balance -= w_amount
                print(f"Your withdrawl of {w_amount} is successful. Your new balance is {self.balance}")
        else:
            print("you have entered wrong password")        
    
    def request_loan(self,loan_amt):
        pass
    
    def check_book_req(self):
        pass  
    
# savings account
savings = Savings_Acc("John",5000,"1234","active")
user_pin = input("Enter your pin to proceed further : ")
savings.Check_balance(user_pin)
 
d_amount = int(input("Enter the amount to be deposited : "))
 
savings.deposit(d_amount)
w_amount = int(input("Enter the amount to be withdrawn : "))  
savings.with_draw(w_amount,5000)


# business account
business = Business_Acc("Alice",10000,"5678","active")
user_pin = input("Enter your pin to proceed further : ")
business.Check_balance(user_pin)  
d_amount = int(input("Enter the amount to be deposited : "))
business.deposit(d_amount)
w_amount = int(input("Enter the amount to be withdrawn : ")) 
business.withdraw_amount(w_amount,2000)

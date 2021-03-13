#write a money transfer program for bank where one customer can transfer money to another customer 

# declare bank class
class Bank():
    
    # constructor
    def __init__(self):
        
        # data member / instance variable
        self.bal = 50000

    # member method
    def balance(self):
        print('Your Account Balace is =>',self.bal)
        
    # member method
    def details(self):
        self.acc = input('Enter Account No. of Receiver ->')
        
    # member method
    def cvvCheck(self):
        
        # accept cvv from user
        self.cvv = input('Enter Your CVV ->')
        
        # verify cvv
        if self.cvv == '123':
            return 'cvv ok'
        else:
            return 'cvv block'
        
    # member method
    def pinCheck(self):
        
        # accept pin from user
        self.pin = input('Enter Your Pin ->')
        
        # verify pin
        if self.pin == '789':
            return 'pin ok'
        else:
            return 'pin block'

    # member method
    def transfer(self):
        
        # accept amount to transfer
        self.rs = int(input('Enter Amount to Transfer:'))
        
        # check if balance is greater than amount want to transfer
        if self.rs > self.bal:
            print('Insufficient Balance')
        else:
            self.bal = self.bal-self.rs
            print('Money Transfered Successfully')
            print('Your Current Balance is -> ',self.bal)
        
# declare function       
def m():
    
    # create an object of Bank class
    b = Bank()
    print('Welcome to HDFC Bank')
    
    # check for user id and password
    while True:
        un = input('Enter your username ->')
        p = input('Enter your password ->')
        if un == 'omkar' and p == '456':
            print('Congratulations...!')
            print('Sucessfully logged in to your Bank Account')
            break
        else:
            print('Wrong User id or Password')
            print('Try again')
    
    
    print('1 for Balance')
    print('2 for Transfer')
    print('3 for Exit')
    while True:
        
        # accept choice of user
        ch = int(input('Enter you Choice ->'))
        
        # check balance
        if ch == 1:
            b.balance()
            
        # check pin,cvv details then transfer
        elif ch == 2:
            b.details()
            a = b.cvvCheck()
            if a == 'cvv ok':
                print('CVV Verified')
            else:
                print('Transfer Blocked Wrong CVV') 
                break
            p = b.pinCheck()
            if p == 'pin ok':
                print('Pin Verified')
            else:
                print('Transfer Blocked Wrong Pin') 
                break    
            
            # after pin,cvv verified then transfer amount
            b.transfer()
        
        # exit
        else:
            print('Logged out of your Account')
            break
m()

# Create a class for Users,
# username
# account no
# mobile no
# address
# account balance
# -> Create a class for user manager
# Manages user => Add new user, Get existing user, remove user
# -> Create a class for ATM,
# Enter account no and get user if not found then show a valid message
# Show options for user operations like creating new users, View Balance. Deposit, Withdraw, Close account, etc...
# Transaction charge: 0.5 for every operation
# Account balance limit: 10000 



from audioop import add
from itertools import count

from click import option


class Users():
    account_no_series = 1111
    def __init__(self,username,mobile_no,address,account_balance):
        self.account_no = Users.account_no_series
        self.username = username
        self.mobile_no = mobile_no
        self.address = address
        self.account_balance = account_balance
        Users.account_no_series += 1
        

class Manages():
    def __init__(self):   
        self.no_of_users = []
        
    def get_existing_user(self):
        for user in self.no_of_users:
            print(user.account_no)
    
    def remove_user(self,account_no):
        for item in self.no_of_users:
            if item[0] == account_no:
                self.no_of_users.remove(item)
                break

class Atm():
    def check_account(no_of_users,get_ac_no):
        for user in no_of_users:
            if user.account_no == get_ac_no:
                return user
        return False
                
        
                  
               
objManage = Manages() 

        


print('Welcome to India Bank')
while True:
    try:
        add_oparation = int(input('\nEnter : 0, User Module\nEnter : 1, Admin user\nEnter : 2, Quit\n'))
        if not add_oparation:
            while True:
                options = int(input('\nEnter 0: Enter Account no\nEnter 1: create new account\nEnter 2: back\n'))
                if options == 0:
                    get_ac_no = int(input('Enter account no: '))
                    get_user_obj = Atm.check_account(objManage.no_of_users,get_ac_no)
                    if get_user_obj:
                        while True:
                            add_oparation_atm = int(input('\nEnter 0:Show Account Details\nEnter 1: Deposit\nEnter 2:Withdraw\nEnter 3:Close account\nEnter 4:Back\n:'))
                            if add_oparation_atm == 0:
                                print(get_user_obj.account_no,get_user_obj.account_balance,get_user_obj.username)
                            elif add_oparation_atm == 1:
                                get_amount = int(input('Enter amount: '))
                                if int(get_user_obj.account_balance) + get_amount <= 10000:
                                        get_user_obj.account_balance = int(get_user_obj.account_balance) + get_amount  
                                else:
                                    print('Account balance limit: 10000')             
                            elif add_oparation_atm == 2:
                                get_amount = int(input('Enter amount: '))
                                if int(get_user_obj.account_balance) - get_amount - 0.5 >= 0:
                                    get_user_obj.account_balance = int(get_user_obj.account_balance) - get_amount - 0.5  
                                else:
                                    print('insufficient balance')                                  
                            elif add_oparation_atm == 3:
                                objManage.no_of_users.remove(get_user_obj)
                            elif add_oparation_atm == 4:
                                break
                    else:
                        print('not found')
                elif options == 1:
                    username = input('Enter Your Name: ')
                    mobile_no = input('Enter Your mobile no: ')
                    address = input('Enter Your adrress: ')
                    account_balance = input('Enter the amount of balance that you want to deposit: ')
                    obj = Users(username,mobile_no,address,account_balance)
                    objManage.no_of_users.append(obj)   
                elif options == 2:
                    break    
        elif add_oparation == 1:
            print('admin')
        elif add_oparation == 2:
            break
        else:
            print('Please Enter only 0,1 or 2')
    except Exception as e:
        print(type(e).__name__,':',e)
        print('Please Enter only 0,1 or 2')
        
        
objManage.get_existing_user()
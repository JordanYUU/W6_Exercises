class RewardsProgram:
    '''Rewards program for restaurants'''
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
    
    def profile(self):
        print(f'{self.cust_name}, {self.phone}, {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name} for visiting our restaurant!')

    def add_to_cust_list(self):
        cust_list = ['{self.cust_name}', '{self.phone}', '{self.email}']
        print(cust_list)

cust_1 = RewardsProgram('TJ Kreen', '877-1500', 'KreenMachine@gmail.com')
cust_2 = RewardsProgram('Glub Tubbis Wepple', '222-2222', 'Fren@yahoo.com')
cust_3 = RewardsProgram('GuyMan', '102-512-5921', 'OrdinaryGuy@outlook.com')

cust_1.add_to_cust_list()
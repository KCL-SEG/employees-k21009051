"""Employee pay calculator."""

class Employee:
    def __init__(self,name,contract_type,commission_type):
        self.name = name
        self.contract_type = contract_type
        self.commission_type = commission_type

        self.hours_worked = 0
        self.hourly_rate = 0
        
        self.monthly_salary = 0

        self.number_of_contracts = 0
        self.contract_rate = 0
        
        self.bonus_commission = 0

        self.contract_pay = 0
        self.commission_pay = 0

        self.contract_name = ''
        self.commission_name = ''

    def get_contract_pay(self):
        if self.contract_type == 'Monthly':
            return self.monthly_salary
        elif self.contract_type == 'Hourly':
            return self.hours_worked * self.hourly_rate
        else:
            return 0

    def get_pay(self):
        self.contract_pay = self.get_contract_pay()
        self.commission_pay = self.get_commission_pay() 

        return self.contract_pay + self.commission_pay

    def __str__(self):
        if self.contract_type == 'Monthly':
            self.contract_name = f'monthly salary of {self.monthly_salary}'
        elif self.contract_type == 'Hourly':
            self.contract_name = f'contract of {self.hours_worked} hours at {self.hourly_rate}/hour'
        else:
            self.contract_name == ''

        if self.commission_type == 'Bonus':
            self.commission_name = f' and receives a bonus commission of {self.bonus_commission}'
        elif self.commission_type == 'Contract':
            self.commission_name = f' and receives a commission for {self.number_of_contracts} contract(s) at {self.contract_rate}/contract'
        else:
            self.commission_name = ''

        return f'{self.name} works on a {self.contract_name}{self.commission_name}.  Their total pay is {self.get_pay()}.'


    def get_commission_pay(self):
        if self.commission_type == 'Bonus':
            return self.bonus_commission
        elif self.commission_type == 'Contract':
            return self.number_of_contracts * self.contract_rate
        else:
            return 0


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie','Monthly',None)

billie.monthly_salary = 4000

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie','Hourly',None)

charlie.hours_worked = 100
charlie.hourly_rate = 25

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','Monthly','Contract')

renee.monthly_salary = 3000

renee.number_of_contracts = 4
renee.contract_rate = 200

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','Hourly','Contract')

jan.hours_worked = 150
jan.hourly_rate = 25

jan.number_of_contracts = 3
jan.contract_rate = 220

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','Monthly','Bonus')

robbie.monthly_salary = 2000

robbie.bonus_commission = 1500 

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel','Hourly','Bonus')

ariel.hours_worked = 120
ariel.hourly_rate = 30

ariel.bonus_commission = 600

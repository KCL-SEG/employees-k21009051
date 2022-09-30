"""Employee pay calculator."""

class Employee:
    def __init__(self,name,contract,commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.ans + self.commission.ans

    def __str__(self):
        return f'{self.name} works on a {self.contract.get_contract_string()}{self.commission.get_commission_string()}.  Their total pay is {self.get_pay()}.'


#QUESTION: Is there a more efficient way of simulating multiple constructors?? 
class Commission():
    def __init__(self,*args):
        if len(args) == 2:
            self.ans = self.calculate_contract_pay(args)
            self.commission_string = f' and receives a commission for {args[0]} contract(s) at {args[1]}/contract'
        elif len(args) == 1:
            self.ans = self.calculate_bonus_pay(args)
            if args[0] != 0:
                self.commission_string = f' and receives a bonus commission of {args[0]}'
            else:
                self.commission_string = ''

    def calculate_contract_pay(self,args):
        return args[0] * args[1]

    def calculate_bonus_pay(self,args):
        return args[0]

    def get_commission_string(self):
        return self.commission_string


class Contract():
    def __init__(self,*args):
        if len(args) == 2:
            self.ans = self.calculate_hourly_pay(args)
            self.contract_string = f'contract of {args[0]} hours at {args[1]}/hour'
        elif len(args) == 1:
            self.ans = self.calculate_monthly_pay(args)
            self.contract_string = f'monthly salary of {args[0]}'

    def calculate_monthly_pay(self,args):
        return args[0]

    def calculate_hourly_pay(self,args):
        return args[0] * args[1]

    def get_contract_string(self):
        return self.contract_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_contract = Contract(4000)
billie_commission = Commission(0)
billie = Employee('Billie',billie_contract,billie_commission)
print(billie.get_pay())
print(billie.__str__())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_contract = Contract(100,25)
charlie_commission = Commission(0)
charlie = Employee('Charlie',charlie_contract,charlie_commission)
print(charlie.get_pay())
print(charlie.__str__())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract = Contract(3000)
renee_commission = Commission(4,200)
renee = Employee('Renee',renee_contract,renee_commission)
print(renee.get_pay())
print(renee.__str__())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract = Contract(150,25)
jan_commission = Commission(3,220)
jan = Employee('Jan',jan_contract,jan_commission)
print(jan.get_pay())
print(jan.__str__())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_contract = Contract(2000)
robbie_commission = Commission(1500)
robbie = Employee('Robbie',robbie_contract,robbie_commission)
print(robbie.get_pay())
print(robbie.__str__())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_contract = Contract(120,30)
ariel_commission = Commission(600)
ariel = Employee('Ariel',ariel_contract,ariel_commission)
print(ariel.get_pay())
print(ariel.__str__())

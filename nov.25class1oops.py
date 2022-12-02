class Andhrabank:
    def __init__(self, name, balance, savings, withdraw, deposit):
        self.cname = name
        self.cbalance = balance
        self.csavings = savings
        self.cwithdraw = withdraw
        self.cdeposit = deposit


    def cust_name(self):
        print(self.cname)

    def cust_balance(self):
        print(self.cbalance)

    def cust_savings(self):
        print(self.csavings)

    def cust_withdraw(self):
        print(self.cwithdraw)

    def cust_deposit(self):
        print(self.cdeposit)

a1 = Andhrabank("chandu", 30000, 15000, 10000, 50000)
b1 = a1.cust_name()
a1.cust_withdraw()

a2 = Andhrabank("hemu", 50000, 30000, 20000, 15000)
a2.cust_name()
a2.cust_withdraw()
#print('a1 is %{b1}, and a1 is %{1}')



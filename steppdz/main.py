class client:
    def __init__(self, name, addresses):
        self.name = name
        self.addresses = addresses

class Rahunok:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def replenish_account(self, syma):
        self.balance += syma

    def зняти_гроші(self, syma):
        if self.balance >= syma:
            self.balance -= syma
        else:
            print("Insufficient funds on your account")

client = client("Den Well", "Dnipro")
Rahunok = Rahunok("1234567890", 1000)

print(client.name)
print(Rahunok.account_number)
print(Rahunok.balance)

Rahunok.replenish_account(500)
print(Rahunok.balance)

Rahunok.withdraw_money(200)
print(Rahunok.balance)
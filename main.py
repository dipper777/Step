class CurrencyConverter:
    def __init__(self):
            self.exchange_rate = 41.23

        def convert_to_usd(self, amount):
            return amount * self.exchange_rate

conventer = CurrencyConverter()
amount_usd = float(input("Введіть кількість валюти в UAH: "))
amount_usd = conventer.convert_to_usd(amount_UAH)
print(f"{amount_UAH} UAH = {amount_usd} USD")
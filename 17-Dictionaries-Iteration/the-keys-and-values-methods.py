cryptocurrency_prices = {
    "Bitcoin": 400000,
    "Ethereum": 7000,
    "Litecoin": 10
}

print(cryptocurrency_prices.keys())
print(type(cryptocurrency_prices.keys()))

print(cryptocurrency_prices.values())
print(type(cryptocurrency_prices.values()))

for currency in cryptocurrency_prices.keys():
    print(f"The next currency is {currency}")

for price in cryptocurrency_prices.values():
    print(f"The next price is {price}")

print("Bitcoin" in cryptocurrency_prices.keys())  # Bool returned
print("Ripple" in cryptocurrency_prices.keys())   # Bool returned

print(400000 in cryptocurrency_prices.values())   # Bool returned
print(5000 in cryptocurrency_prices.values())     # Bool returned

print(len(cryptocurrency_prices.keys()))          # 3 keys
print(len(cryptocurrency_prices.values()))        # 3 values
print(len(cryptocurrency_prices))                 # 3 key/value pairs

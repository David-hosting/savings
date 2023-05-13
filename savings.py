BALANCE : float = 0 
INVESTMENT_TIME_MONTHS : int = None
starting_money : float = None

INTREST_RATE = 1 + (1.84 / (100 * 12))

account_settings : dict = {
    'ir' : INTREST_RATE,
    "Balance" : BALANCE,
    "Investment time" : INVESTMENT_TIME_MONTHS
}

while starting_money is None:
    try:
        starting_money = float(input("Enter your starting money: "))
        BALANCE += starting_money
        break
    except ValueError:
        print("Incorrect use of input, please try again.", end="\n")
        continue

while INVESTMENT_TIME_MONTHS is None:
    try:
        INVESTMENT_TIME_YEARS = int(input("Enter time of investment in years: "))
        INVESTMENT_TIME_MONTHS = 12 * INVESTMENT_TIME_YEARS
        break
    except ValueError:
        print("Incorrect use of input, please try again.", end="\n")
        continue

account_settings['Balance'] = BALANCE
account_settings['Investment time'] = INVESTMENT_TIME_MONTHS

if account_settings['Investment time'] >= 36:
    BALANCE += 550

for _ in range(account_settings['Investment time']):
    BALANCE *= INTREST_RATE
account_settings['Balance'] = BALANCE
print(f"New balance: {round(account_settings['Balance'], 2)}")

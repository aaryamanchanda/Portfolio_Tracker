import json
import os
import time

my_portfolio = {} 
market_prices = {}

def load_our_data():
    if os.path.exists('user_portfolio.json'):
        print("-> Found your save file. Loading...")
        file = open('user_portfolio.json', 'r')
        data = json.load(file)
        file.close()
        return data
    else:
        print("-> No save file found. Starting fresh!")
        return {}

def save_our_work():
    file = open('user_portfolio.json', 'w')
    json.dump(my_portfolio, file, indent=2)
    file.close()
    print("-> (Saved successfully)")

def check_market_prices():
    if os.path.exists('market_data.json'):
        file = open('market_data.json', 'r')
        prices = json.load(file)
        file.close()
        return prices
    else:
        fake_data = {"AAPL": 150.00, "GOOG": 2800.50, "TSLA": 750.25}
        file = open('market_data.json', 'w')
        json.dump(fake_data, file)
        file.close()
        return fake_data


def buy_some_stock():
    print("\n--- Let's Buy Some Stock ---")
    
    symbol = input("Which stock symbol do you want? (e.g. AAPL): ").strip().upper()

    if symbol not in market_prices:
        print(f"Oh no! We don't have pricing info for '{symbol}'.")
        print("Please check your spelling or add it to market_data.json")
        return

    price_right_now = market_prices[symbol]
    print(f"Great choice. {symbol} is currently trading at ${price_right_now}")

    amount_to_buy = int(input("How many shares do you want to buy? "))

    if symbol in my_portfolio:
        amount_we_had = my_portfolio[symbol]['quantity']
        price_we_paid_originally = my_portfolio[symbol]['avg_price']

        old_total_value = amount_we_had * price_we_paid_originally
        new_purchase_value = amount_to_buy * price_right_now
        
        total_shares = amount_we_had + amount_to_buy
        total_value = old_total_value + new_purchase_value

        new_average = total_value / total_shares

        my_portfolio[symbol]['quantity'] = total_shares
        my_portfolio[symbol]['avg_price'] = new_average
    
    else:
        my_portfolio[symbol] = {
            'quantity': amount_to_buy, 
            'avg_price': price_right_now
        }

    print(f"Success! You now own {my_portfolio[symbol]['quantity']} shares of {symbol}.")
    save_our_work()

def sell_some_stock():
    print("\n--- Let's Sell Some Stock ---")
    
    if not my_portfolio:
        print("You don't have any stocks to sell yet!")
        return

    symbol = input("Which stock do you want to sell? ").strip().upper()

    if symbol not in my_portfolio:
        print("You don't own that stock.")
        return

    amount_we_have = my_portfolio[symbol]['quantity']
    print(f"You currently have {amount_we_have} shares.")

    amount_to_sell = int(input("How many do you want to sell? "))

    if amount_to_sell > amount_we_have:
        print("You can't sell more than you have!")
        return

    current_price = market_prices.get(symbol, 0)
    price_we_paid = my_portfolio[symbol]['avg_price']
    
    profit_per_share = current_price - price_we_paid
    total_profit = profit_per_share * amount_to_sell

    print(f"Sold at ${current_price} per share.")
    if total_profit > 0:
        print(f"You made a profit of ${total_profit:.2f}! Nice work!")
    else:
        print(f"You lost ${abs(total_profit):.2f}. Better luck next time.")

    amount_remaining = amount_we_have - amount_to_sell

    if amount_remaining == 0:
        print(f"You have sold all your {symbol}.")
        del my_portfolio[symbol]
    else:
        my_portfolio[symbol]['quantity'] = amount_remaining

    save_our_work()

def show_my_portfolio():
    print("\n" + "="*30)
    print("      MY PORTFOLIO      ")
    print("="*30)

    if len(my_portfolio) == 0:
        print("It's looking a bit empty here.")
        print("Go buy some stocks!")
        return

    total_account_value = 0

    print(f"{'STOCK':<10} {'QTY':<10} {'PRICE':<10} {'VALUE':<10}")
    print("-" * 45)

    for symbol in my_portfolio:
        data = my_portfolio[symbol]
        qty = data['quantity']
        
        current_price = market_prices.get(symbol, 0)
        
        current_value = qty * current_price
        total_account_value += current_value

        print(f"{symbol:<10} {qty:<10} ${current_price:<9.2f} ${current_value:<9.2f}")

    print("-" * 45)
    print(f"TOTAL VALUE: ${total_account_value:.2f}")

print("Welcome to your Personal Stock App.")
time.sleep(1) 
my_portfolio = load_our_data()
market_prices = check_market_prices()

app_is_running = True

while app_is_running:
    print("\nWhat would you like to do?")
    print("1. See my stocks")
    print("2. Buy")
    print("3. Sell")
    print("4. Quit app")

    user_choice = input("Type a number: ").strip()

    if user_choice == '1':
        market_prices = check_market_prices()
        show_my_portfolio()
    
    elif user_choice == '2':
        market_prices = check_market_prices()
        buy_some_stock()
    
    elif user_choice == '3':
        market_prices = check_market_prices()
        sell_some_stock()
    
    elif user_choice == '4':
        print("Saving your data...")
        save_our_work()
        print("Goodbye! See you next time.")
        app_is_running = False
    
    else:
        print("I didn't understand that. Please type 1, 2, 3, or 4.")
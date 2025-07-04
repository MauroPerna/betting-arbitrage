from typing import Dict
import utils
import json


def main(test=False):
    for possible_arbitrage in utils.paginated_arbitrage_search(test=test):
        print("Markets with possible arbitrage:\n")
        for market in possible_arbitrage:
            prices = [float(bet["price"]) for bet in market["bets"]]
            stakes, profits = utils.calculate_arbitrage_bets(prices, total=100)
            min_profit = min(profits)
            if min_profit > 0:
                print(f"Market: {market['question']}")
                for outcome, stake, profit in zip(market["bets"], stakes, profits):
                    print(
                        f"  Bet ${stake:.2f} on '{outcome['outcome']}' (prob: {outcome['price']}) -> profit if wins: ${profit:.2f}")
                print(f"  Guaranteed net profit: ${min_profit:.2f}\n")
        print("="*50)


if __name__ == '__main__':
    # Run the main function with test=True to use local data
    # or test=False to fetch data from the API.
    main(test=True)

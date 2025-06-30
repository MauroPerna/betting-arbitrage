from typing import List, Dict
import requests
import json
from typing import List, Dict


def get_data(offset=0, limit=100):
    url = "https://gamma-api.polymarket.com/markets"
    response = requests.get(url, params={
        "active": "true",
        "closed": "false",
        "liquidity_min": "10000",
        "volume_min": "10000",
        "offset": offset,
        "limit": limit
    })
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(
            f"Failed to fetch data. Status code: {response.status_code}")


def get_local_data(path="data/data.json", offset=0, limit=100):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data[offset:offset+limit]


def format_data(data: List[Dict]) -> List[Dict]:
    formatted_data = []
    for item in data:
        outcomes_str = item.get("outcomes", "[]")
        outcome_prices_str = item.get("outcomePrices", "[]")
        outcomes = json.loads(outcomes_str)
        outcome_prices = json.loads(outcome_prices_str)
        bets = []
        for outcome, price in zip(outcomes, outcome_prices):
            bet = {
                "outcome": outcome,
                "price": price,
            }
            bets.append(bet)

        formatted_item = {
            "id": item.get("id"),
            "question": item.get("question"),
            "bets": bets,
        }
        formatted_data.append(formatted_item)
    return formatted_data


def exist_arbitrage(formatted_date: List[Dict]) -> bool:
    possible_arbitrage = []

    for formatted_item in formatted_date:
        outcomes = formatted_item.get("bets", [])
        if not outcomes:
            continue

        total_probability = sum(float(outcome.get("price", 0))
                                for outcome in outcomes)
        if total_probability < 1.0:
            possible_arbitrage.append(formatted_item)

    return possible_arbitrage


def paginated_arbitrage_search(limit=100, test=False, test_path="data/data.json"):
    offset = 0
    while True:
        if test:
            data = get_local_data(test_path, offset=offset, limit=limit)
        else:
            data = get_data(offset=offset, limit=limit)
        if not data:
            break

        if test:
            formatted_data = data
        else:
            formatted_data = format_data(data)
        possible_arbitrage = exist_arbitrage(formatted_data)

        if possible_arbitrage:
            yield possible_arbitrage
            break

        offset += limit


def calculate_arbitrage_bets(prices, total=100):
    prices = [float(p) for p in prices]
    numerators = [1 - p for p in prices]
    denominator = sum(numerators)
    stakes = [total * num / denominator for num in numerators]
    profits = [stake / p - total for stake, p in zip(stakes, prices)]
    return stakes, profits

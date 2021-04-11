import requests
import json


currency_cache = dict()


def get_currency_rates(currency_code):
    r = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json")
    if r:
        return json.loads(r.content)
    else:
        return None


actual_currency_code = input().upper()

all_currencies_rate = get_currency_rates(actual_currency_code)
if actual_currency_code == "USD":
    currency_cache["USD"] = 1
    currency_cache["EUR"] = all_currencies_rate["eur"]["rate"]
elif actual_currency_code == "EUR":
    currency_cache["USD"] = all_currencies_rate["usd"]["rate"]
    currency_cache["EUR"] = 1
else:
    currency_cache["USD"] = all_currencies_rate["usd"]["rate"]
    currency_cache["EUR"] = all_currencies_rate["eur"]["rate"]

while True:
    exchanged_currency_code = input().upper()
    if exchanged_currency_code == "":
        break
    amount_actual_currency = int(input())

    print("Checking the cache...")
    if exchanged_currency_code not in currency_cache:
        print("Sorry, but it is not in the cache!")
        currency_cache[exchanged_currency_code] = all_currencies_rate[exchanged_currency_code.lower()]["rate"]
    else:
        print("Oh! It is in the cache!")
    exchanged_amount = round(amount_actual_currency * currency_cache[exchanged_currency_code], 2)
    print(f"You received {exchanged_amount} {exchanged_currency_code}.")

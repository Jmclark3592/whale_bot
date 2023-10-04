import requests
import time

ETHERSCAN_API_ENDPOINT = "https://api.etherscan.io/api"
API_KEY = "BIPX43VCY7SZ6MMAMXBTSCCAAEUFUPNKHN"

def get_token_holders(contract_address, page=1, offset=50):
    params = {
        "module": "token",
        "action": "tokenholderlist",
        "contractaddress": contract_address,
        "page": page,
        "offset": offset,
        "apikey": API_KEY
    }

    response = requests.get(ETHERSCAN_API_ENDPOINT, params=params)
    data = response.json()

    if data['status'] == '1':
        return data['result']
    else:
        print(f"Error fetching data for contract {contract_address}: {data['message']}")
        return []

contract_addresses = [
    "0xe0f63a424a4439cbe457d80e4f4b51ad25b2c56c",
    "0x72e4f9f808c49a2a61de9c5896298920dc4eeea9",
    "0x24d541c86dd44bc6ce0a0511cf3146c37388ec4c"
]

for address in contract_addresses:
    holders = get_token_holders(address)
    print(holders)
    time.sleep(0.3)  # Respect rate limits (adding a delay between requests)

# Assignment # 07
# Topic : Currency converter using API

import requests
API_URL = "https://open.er-api.com/v6/latest/"

def get_exchange_rate(source, target):
    url = API_URL + source
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json() # Parse JSON response

        # Check if the API call was successful and rates are available
        if data.get("result") != "success":
            print(f"Error from API: {data.get('error-type', 'Unknown error')}")
            return None

        rates = data["rates"]
        if target not in rates:
            print("Invalid target currency code. Please use codes like USD, EUR, PKR.")
            return None

        return rates[target]

    except requests.exceptions.RequestException as error:
        print(f"Error fetching exchange rate: {error}")
        return None
    except ValueError: # Catches JSON decoding errors (e.g., if response is not valid JSON)
        print("Error: Could not decode JSON response from API.")
        return None

def main():
    source = input("Enter source currency (e.g., USD): ").strip().upper()
    target = input("Enter target currency (e.g., EUR): ").strip().upper()

    try:
        amount = float(input("Enter amount to convert: ")) # Use float for amounts
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return # Valid return, as it's inside the main function

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    rate = get_exchange_rate(source, target)

    if rate is None:
        return # Error message already printed by get_exchange_rate

    converted_amount = amount * rate

    print(f"{amount} {source} = {converted_amount:.2f} {target}")

# Run the main function when the script is executed
main()

import requests

# Define your API access key
api_key = "YOUR_API_KEY"

# Define the base URL for the Open Exchange Rates API
base_url = "https://open.er-api.com/v6/latest/USD"

# Define the currencies you want to get exchange rates for
currencies = ["EUR", "GBP", "JPY","INR"]

# Construct the URL with the API key and target currencies
url = f"{base_url}?symbols={''.join(currencies)}&apikey={api_key}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()

    # Extract the rates from the response
    rates = data["rates"]

    # Print the exchange rates
    for currency in currencies:
        print(f"1 USD = {rates[currency]} {currency}")
else:
    # If the request was not successful, print the error message
    print(f"Error: {response.status_code} - {response.text}")

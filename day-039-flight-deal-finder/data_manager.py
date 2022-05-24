import requests

# Sheety API
SHEETY_PRICES_ENDPOINT = ''
AUTH_TOKEN = ''


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {'Authorization': AUTH_TOKEN}
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        print(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        headers = {'Authorization': AUTH_TOKEN}
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(url=url, json=new_data, headers=headers)
            print(response.text)

    def update_prices(self):
        headers = {'Authorization': AUTH_TOKEN}
        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"]
                }
            }
            url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(url=url, json=new_data, headers=headers)
            print(response.text)

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = 'LON'


if sheet_data[0]['iataCode'] == '':
    # get iata codes, update google sheet
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    # get flight data
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    # compare prices
    if flight and flight.price:
        index = sheet_data.index(destination)
        prev_price = sheet_data[index]['lowestPrice']
        if int(flight.price) < int(prev_price):
            # update sheet with new price
            sheet_data[index]['lowestPrice'] = str(flight.price)
            data_manager.destination_data = sheet_data
            # send SMS notification
            notification_manager.send_sms(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )

# update google sheet
data_manager.update_prices()

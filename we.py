from weatherbit.api import Api
lat = 19.88
lon = 73.78
import time

# Function to fetch temperature data from the API
def fetch_temperature():
    lat = 19.88
    lon = 73.78
    api_key = "e0f01d11f67f49fbb7e82cff04a64263"
    api = Api(api_key)
   # api.get_forecast(lat=lat, lon=lon, days=10, tp='daily').get()
    data = api.get_forecast(lat=lat, lon=lon, hours=240, tp='hourly').get()
    # Accessing data for the first date
    first_date_data = data[0]  # Assuming 'data' is the variable containing your list of dictionaries
    temperature = first_date_data['temp']
    print(temperature)
    return temperature

# Function to control the AC based on the temperature
def control_ac(temperature_threshold):
    temperature = fetch_temperature()
    if temperature > temperature_threshold:
        # Turn on the AC
        print("Temperature is too high. Turning on the AC.")
        # Code to turn on the AC goes here
    else:
        # Turn off the AC
        print("Temperature is normal. Turning off the AC.")
        # Code to turn off the AC goes here

# Main function to run the system
def main():
    # Define the temperature threshold for turning on the AC
    temperature_threshold = 20  # Change this threshold as needed

    # Run the system continuously
    while True:
        control_ac(temperature_threshold)

        # Wait for a certain interval before checking the temperature again
        # Adjust this interval based on your requirements
        time.sleep(3600)  # 5 minutes interval

if __name__ == "__main__":
    main()

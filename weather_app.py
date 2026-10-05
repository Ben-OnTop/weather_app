#weather
import requests

def main():
    print("Welcome to the weather app")
    while True:
        choice = input("Do you wanna check the weather? (y/n): ")
        if choice.lower() in ["yes", "y"]:
            weather()
        elif choice.lower() in ["no", "n"]:
            print("Ok bye!")
            break
        else:
            print("Invalid input")


def weather():
    try:
        city = input("Choose a city: ").title()

        time = int(input("At what time (1-24): "))

        if time == 24:
            time == 0
        else:
            pass

        print("\n")

        url_city = (f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1")
        response_1 = requests.get(url_city)
        data_1 = response_1.json()


        latitude = data_1['results'][0]['latitude']
        longitude = data_1['results'][0]['latitude']
        country = data_1['results'][0]['country']
            

        url = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&models=ncep_gfs_seamless&timezone=auto&forecast_days=7")
        response_2 = requests.get(url)
        data_2 = response_2.json()


        print(country)
        print(f"time                         temperature")
        
        print(f"{data_2['hourly']['time'][time]}     -->     {data_2['hourly']['temperature_2m'][time]}°C")
        print("\n")
        
    except ValueError:
        print("Invalid city")








if __name__ == "__main__":
    main()
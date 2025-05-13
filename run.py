from geopy.geocoders import Nominatim

def coordinates_finder():
    geolocator = Nominatim(user_agent="my_user_agent")
    city = input("Enter City: ")
    while not city:
        print("Please enter a city")
        city = input("Enter City: ").lower()
    country = input("Enter Country: ").lower()
    while not country:
        print("Please enter a country: ")
        country = input("Enter Country: ").lower()
    if ValueError:
        print("\nInvalid Coordinates")
        city = input("Enter City: ").lower()
        while not city:
            print("Please enter a city")
            city = input("Enter City: ").lower()
        country = input("Enter Country: ").lower()
        while not country:
            print("\nPlease enter a country: ")
            country = input("Enter Country: ").lower()
    loc = geolocator.geocode(city+','+ country)
    print("\nlatitude is :-" ,loc.latitude, "|" " longtitude is:-" ,loc.longitude)
coordinates_finder()
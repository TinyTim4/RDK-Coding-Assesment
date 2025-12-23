import requests


def getTemp(api_eky, city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        #Find the latitude and longtitude of city first
        coords = response.json()
        if len(coords) == 0:
               print("Error: invalid city")
               return "Error"
        lat = coords[0]['lat']
        long = coords[0]['lon']
        url2 = f"https://api.openweathermap.org/data/3.0/onecall?lat={round(lat,2)}&lon={round(long,2)}&appid={api_key}"
        response2 = requests.get(url2)
        #Gets the current temperature of the city
        if response2.status_code == 200:
                data = response2.json()
                temp = data['current']['temp']
                return temp
        else:
                print(f"Error: {response2.status_code}")
                return "Error"
    else:
        print(f"Error: {response.status_code}")
        return "Error"


#API key
api_key = "12fb7fa2f05a1e82d269cb2fab163bf4"

#Stores the list of favorite cities of user
favorites = {}

#Take in user input for request
while(1):
        print("\n")
        print("Enter the number of which option you want: \n 1: Find temp of city \n 2: Add city to favorite \n 3: List Favorite Cities \n 4: Update Favorite City \n 5: Exit")
        option = int(input())
        if option == 1:
                print("Enter the city you want: ")
                city = input()
                print(f"The temperature for {city} is {getTemp(api_key, city)}") if getTemp(api_key, city) != "Error" else 0
        elif option == 2:
                if len(favorites) >= 3:
                        print("Error: Only a max of 3 cities are allowed at a time")
                else:
                        print("What city do you want to favorite?")
                        city = input()
                        favorites[city] = getTemp(api_key,city) if getTemp(api_key, city) != "Error" else 0
                        print(f"{city} has been added to favorites")
        elif option == 3:
                print("My Favorite Cities")
                for city in favorites.keys():
                        print(f"{city} : {favorites[city]}")
        elif option == 4:
                print("Which city do you want to remove?")
                city1 = input()
                if city1 in favorites:
                        #Remove city from favorites list
                        favorites.pop(city1)
                        print(f"{city1} removed \n")
                        print("What city do you want to add?")
                        city2 = input()
                        favorites[city2] = getTemp(api_key,city2) if getTemp(api_key, city) != "Error" else 0
                        print(f"{city2} has been added to favorites")
                else:
                        print("Error: City is not in your favorites list")
        elif option == 5:
               break
        else:
               print("Please input valid option.")
        
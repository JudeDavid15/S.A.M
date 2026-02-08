import requests
apikey="a4a2972687928beba0a843b906ca24c15"
CITY = "Chennai"
COUNTRY = "IN"

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY},{COUNTRY}&appid={apikey}&units=metric"
)


response=requests.get(url)
data=response.json()


# # print("Temp:", data["main"]["temp"], "°C")
# print("Weather:", data["weather"][0]["main"])
weather = data["weather"][0]

print("Condition:", weather["main"])
print("Description:", weather["description"])

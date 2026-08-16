
class WeatherExpert:
    def __init__(self, temp, humidity, wind, sky, pressure):
        self.temp = temp
        self.humidity = humidity
        self.wind = wind
        self.sky = sky
        self.pressure = pressure


    def forecast(self):
        result = []

        if self.sky == "clear" and self.humidity < 40:
            result.append("Sunny day expected.")
        if self.sky == "cloudy" and self.humidity >= 70:
            result.append("High chance of rain.")
        if self.pressure < 1000 and self.wind > 40:
            result.append("Storm warning!")
        if self.temp > 35:
            result.append("Heatwave alert.")
        if self.temp < 5:
            result.append("Cold wave alert.")
        if self.wind > 60:
            result.append("High wind advisory.")

        if not result:
            result.append("Weather appears normal.")

        return result

print("Rohit Nyaupane 4th sem CSIT")

# First case
weather1 = WeatherExpert(38, 30, 20, "clear", 1005)

print("Case 1: Normal/Clear Weather")
for result in weather1.forecast():
    print("->", result)


# Second case
weather2 = WeatherExpert(22, 85, 65, "cloudy", 985)

print("\nCase 2: Stormy Weather")
for result in weather2.forecast():
    print("->", result)
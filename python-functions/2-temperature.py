def convert_to_celsius(fahrenheit):
    celcius = (5/9) * (fahrenheit - 32)
    if fahrenheit < 0:
        trimmedCelcius = round(celcius, 2)
        return trimmedCelcius
    else:
        return celcius

print(convert_to_celsius(-450))

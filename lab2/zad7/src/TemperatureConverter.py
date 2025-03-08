class TemperatureConverter():
    def celsius_to_fahrenheit(celc):
        return celc * (9/5) + 32

    def fahrenheit_to_celsius(fahr):
        return (fahr - 32) / (9/5)

    def celsius_to_kelvin(celc):
        return celc + 273.15

    def kelvin_to_celsius(celc):
        return celc - 273.15
import adafruit_dht
import board


class Dht:
    def __init__(self, pin):
        self.dhtDevice = adafruit_dht.DHT22(getattr(board, f"D{pin}"))

    def get_temperature(self):
        return self.dhtDevice.temperature

    def get_humidity(self):
        return self.dhtDevice.humidity

    def get_message(self):
        temperature_c = self.get_temperature()
        humidity = self.get_humidity()
        temperature_f = temperature_c * (9 / 5) + 32
        return f"Temp: {temperature_f} F / {temperature_c} C    Humidity: {humidity}% "

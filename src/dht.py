import adafruit_dht
import board
import time

class Dht:
    def __init__(self):
        self.dhtDevice = adafruit_dht.DHT22(board.D14)

    def get_temperature(self):
        return self.dhtDevice.temperature

    def get_humidity(self):
        return self.dhtDevice.humidity

    def get_message(self):
        return f"Temp: {self.get_temperature()} C ,Humidity: {self.get_humidity()}% "

    def loop_info(self):
        for _ in range(10):
            print(self.get_message())
            time.sleep(5)

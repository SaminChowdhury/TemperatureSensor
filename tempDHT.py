
import logging
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT22(board.D18)


dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
logging.basicConfig(filename='/home/isam/temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)

while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        logging.info('Temp={0:0.1f} C and Humidity={1:0.1f} %'.format(temperature_f, humidity))
  

    except RuntimeError as error:

        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(0.5)


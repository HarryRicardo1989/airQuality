#! /usr/bin/python3
import datetime as dt
#from bmp085 import BMP085
import os
from bme280 import *
from insertDb import InsertDB
from time import sleep, time

insertdb = InsertDB()
ultima_atualizacao = 0
db_update = time()


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(TEMPERATURA, UMIDADE, PRESSURE, ALTITUDE, SEALEVEL_PRESSURE, DEW_POINT):
    global db_update
    if not should_update(db_update, 30):
        return
    DATA = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    HOSTNAME = os.popen('hostname').read().replace("\n", "").strip()
    print(HOSTNAME)
    insertdb.InsertDB(HOSTNAME, DATA, TEMPERATURA, UMIDADE,
                      PRESSURE, ALTITUDE, SEALEVEL_PRESSURE, DEW_POINT)
    db_update = time()


if __name__ == '__main__':
    while(1):
        barometer = BME280(t_mode=BME280_OSAMPLE_8,
                           p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        temperatura = barometer.read_temperature()
        umidade = barometer.read_humidity()
        #temperatura2 = barometer.read_temperature()
        pressure = barometer.read_pressure()
        altitude = barometer.read_altitude()
        sealevel_pressure = barometer.read_sealevel_pressure(545)
        dew_point = barometer.read_dewpoint()

        #print(altitude, pressure, sealevel_pressure, temperatura, umidade)
        salva_banco(temperatura, umidade, pressure,
                    altitude, sealevel_pressure, dew_point)

        sleep(0.3)

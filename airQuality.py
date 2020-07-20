#! /usr/bin/python3
from time import sleep, time
import os
import datetime as dt
from bmp085 import BMP085
#from l3g4200d import L3G4200D
#from hmc5883l import HMC5883l
#from adx1345 import ADXL345
from insertDb import InsertDB
from read_hdc1080 import ReadHdc1080

insertdb = InsertDB()
ultima_atualizacao = 0,
db_update = compass_update = time()


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(TEMPERATURA, UMIDADE, PRESSURE, ALTITUDE):
    global db_update
    if not should_update(db_update, 2):
        return
    DATA = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    HOSTNAME = os.popen('hostname').read().replace("\n", "").strip()
    print(HOSTNAME)
    insertdb.InsertDB(HOSTNAME, DATA, TEMPERATURA, UMIDADE, PRESSURE, ALTITUDE)

    db_update = time()


if __name__ == '__main__':
    while(1):
        hdc1080 = ReadHdc1080(offsetTemp=0)
        barometer = BMP085(mode=3)
        temperatura = hdc1080.read_temp()
        umidade = hdc1080.read_humid()
        temperatura2 = barometer.read_temperature()
        pressure = barometer.read_pressure()
        altitude = barometer.read_altitude()
        sealevel_pressure = barometer.read_sealevel_pressure(altitude)
        #print(altitude, pressure, sealevel_pressure, temperatura2)
        salva_banco(temperatura, umidade, sealevel_pressure, altitude)

        sleep(0.3)

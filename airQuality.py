#! /usr/bin/python3
import datetime as dt
import os
from bme280 import *
from post_Db import POSTDB
from time import sleep, time

post_db = POSTDB()
ultima_atualizacao = 0
db_update = time()


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(temperatura_ar=0, temperatura_orvalho=0, umidade=0, pressao_local=0, pressao_nivel_mar=0, altitude=0, uva=0, uvb=0, wind_speed=0, wind_direction=0, pluviometro=0, co2=0, tvoc=0, relampago=0):
    global db_update
    if not should_update(db_update, 3):
        return
    data_hora = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = os.popen('hostname').read().replace("\n", "").strip()
    post_db.post_DB(hostname=hostname, data_hora=data_hora, temperatura_ar=temperatura_ar, temperatura_orvalho=temperatura_orvalho, umidade=umidade, pressao_local=pressao_local,
                    pressao_nivel_mar=pressao_nivel_mar, altitude=altitude, uva=uva, uvb=uvb, wind_speed=wind_speed, wind_direction=wind_direction, pluviometro=pluviometro, co2=co2, tvoc=tvoc, relampago=relampago)
    db_update = time()


if __name__ == '__main__':
    while(1):
        barometer = BME280(t_mode=BME280_OSAMPLE_8,
                           p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        temperatura_ar = barometer.read_temperature()
        umidade = barometer.read_humidity()
        #temperatura2 = barometer.read_temperature()
        pressao_local = barometer.read_pressure()
        altitude = barometer.read_altitude()
        pressao_nivel_mar = barometer.read_sealevel_pressure(545)
        temperatura_orvalho = barometer.read_dewpoint()

        #print(altitude, pressure, sealevel_pressure, temperatura, umidade)
        salva_banco(temperatura_ar=temperatura_ar, temperatura_orvalho=temperatura_orvalho, umidade=umidade,
                    pressao_local=pressao_local, pressao_nivel_mar=pressao_nivel_mar, altitude=altitude)

        sleep(0.3)

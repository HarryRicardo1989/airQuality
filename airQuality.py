#! /usr/bin/python3
import datetime as dt
import os
import serial
import math
from read_ccs import ReadCcs
from bme280 import *
from post_Db import POSTDB
from time import sleep, time

read_ccs811 = ReadCcs()
uart = serial.Serial('/dev/ttyS0', 115200)
post_db = POSTDB()
ultima_atualizacao = 0
db_update = timer_wind_speed = timerccs811 = time()
media_vel = 0
media_tvoc = 0
media_co2 = 0
n = 1
n2 = 1


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(temperatura_ar=0, temperatura_orvalho=0, umidade=0, pressao_local=0, pressao_nivel_mar=0, altitude=0, uva=0, uvb=0, wind_speed=0, wind_direction=0, pluviometro=0, co2=0, tvoc=0, relampago=0):
    global db_update
    if not should_update(db_update, 20):
        return
    data_hora = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = os.popen('hostname').read().replace("\n", "").strip()
    post_db.post_DB(hostname=hostname, data_hora=data_hora, temperatura_ar=temperatura_ar, temperatura_orvalho=temperatura_orvalho, umidade=umidade, pressao_local=pressao_local,
                    pressao_nivel_mar=pressao_nivel_mar, altitude=altitude, uva=uva, uvb=uvb, wind_speed=wind_speed, wind_direction=wind_direction, pluviometro=pluviometro, co2=co2, tvoc=tvoc, relampago=relampago)
    db_update = time()


def wind_speed():
    global timer_wind_speed
    global media_vel
    global n

    if not should_update(timer_wind_speed, 1):
        return

    try:
        raw_value = int(uart.readline().decode())
        velocidade = (raw_value * math.pi * 0.09)
        media_vel += 1/n*(velocidade-media_vel)
        n += 1
    except Exception as ex:
        print(ex)
        sleep(0.1)

    if n > 20:
        n = 1


def ccs811():
    global timerccs811
    global media_tvoc
    global media_co2
    global n2

    if not should_update(timerccs811, 1):
        return

    try:

        raw_co2, raw_tvoc = read_ccs811.read_ccs()
        media_co2 += 1/n*(raw_co2-media_co2)
        media_tvoc += 1/n*(raw_tvoc-media_tvoc)
        n2 += 1
    except Exception as ex:
        print(ex)
        sleep(0.1)

    if n2 > 20:
        n2 = 1


if __name__ == '__main__':

    while(1):
        barometer = BME280(t_mode=BME280_OSAMPLE_8,
                           p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        temperatura_ar = barometer.read_temperature()
        umidade = barometer.read_humidity()
        #temperatura2 = barometer.read_temperature()
        pressao_local = barometer.read_pressure()
        altitude = barometer.read_altitude()
        pressao_nivel_mar = barometer.read_sealevel_pressure(543)
        temperatura_orvalho = barometer.read_dewpoint()
        wind_speed()
        ccs811()

        #print(altitude, pressure, sealevel_pressure, temperatura, umidade)
        salva_banco(temperatura_ar=temperatura_ar, temperatura_orvalho=temperatura_orvalho, umidade=umidade,
                    pressao_local=pressao_local, pressao_nivel_mar=pressao_nivel_mar, altitude=altitude, wind_speed=media_vel, co2=media_co2, tvoc=media_tvoc)

        sleep(0.2)

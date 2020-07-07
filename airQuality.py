#! /usr/bin/python3
from time import sleep
from carrega_display import CarregaDisplay
from Adafruit_CCS811 import Adafruit_CCS811
import HDC1080 as SDL_Pi_HDC1000


def display_write(temperatura, humidade, co2, tvoc):
    display.display_line_0("Temperature = %3.1f C" % temperatura)
    display.display_line_1("Humidity = %3.1f %%" % humidade)
    display.display_line_2(f'CO2: {co2} ppm ')
    display.display_line_3(f'TVOC: {tvoc} ppm')


def config():
    display = CarregaDisplay(i2c_bus=1, address=0x27, numLinhas=4)
    hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000(addr=(0x40))
    ccs = Adafruit_CCS811()
    ccs.setDriveMode(0x04)
    while not ccs.available():
        pass
    return display, hdc1000, ccs


def read_ccs():
    try:
        if ccs.available():
            if not ccs.readData():
                ccs811_CO2 = ccs.geteCO2()
                ccs811_TVOC = ccs.getTVOC()
    except:
        print("erro")
        config()
    return ccs811_CO2, ccs811_TVOC


def read_hdc1080():
    humidade = hdc1000.readHumidity()
    temperatura = hdc1000.readTemperature()
    return temperatura, humidade


display, hdc1000, ccs = config()

ccs811_CO2 = None
ccs811_TVOC = None


while(1):
    temp, humid = read_hdc1080()
    co2, tvoc = read_ccs()
    display_write(temp, humid, co2, tvoc)

    sleep(0.1)

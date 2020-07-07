#! /usr/bin/python3
from carrega_display import CarregaDisplay
import HDC1080 as SDL_Pi_HDC1000
from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811


hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000(addr=(0x40))
display = CarregaDisplay(i2c_bus=1, address=0x27, numLinhas=4)
hdc1000.turnHeaterOn()
hdc1000.turnHeaterOff()
hdc1000.setTemperatureResolution(
    SDL_Pi_HDC1000.HDC1000_CONFIG_TEMPERATURE_RESOLUTION_14BIT)
hdc1000.setHumidityResolution(
    SDL_Pi_HDC1000.HDC1000_CONFIG_HUMIDITY_RESOLUTION_14BIT)

while not ccs.available():
    pass

temp = ccs.calculateTemperature()
ccs.tempOffset = temp - 25.0
i = 0
while(1):
    i = i+1
    display.display_line_0("Temperature = %3.1f C" % hdc1000.readTemperature())
    display.display_line_1("Humidity = %3.1f %%" % hdc1000.readHumidity())
    display.display_line_2(f'CO2: {ccs.geteCO2()} ppm TVOC: {ccs.getTVOC()}')
    display.display_line_3("Temperature = %3.1f C" % temp)
    sleep(0.1)

#! /usr/bin/python3
from time import sleep
from carrega_display import CarregaDisplay
from read_ccs import ReadCcs
from read_hdc1080 import ReadHdc1080
display = CarregaDisplay(i2c_bus=1, address=0x27, numLinhas=4)


if __name__ == '__main__':

    ccs = ReadCcs()
    hdc1080 = ReadHdc1080()

    while(1):
        display.display_line_0("Temperature = %3.1f C" % hdc1080.read_temp())
        display.display_line_1("Humidity = %3.1f %%" % hdc1080.read_humid())
        co2, tvoc = ccs.read_ccs()
        display.display_line_2(f'CO2: {co2} ppm ')
        display.display_line_3(f'TVOC: {tvoc} ppm')

        sleep(0.1)

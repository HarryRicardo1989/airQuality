#! /usr/bin/python3
from time import sleep, time
import datetime as dt
from insertDb import InsertDB
from carrega_display import CarregaDisplay
from read_ccs import ReadCcs
from read_hdc1080 import ReadHdc1080
display = CarregaDisplay(i2c_bus=1, address=0x27, numLinhas=4)
insertdb = InsertDB()
ultima_atualizacao = 0,
last_update = time()


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(TEMPERATURA, UMIDADE, CO2, TVOC):
    global last_update
    if not should_update(last_update, 120):
        return
    DATA = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insertdb.InsertDB(DATA, TEMPERATURA, UMIDADE, CO2, TVOC)
    last_update = time()


if __name__ == '__main__':

    ccs = ReadCcs()
    hdc1080 = ReadHdc1080()

    while(1):
        temperatura = hdc1080.read_temp()
        umidade = hdc1080.read_humid()
        display.display_line_0("Temperature = %3.2fC" % temperatura)
        display.display_line_1("Humidity = %3.2f%%" % umidade)
        co2, tvoc = ccs.read_ccs()
        display.display_line_2(f'CO2: {co2} ppm ')
        display.display_line_3(f'TVOC: {tvoc} ppm')
        salva_banco(temperatura, umidade, co2, tvoc)

        sleep(0.5)

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
ccs = None
i = 0


def should_update(last_update, rate):
    if(time() - last_update) > rate:
        return True
    return False


def salva_banco(TEMPERATURA, UMIDADE):
    global last_update
    if not should_update(last_update, 60):
        return
    DATA = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insertdb.InsertDB(DATA, TEMPERATURA, UMIDADE)
    # constr()
    last_update = time()


def verifica_horario():
    if dt.datetime.now().time() > dt.time(18, 0, 0):
        display.desliga_display()
    elif dt.datetime.now().time() > dt.time(8, 0, 0):
        display.liga_display()


if __name__ == '__main__':
    hdc1080 = ReadHdc1080(offsetTemp=-3.5)
    while(1):
        temperatura = hdc1080.read_temp()
        umidade = hdc1080.read_humid()
        display.display_line_0("Temperature = %3.2fC" % temperatura)
        display.display_line_1("Humidity = %3.2f%%" % umidade)
        salva_banco(temperatura, umidade)
        verifica_horario()
        sleep(0.3)

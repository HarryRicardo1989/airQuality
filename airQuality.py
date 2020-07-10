#! /usr/bin/python3
from time import sleep, time
import datetime as dt
from insertDb import InsertDB
from read_hdc1080 import ReadHdc1080

insertdb = InsertDB()
ultima_atualizacao = 0,
last_update = time()


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
    last_update = time()


if __name__ == '__main__':
    hdc1080 = ReadHdc1080(offsetTemp=-1.5)
    while(1):
        temperatura = hdc1080.read_temp()
        umidade = hdc1080.read_humid()
        salva_banco(temperatura, umidade)
        sleep(0.3)

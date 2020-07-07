
from Adafruit_CCS811 import Adafruit_CCS811


class ReadCcs:
    def __init__(self):
        self.__ccs = Adafruit_CCS811()
        self.__ccs.setDriveMode(0x04)
        while not self.__ccs.available():
            pass

    def read_co2(self):
        try:
            if self.__ccs.available():
                if not self.__ccs.readData():
                    ccs811_CO2 = self.__ccs.geteCO2()
                    return ccs811_CO2
        except:
            print("erro")
            return 0

    def read_tvoc(self):
        try:
            if self.__ccs.available():
                if not self.__ccs.readData():
                    ccs811_TVOC = self.__ccs.getTVOC()
                    return ccs811_TVOC
        except:
            print("erro")
            return 0

# print(ReadCcs().read_ccs())

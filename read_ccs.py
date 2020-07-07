
from Adafruit_CCS811 import Adafruit_CCS811


class ReadCcs:
    def __init__(self):
        self.__ccs = Adafruit_CCS811()
        self.__ccs.setDriveMode(0x01)
        self.__co2 = 0
        self.__tvoc = 0
        while not self.__ccs.available():
            pass

    def read_ccs(self):
        try:
            if self.__ccs.available():
                if not self.__ccs.readData():
                    self.__co2 = self.__ccs.geteCO2()
                    self.__tvoc = self.__ccs.getTVOC()
                    return self.__co2, self.__tvoc
            else:
                return self.__co2, self.__tvoc

        except:
            print("erro")
            return 0

# print(ReadCcs().read_ccs())

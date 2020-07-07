import HDC1080 as SDL_Pi_HDC1000


class ReadHdc1080:
    def __init__(self):
        self.__hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000(addr=(0x40))

    def read_temp(self):
        return self.__hdc1000.readTemperature()

    def read_humid(self):
        return self.__hdc1000.readHumidity()

# print(ReadHdc1080().read_hdc1080())

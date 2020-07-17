import smbus
import time


class L3G4200D:
    def __init__(self, i2c=1, address=0x69):
        self.__bus = smbus.SMBus(i2c)
        # L3GD20 address, 0x69
        self.__bus.write_byte_data(address, 0x20, 0x0F)
        self.__bus.write_byte_data(address, 0x23, 0x30)
        time.sleep(0.5)
        # Read X-Axis data

    def gyro_ret(self):
        data0 = self.__bus.read_byte_data(0x69, 0x28)
        data1 = self.__bus.read_byte_data(0x69, 0x29)

        xGyro = data1 * 256 + data0
        if xGyro > 32767:
            xGyro -= 65536

        # Read Y-Axis data
        data0 = self.__bus.read_byte_data(0x69, 0x2A)
        data1 = self.__bus.read_byte_data(0x69, 0x2B)

        yGyro = data1 * 256 + data0
        if yGyro > 32767:
            yGyro -= 65536

        # Read Z-Axis data
        data0 = self.__bus.read_byte_data(0x69, 0x2C)
        data1 = self.__bus.read_byte_data(0x69, 0x2D)

        # Convert the data
        zGyro = data1 * 256 + data0
        if zGyro > 32767:
            zGyro -= 65536

        return xGyro, yGyro, zGyro

import smbus
from time import sleep


class LCD(object):
    '''Classe para controle do Display LCD 16x2 ou 20x4 via I2C
    '''

    # Controle de Pinos
    ENABLE = 0x04
    BACKLIGHT_OFF = 0x00
    BACKLIGHT_ON = 0x08
    RS = 0x01
    RW = 0x02

    # Controlde de Comandos
    FUNCTION_SET = 0x20
    MODE8BITS = 0x10
    MODE4BITS = 0x00
    LINES1 = 0x00
    LINES2 = 0x08
    DOTS5X8 = 0x00
    DOTS5X10 = 0x04

    DISPLAYCONTROL = 0x08
    DISPLAYON = 0x04
    DISPLAYOFF = 0x00
    CURSORON = 0x02
    CURSOROFF = 0x00
    CURSORBLINKON = 0x01
    CURSORBLINKOFF = 0x00

    ENTRYSETMODE = 0x04
    RIGHTSHIFT = 0x02
    LEFTSHIFT = 0x00
    DISPLAYSHIFTON = 0x01
    DISPLAYSHIFTOFF = 0x00

    LCD_CLEAR = 0x01
    RETURN_HOME = 0x10

    # Endereço das Linhas
    LINE0 = 0x80
    LINE1 = 0xC0
    LINE2 = 0x94
    LINE3 = 0xD4

    def __init__(self, i2c_bus: int, address: int, mode, lines, dots, numLinhas):
        self._bus = smbus.SMBus(i2c_bus)
        self._address = address
        self._backlight = self.BACKLIGHT_ON
        self._numLines = numLinhas
        self._start(mode, lines, dots)

    def _start(self, mode, lines, dots):
        '''Processo de Inicialização do Display
        '''
        sleep(15.0 / 1E3)
        self._writeNibble(0x30)
        sleep(4.1 / 1E3)
        self._writeNibble(0x30)
        sleep(100.0 / 1E6)
        self._writeNibble(0x30)
        sleep(40.0 / 1E6)
        self._writeNibble(0x20)
        sleep(20.0 / 1E6)
        self.writeCommand(self.FUNCTION_SET | mode | lines | dots)
        sleep(4.0 / 1E6)
        self.writeCommand(self.DISPLAYCONTROL | self.DISPLAYON |
                          self.CURSOROFF | self.CURSORBLINKOFF)
        sleep(4.0 / 1E6)
        self.clear()
        self.writeCommand(self.ENTRYSETMODE |
                          self.RIGHTSHIFT | self.DISPLAYSHIFTOFF)
        sleep(40.0 / 1E6)

    def _writeNibble(self, nibble):
        '''Envia um Nibble para o Display
        '''
        self._bus.write_byte(self._address, nibble |
                             self.ENABLE | self._backlight)
        self._bus.write_byte(self._address, nibble | self._backlight)

    def writeCommand(self, cmd):
        h_nibble = (cmd & 0xF0)
        l_nibble = ((cmd & 0x0F) << 4) & 0xF0
        self._writeNibble(h_nibble)
        self._writeNibble(l_nibble)

    def writeChar(self, data):
        h_nibble = (data & 0xF0) | self.RS
        l_nibble = ((data & 0x0F) << 4) | self.RS
        self._writeNibble(h_nibble)
        self._writeNibble(l_nibble)

    def clear(self):
        self.writeCommand(self.LCD_CLEAR)
        sleep(2.0 / 1E3)

    def setPosition(self, column, line):
        address = 0
        if line == 0:
            address = self.LINE0
        elif line == 1:
            address = self.LINE1
        elif line == 2 and self._numLines == 4:
            address = self.LINE2
        elif line == 3 and self._numLines == 4:
            address = self.LINE3
        else:
            address = self.LINE0

        if self._numLines == 4:
            if column > 19:
                column = 19
        else:
            if column > 15:
                column = 15

        address += column

        self.writeCommand(address)

    def writeLine(self, string: str, line):
        self.setPosition(0, line)
        if self._numLines == 2:
            string = string.ljust(16)
        else:
            string = string.ljust(20)
        for char in string:
            self.writeChar(ord(char))

    def backLight(self, status):
        self._backlight = status
        self._bus.write_byte(self._address, status)

from lcd_12c import LCD


class CarregaDisplay:

    def __init__(self, i2c_bus=0, address=0x00, mode=LCD.MODE4BITS, lines=LCD.LINES2, dots=LCD.DOTS5X8, numLinhas=2):
        self.display = LCD(i2c_bus, address, mode, lines, dots, numLinhas)

    def display_line_0(self, string):
        self.display.writeLine(str(string), 0)

    def display_line_1(self, string):
        self.display.writeLine(str(string), 1)

    def display_line_2(self, string):
        self.display.writeLine(str(string), 2)

    def display_line_3(self, string):
        self.display.writeLine(str(string), 3)

    def clear_line_0(self):
        self.display.writeLine('', 0)

    def clear_line_1(self):
        self.display.writeLine('', 1)

    def clear_line_2(self):
        self.display.writeLine('', 2)

    def clear_line_3(self):
        self.display.writeLine('', 3)

    def desliga_display(self):
        self.display.backLight(self.display.BACKLIGHT_OFF)

    def liga_display(self):
        self.display.backLight(self.display.BACKLIGHT_ON)

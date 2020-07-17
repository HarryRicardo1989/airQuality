#! /usr/bin/python3
from time import sleep, time
import os
import datetime as dt
from bmp085 import BMP085


barometer = BMP085(mode=3)

barometer.read_pressure()

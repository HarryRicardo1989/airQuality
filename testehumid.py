import HDC1080 as SDL_Pi_HDC1000
from time import sleep

# Main Program

hdc1000 = SDL_Pi_HDC1000.SDL_Pi_HDC1000()

while True:

    print("Temperature = %3.1f C" % hdc1000.readTemperature())
    print("Humidity = %3.1f %%" % hdc1000.readHumidity())

    sleep(3.0)

import math

sealevel_pa = 1013.25
pressure = 947
T = 29.36

h1 = (10*(-28.93*(1*(T+273))*(math.log(pressure/sealevel_pa))))/10

print(h1)

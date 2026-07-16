from modules.schilthuis import *


pressure = [
    3500,
    3300,
    3000,
    2700,
    2500
]


We = schilthuis_influx(
    pressure,
    initial_pressure=3500,
    aquifer_constant=5000
)


print(We)
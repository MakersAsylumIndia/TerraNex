import serial
import time


ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2) 

print("Reading soil moisture values...")
while True:
    if ser.in_waiting:
        data = ser.readline().decode().strip()
        print(f"Soil Moisture: {data}")

import time
import board
import busio
from adafruit_mcp9600 import MCP9600

SENSOR_ADDR = 0x67

# try different frequency values if you get an i2c input/output error
i2c = busio.I2C(board.SCL, board.SDA, frequency=200000)

try:
    device = MCP9600(i2c,SENSOR_ADDR,"K")
    print("version:", device.version)
    while True:
        print((
            device.ambient_temperature,
            device.temperature,
            device.delta_temperature
        ))
        time.sleep(1)
except ValueError:
    print("MCP9600 sensor not detected")

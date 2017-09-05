from machine import UART
import os

# Duplicate terminal to debug port
uart = UART(0, 115200)
os.dupterm(uart)

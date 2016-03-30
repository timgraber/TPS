
#!/usr/bin/python
# Author:Tim Graber
# 2016-03-17
# Revision 1.0

# AS5048B Magnetic Position Sensor
# I2C bus
# This script changes the I2C address. Total of four different addresses

#
import sys
import smbus
import time
#
i2caddress=0x4C
error_status=0x0F
readings=0xFA
i2c_register=0x15
agc_register=0xFA
diag=0xFB
mag_msb=0xFC
mag_lsb=0xFD
angle_msb=0xFE
angle_lsb=0xFF
i2c_newaddr=0x00 # Change this value to 0x01, 0x10 or 0x11

# Read registers
try:
        bus=smbus.SMBus(1)
        bus.write_byte_data(i2caddress,i2c_register,i2c_newaddr)

        print "Changed I2C address "

except Exception, Argument:
        print "Could not read device data


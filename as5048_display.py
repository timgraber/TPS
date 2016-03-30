#!/usr/bin/python
#
#
# Tim Graber
# 2016-03-29
# Rev 1
#
# DISCLAIMER: This code is presented AS IS for educational purposes only. By using this
# code, the user assumes all responsibility for any consequences, real or imagined.
# This code may be modified or changed by the author at any time. End user agrees
# there is no support given or expected.
#
# Follow the Raspberry Pi preparation steps - separate document
#
# Making the OLED work
# Download the appropriate code from the Adafruit site - please support this group
# by purchasing through them. They have put a lot of hours into developing the code
# and libraries to get things to work well.
# https://github.com/adafruit/Adafruit_Python_SSD1306.git
# After installing, run the various sample code scripts to make sure you have the display
# connected correctly.
#
# Connect both display and one position sensor to the I2C bus. 
# A Separate script is available to change the I2C address of the sensor. They can 
# be changed to one of four possibles which is more than enough for this project.
#
# Make the bracket for the magnet and attach to a piece of metal rod or drill 
# bit (what I used)
#
# For ease of testing, also print a plastic knob so the metal rod can be turned easily.

import sys
import smbus
import math
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageFont
import ImageDraw

bus=smbus.SMBus(1)
i2caddress=0x40
error_status=0x0F
readings=0xFA
i2c_register=0x15
agc_register=0xFA
diag=0xFB
mag_msb=0xFC
mag_lsb=0xFD
angle_lsb=0xFE
angle_msb=0xFF

## Reuired for OLED Display
######################################
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# Initialize library.
disp.begin()

# Get display width and height.
width = disp.width
height = disp.height
# Clear display.
disp.clear()
disp.display()
# Create image buffer.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new('1', (width, height))
# Load default font.
font = ImageFont.load_default()
# font = ImageFont.truetype('Minecraftia.ttf', 8)

# Create drawing object.
draw = ImageDraw.Draw(image)
# Define text and get total width.
text = 'ANGLE = '
maxwidth, unused = draw.textsize(text, font=font)

print 'Press Ctrl-C to quit.'
data=""
while True:
        data=raw_input("Enter Z or R, CTRL-C to quit")
        if data=="Z": # Zero out at this angle
                print("This angle will be used as a Zero Reference.")
                bus.write_byte_data(i2caddress,0x16,0x00)
                bus.write_byte_data(i2caddress,0x17,0x00)
                angl=bus.read_byte_data(i2caddress, angle_lsb)
                angm=bus.read_byte_data(i2caddress, angle_msb)
                ang = (angm<<6)+(angl&0x3f)
                print"Zero reference: ", (ang/45.51)
                bus.write_byte_data(i2caddress,0x16,angm)
                bus.write_byte_data(i2caddress,0x17,angl)
        else: # Run angle display
                while True:
                        ## Read the angle from the as5048
                        angm=bus.read_byte_data(i2caddress, angle_msb)
                        angl=bus.read_byte_data(i2caddress, angle_lsb)
                        ang = (angm<<6)+(angl&0x3f)
                        diagreg=bus.read_byte_data(i2caddress, diag)
                        agc = bus.read_byte_data(i2caddress, 0XFA)
                        calc_angle = (ang/45.51)
                        new_angle = format(calc_angle, '.1f')
                        text = 'ANGLE = ' + str(new_angle)
                        #Uncomment the line below to display to screen for troubleshooting
                        #print format(calc_angle, '.1f')
                        #######################
                        # Clear image buffer by drawing a black filled box.
                        draw.rectangle((0,0,width,height), outline=0, fill=0)
                        # Enumerate characters and draw them offset vertically based on a sine wave.
                        x = 0
                        y = 15
                        # Draw text.
                        draw.text((x, y), text, font=font, fill=255)
                        draw.text((x, y), text, font=font, fill=255)
                        # Draw the image buffer.
                        disp.image(image)
                        disp.display()
                        # Pause briefly before drawing next frame.
                        time.sleep(0.5)

                      

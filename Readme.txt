Telescope Position Sensor
=========================

1. Introduction

This is a positioning system that allows you to accurately determine where your telescope is pointing on two axes - elevation and direction. Each time this system is used, it will need to be calibrated and the accuracy of your calibration will be the overall determining factor as to how accurate the readings will be.

2. Background

My wife and I have been casual star gazers for many years. A few years ago, we decided to 'up our game' and purchased an Orion XT10 Classic Dobsonian telescope. Not realizing it couldn't be upgraded to a computerized mount, it seemed like a pretty good deal. I was to find out that an upgrade for this model was not available - very sad. Since I dabble in electronics, I decided to take on the task of designing an electronic interface that could display where the telescope was pointing.

3. Electronics framework

This project is centered around the Raspberry Pi computer with sensors connected to it that measure angular rotation. It is paired with an OLED that shows the information on screen, so it can be used without having to connect a keyboard, mouse and computer display. 

4. Software

The code is written in Python.

5. Estimated cost

Since this is a project in progress, I will update with the final cost when completed. So far, the implementer will need to purchase the following - 

Two AS5048B sensor evaluation kits. These are available from DigiKey for $15.96. It comes with a sensor mounted on a PCB and a rare-earth magnet. 

One 128X32 OLED can be purchased from Adafruit for about $18. 

One Raspberry Pi computer board, power supply and SD card. I purchased the CANAKIT Raspberry Pi 3, which was $49.99. I already had an SD card, so I didn't need to buy one - this project is using a 16GB card, but an 8GB should be fine.

Overall, you will need to have a USB keyboard, mouse and HDMI display to configure the RPi and to load the code. If you are attempting this project, you probably have these items on hand.

Estimated cost minus brackets and housing - $110.00 USD.

Enclosure and brackets - still to be determined


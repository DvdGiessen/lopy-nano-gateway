# LoPy LoRaWAN nano gateway
**Note: PyCom has merged these changes in [b97faca](https://github.com/pycom/pycom-libraries/commit/b97facad08a2c3840d98f5315b3c6a36b072eba0) , I'd recommend using
that version instead of this one since I probably won't be updating this very
often anymore. Go get [here](https://github.com/pycom/pycom-libraries/blob/master/examples/lorawan-nano-gateway).**

This repository contains a simple LoRaWAN nano gateway for use on a LoPy.
Only required configuration is `wifi_ssid` and `wifi_password` which are used
for connecting to the Internet.

Can be used for both EU868 and US915. Set up by default for use with TTN
on EU frequencies, but can be configured for any other region or even other
network supporting the Semtech Packet Forwarder. To use for example US region
frequencies, set `frequency=903900000`.

To use, change the configuration in `main.py` as you wish, and upload the three
files to your LoPy. Alternatively, if you know your way around Python you may
use the NanoGateway class directly in your application.

Based on code by PyCom. Compared to that original, this contains some detailed
logging output allowing easy monitoring of gateway activity from the console,
and a number of fixes for alternative frequencies and data rates.

Original can be found at
https://github.com/pycom/pycom-libraries/blob/master/examples/lorawan-nano-gateway/nanogateway.py

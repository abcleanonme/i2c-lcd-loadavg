# i2c-lcd-loadavg
This will read out the load averages on an i2c connected 16x2 lcd screen on the Onion Omega 2

# Installation
This program uses David Stein's fireonion_i2c_lcd Python library to interface with a 16x2 LCD Screen.
It can be found at https://bitbucket.org/fires/fireonion_i2c_lcd and more information can be found on
his blog at http://davidstein.cz/2016/03/13/onion-io-i2c-lcd-16x220x4-backpack-library/. Note that to use fireonion_i2c_lcd and subsequently
this program, the pyOnionI2C library is required and can be installed through opkg.

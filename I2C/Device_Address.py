from machine
import pin, I2C
#Init I2C using GP8 & GP9 (default I2C0 pins)
i2c = I2C(0, scl=pin(9), sda=pin(8), freq=200000 )
#Display device address
print("I2C Address :"+hex(i2c.scan()[0]).upper())
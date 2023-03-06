from machine
import pin, Timer
led = pin (25, Pin.OUT)
LED_state = True
tim = Timer()

def tick(timer):
    global led, LED_state
    LED_state = not LED_state
    led.value(LED_state)

tim.init(freq=1, mode= Timer.PERIODIC, callback = tick )
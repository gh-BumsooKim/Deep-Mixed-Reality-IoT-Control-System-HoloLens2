import RPi.GPIO as GPIO

def led_on():
    GPIO.setmode(GPIO.BCM)
    PIN = 17
    GPIO.setup(PIN, GPIO.OUT)

    try:
        while True:
            GPIO.output(PIN, True)
    except KeyboardInterrupt:
        GPIO.cleanup()

    print("On")

import RPi.GPIO as GPIO
import time
import keyboard 


DIR_PIN = 27    
PUL_PIN = 17    


STEP_DELAY = 0.001  

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(PUL_PIN, GPIO.OUT)

step_counter = 0

print("Virajs's actuator test script")
print("Press 'space' to move CW, 'b' to move CCW, and 'esc' to exit.")

try:
    while True:
        if keyboard.is_pressed('space'):
            GPIO.output(DIR_PIN, GPIO.HIGH)  # CW
            GPIO.output(PUL_PIN, GPIO.HIGH)
            time.sleep(STEP_DELAY)
            GPIO.output(PUL_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY)
            step_counter += 1
            print(f"Steps: {step_counter}", end='\r')

        elif keyboard.is_pressed('b'):
            GPIO.output(DIR_PIN, GPIO.LOW)  # CCW
            GPIO.output(PUL_PIN, GPIO.HIGH)
            time.sleep(STEP_DELAY)
            GPIO.output(PUL_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY)
            step_counter -= 1
            print(f"Steps: {step_counter}", end='\r')

        elif keyboard.is_pressed('esc'):
            print("\nExiting.")
            break

except KeyboardInterrupt:
    print("\nInterrupted manually.")

finally:
    GPIO.cleanup()

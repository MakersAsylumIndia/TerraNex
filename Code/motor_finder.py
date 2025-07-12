import RPi.GPIO as GPIO
import time

motor_map = {
    "1": {"name": "Motor 1", "step": 17, "dir": 27},
    "2": {"name": "Motor 2", "step": 22, "dir": 23},
    "3": {"name": "Motor 3", "step": 5,  "dir": 6},
    "4": {"name": "Motor 4", "step": 19, "dir": 26}
}

STEP_DELAY = 0.001
STEPS = 200

GPIO.setmode(GPIO.BCM)


for motor in motor_map.values():
    GPIO.setup(motor["step"], GPIO.OUT)
    GPIO.setup(motor["dir"], GPIO.OUT)

def move_motor(step_pin, dir_pin, steps=STEPS):
    GPIO.output(dir_pin, GPIO.HIGH) 
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(STEP_DELAY)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(STEP_DELAY)

try:
    while True:
        motor_choice = input("🔢 Enter motor number to move (1/2/3/4), or 'q' to quit: ").strip()
        
        if motor_choice.lower() == 'q':
            print("Exiting motor finder.")
            break
        
        if motor_choice not in motor_map:
            print("Invalid input. Enter 1, 2, 3, or 4.")
            continue

        motor = motor_map[motor_choice]
        print(f"⚙️ Moving {motor['name']} ({motor_choice})...")
        move_motor(motor["step"], motor["dir"])
        print(f"✅ Done testing {motor['name']}\n")

except KeyboardInterrupt:
    print("\nInterrupted.")

finally:
    GPIO.cleanup()

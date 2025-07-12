import RPi.GPIO as GPIO
import time
import keyboard  # sudo pip3 install keyboard

# Define motors with clear labels
motors = {
    "FL": {"step": 17, "dir": 27},  # Front Left
    "RL": {"step": 5,  "dir": 6},   # Rear Left
    "FR": {"step": 22, "dir": 23},  # Front Right
    "RR": {"step": 19, "dir": 26}   # Rear Right
}

STEP_DELAY = 0.001

# Grouped by side
LEFT_MOTORS = ["FL", "RL"]
RIGHT_MOTORS = ["FR", "RR"]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for m in motors.values():
    GPIO.setup(m["step"], GPIO.OUT)
    GPIO.setup(m["dir"], GPIO.OUT)

def set_direction(motor_labels, clockwise=True):
    for label in motor_labels:
        GPIO.output(motors[label]["dir"], GPIO.HIGH if clockwise else GPIO.LOW)

def step_motors(motor_labels):
    for label in motor_labels:
        GPIO.output(motors[label]["step"], GPIO.HIGH)
    time.sleep(STEP_DELAY)
    for label in motor_labels:
        GPIO.output(motors[label]["step"], GPIO.LOW)
    time.sleep(STEP_DELAY)

def drive_loop(left_dir, right_dir):
    set_direction(LEFT_MOTORS, clockwise=left_dir)
    set_direction(RIGHT_MOTORS, clockwise=right_dir)
    while True:
        step_motors(LEFT_MOTORS + RIGHT_MOTORS)
        if any(keyboard.is_pressed(k) for k in ['space', 'w', 'a', 's', 'd', 'esc']):
            break

try:
    print("🛻 TerraNex Drive | Controls: W/A/S/D to move, SPACE to stop, ESC to exit")

    while True:
        if keyboard.is_pressed('w'):
            print("⬆️  Moving Forward")
            drive_loop(left_dir=True, right_dir=True)

        elif keyboard.is_pressed('s'):
            print("⬇️  Moving Backward")
            drive_loop(left_dir=False, right_dir=False)

        elif keyboard.is_pressed('a'):
            print("↪️  Turning Left")
            drive_loop(left_dir=False, right_dir=True)

        elif keyboard.is_pressed('d'):
            print("↩️  Turning Right")
            drive_loop(left_dir=True, right_dir=False)

        elif keyboard.is_pressed('esc'):
            print("❌ Exiting...")
            break

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n🔌 Interrupted")

finally:
    GPIO.cleanup()

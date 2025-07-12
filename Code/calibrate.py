import RPi.GPIO as GPIO
import time

# Motor pins (grouped by side, FL + RL and FR + RR)
motors = {
    "FL": {"step": 17, "dir": 27},
    "RL": {"step": 5,  "dir": 6},
    "FR": {"step": 22, "dir": 23},
    "RR": {"step": 19, "dir": 26}
}

LEFT_MOTORS = ["FL", "RL"]
RIGHT_MOTORS = ["FR", "RR"]

STEP_DELAY = 0.001  # Speed
CALIBRATION_STEPS = 200  # Number of steps for test movement

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

try:
    print("📏 Starting Calibration")
    print(f"➡️ Bot will move FORWARD {CALIBRATION_STEPS} steps")
    input("Place bot at starting point. Press Enter to begin...")

    set_direction(LEFT_MOTORS, True)
    set_direction(RIGHT_MOTORS, True)

    for _ in range(CALIBRATION_STEPS):
        step_motors(LEFT_MOTORS + RIGHT_MOTORS)

    print("✅ Bot moved forward.")

    distance_cm = float(input("📏 Now measure distance moved (in cm) and enter here: "))

    steps_per_cm = CALIBRATION_STEPS / distance_cm
    print(f"✅ Calibration complete.")
    print(f"🧠 Steps per cm: {steps_per_cm:.2f}")

    # Optional: Save to file
    with open("steps_per_cm.txt", "w") as f:
        f.write(str(steps_per_cm))

except KeyboardInterrupt:
    print("\n🔌 Interrupted")

finally:
    GPIO.cleanup()

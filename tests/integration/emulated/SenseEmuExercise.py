from sense_emu import SenseHat
import time

sense = SenseHat()

while True:
    # Environmental sensors
    temp = sense.get_temperature()
    temp_h = sense.get_temperature_from_humidity()
    temp_p = sense.get_temperature_from_pressure()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    # Orientation
    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll = orientation["roll"]
    yaw = orientation["yaw"]

    # Compass / Magnetometer
    compass = sense.get_compass()

    # Gyroscope
    gyro = sense.get_gyroscope()
    g_pitch = gyro["pitch"]
    g_roll = gyro["roll"]
    g_yaw = gyro["yaw"]

    # Accelerometer
    accel = sense.get_accelerometer_raw()
    ax = accel["x"]
    ay = accel["y"]
    az = accel["z"]

    # Print all sensor data
    print(f"""
    === Sense HAT Sensor Data ===
    Temperature: {temp:.2f} °C
      (from Humidity): {temp_h:.2f} °C
      (from Pressure): {temp_p:.2f} °C
    Humidity: {humidity:.2f} %
    Pressure: {pressure:.2f} hPa

    Orientation: Pitch={pitch:.2f}, Roll={roll:.2f}, Yaw={yaw:.2f}
    Compass: {compass:.2f} degrees
    Gyroscope: Pitch={g_pitch:.2f}, Roll={g_roll:.2f}, Yaw={g_yaw:.2f}
    Accelerometer: x={ax:.3f}, y={ay:.3f}, z={az:.3f}
    ==============================
    """)

    # Short scrolling message on LED matrix
    msg = f"T:{temp:.1f} H:{humidity:.1f} P:{pressure:.1f}"
    sense.show_message(msg, scroll_speed=0.06, text_colour=[0, 255, 0])

    time.sleep(2)

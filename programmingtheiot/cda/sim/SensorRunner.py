# sensor_runner.py
import time
from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask
import csv

def run_task(task, seconds=10):
    start = time.time()
    while time.time() - start < seconds:
        sd = task.generateTelemetry()
        print(f"{sd.getName():<18} | {sd.getTimeStamp()} | {sd.getValue():.2f}")
        time.sleep(1)

if __name__ == "__main__":
    print("\n--- Temperature ---")
    run_task(TemperatureSensorSimTask(), seconds=10)

    print("\n--- Humidity ---")
    run_task(HumiditySensorSimTask(), seconds=10)

    print("\n--- Pressure ---")
    run_task(PressureSensorSimTask(), seconds=10)


'''
    Add csv
    
    # sensor_logger.py
import csv, time
from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask

tasks = [TemperatureSensorSimTask(), HumiditySensorSimTask(), PressureSensorSimTask()]
with open("sensor_log.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["ts", "sensor", "value"])
    start = time.time()
    while time.time() - start < 60:
        for t in tasks:
            sd = t.generateTelemetry()
            w.writerow([sd.getTimeStamp(), sd.getName(), round(sd.getValue(),2)])
        time.sleep(1)

print("Wrote sensor_log.csv")

'''
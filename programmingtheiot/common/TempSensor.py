# programmingtheiot/common/TempSensor.py

import random

from programmingtheiot.common.BaseSensor import BaseSensor


class TempSensor(BaseSensor):
    """
    Concrete sensor that reports ambient temperature.
    Generates synthetic readings within a configured Celsius range when active.
    """

    def __init__(self, name: str = "TempSensor", minC: float = 18.0, maxC: float = 26.0):
        super().__init__(name=name)

        if minC > maxC:
            raise ValueError("minC must be less than or equal to maxC")

        self.minC = minC
        self.maxC = maxC

    def readValue(self):
        """Return a random temperature reading when active, else None."""
        if not self.active:
            return None

        return random.uniform(self.minC, self.maxC)

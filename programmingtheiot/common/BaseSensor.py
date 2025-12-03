# programmingtheiot/common/BaseSensor.py

from abc import ABC, abstractmethod


class BaseSensor(ABC):
    """
    Minimal base class for a CDA sensor component.
    Subclasses should:
    - start()
    - stop()
    - readValue() when active
    """

    def __init__(self, name: str):
        self.name = name
        self.active = False

    def start(self):
        """Mark sensor as active."""
        self.active = True

    def stop(self):
        """Mark sensor as inactive."""
        self.active = False

    def isActive(self) -> bool:
        """Return True when the sensor has been started."""
        return self.active

    @abstractmethod
    def readValue(self):
        """
        Return the current sensor reading.
        Should return:
          - a float for real readings
          - None if no reading is available or sensor is inactive
        """
        pass

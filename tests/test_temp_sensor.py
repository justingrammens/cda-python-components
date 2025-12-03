import unittest

from programmingtheiot.common.TempSensor import TempSensor


class TempSensorTest(unittest.TestCase):
    def test_start_and_stop_toggle_active_flag(self):
        sensor = TempSensor()

        self.assertFalse(sensor.isActive())

        sensor.start()
        self.assertTrue(sensor.isActive())

        sensor.stop()
        self.assertFalse(sensor.isActive())

    def test_read_value_returns_none_when_inactive(self):
        sensor = TempSensor()

        self.assertIsNone(sensor.readValue())

    def test_read_value_returns_float_within_range_when_active(self):
        min_c = 10.5
        max_c = 42.5
        sensor = TempSensor(minC=min_c, maxC=max_c)

        sensor.start()

        for _ in range(10):
            value = sensor.readValue()
            self.assertIsInstance(value, float)
            self.assertGreaterEqual(value, min_c)
            self.assertLessEqual(value, max_c)


if __name__ == "__main__":
    unittest.main()

import unittest
from datetime import date

from fake_data_app.sensor import VisitorSensor


class TestVisitSensor(unittest.TestCase):

    def test_weekday_open(self):
        for test_day in range(12, 17 + 1):
            with self.subTest(i=test_day):
                visit_sensor = VisitorSensor(
                    avg_visit=1500, std_visit=300, perc_break=0
                )
                visit_count = visit_sensor.get_visit_count(
                    date(year=2024, month=8, day=test_day)
                )
                self.assertFalse(visit_count == 0)

    def test_sunday_closed(self):
        visit_sensor = VisitorSensor(avg_visit=1500, std_visit=300, perc_break=0)
        visit_count = visit_sensor.get_visit_count(date(year=2024, month=8, day=18))
        self.assertEqual(visit_count, 0)

    def test_break(self):
        visit_sensor = VisitorSensor(avg_visit=1500, std_visit=300, perc_break=10)
        visit_count = visit_sensor.get_visit_count(date(year=2024, month=8, day=17))
        self.assertEqual(visit_count, 0)

    def test_malfunction(self):
        visit_sensor = VisitorSensor(avg_visit=1500, std_visit=300, perc_malfunction=10)
        visit_count = visit_sensor.get_visit_count(date(year=2024, month=8, day=17))
        self.assertEqual(visit_count, 433)


if __name__ == "__main__":
    unittest.main()

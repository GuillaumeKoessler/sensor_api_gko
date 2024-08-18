import unittest
from datetime import date

from fake_data_app.store import StoreSensor


class TestStore(unittest.TestCase):
    def test_get_all_traffic(self):
        store_test = StoreSensor(
            "Strasbourg",
            avg_visit=1500,
            std_visit=100,
            perc_break=0,
            perc_malfunction=0,
        )
        visits = store_test.get_all_traffic(date(year=2024, month=8, day=19))
        self.assertEqual(visits, 1478)

    def test_get_sensor_traffic(self):
        store_test = StoreSensor(
            "Strasbourg",
            avg_visit=1500,
            std_visit=100,
            perc_break=0,
            perc_malfunction=0,
        )
        visit = store_test.get_sensor_traffic(2, date(year=2024, month=8, day=19))
        self.assertEqual(visit, 74)

    def test_sunday_closed(self):
        store_test = StoreSensor(
            "Strasbourg",
            avg_visit=1500,
            std_visit=100,
            perc_break=0,
            perc_malfunction=0,
        )
        visits = store_test.get_all_traffic(date(year=2024, month=8, day=18))
        self.assertEqual(visits, 0)


if __name__ == "__main__":
    unittest.main()

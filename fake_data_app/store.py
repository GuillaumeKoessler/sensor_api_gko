from datetime import date, timedelta

import numpy as np

from fake_data_app.sensor import VisitorSensor


class StoreSensor:
    """
    Permet de consolider plusieurs capteurs pour un magasin
    """

    def __init__(
        self,
        name: str,
        avg_visit: int,
        std_visit: int,
        perc_break: float = 0.015,
        perc_malfunction: float = 0.035,
    ) -> None:

        self.name = name
        self.sensors = list()

        # on fige la graine en fonction du nom du magasin
        seed_str = np.sum(list(self.name.encode("ascii")))
        np.random.seed(seed=seed_str)

        # on crée un repartition des passages par sensor
        # on fait l'hypothèse de n'avoir que 8 capteurs par magasins

        repart_sensor = [0.48, 0.30, 0.07, 0.05, 0.03, 0.03, 0.02, 0.02]
        np.random.shuffle(repart_sensor)

        for i in range(8):
            sensor = VisitorSensor(
                repart_sensor[i] * avg_visit,
                repart_sensor[i] * std_visit,
                perc_malfunction,
                perc_break,
            )

            self.sensors.append(sensor)

    def get_sensor_traffic(self, sensor_id: int, business_date: date) -> int:
        """
        Retourne le nombre de visite d'un capteur
        """
        visit = self.sensors[sensor_id].get_visit_count(business_date)
        return visit

    def get_all_traffic(self, business_date: date) -> int:
        """
        Retourne le nombre de visite d'un magasin
        """
        visits = sum([self.sensors[i].get_visit_count(business_date) for i in range(8)])
        return visits

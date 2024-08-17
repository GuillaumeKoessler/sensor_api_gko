import sys
from datetime import date, timedelta

import numpy as np


class VisitorSensor:
    """
    Simule le nombre d'entrée d'un centre commercial
    Prend la moyenne et l'écart type comme inputs
    Retourne un nombre de visiteurs
    """

    def __init__(
        self,
        avg_visit: int,
        std_visit: int,
        perc_break: float = 0.015,
        perc_malfunction: float = 0.035,
    ) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction

    def simulate_visit(self, business_date: date) -> int:
        """
        Simule le nombre de visite à partir de la date choisies
        """
        # permet de figer la graine en convertissant la date en nombre
        np.random.seed(seed=business_date.toordinal())

        # on déduit le jour de la semaine
        week_day = business_date.weekday()

        # on simule le nombre de visite à partir de la loi normale
        visit = np.random.normal(self.avg_visit, self.std_visit)

        # on définit des facteurs multiplicatifs en fonction du jour de la semaine
        visits_factor = {2: 1.10, 4: 1.25, 5: 1.35, 6: 0}

        visit = visit * visits_factor.get(week_day, 1)

        return np.floor(visit)

    def get_visit_count(self, business_date: date) -> int:
        """
        fonction pour simuler des malfonctions des capteurs
        Ils peuvent casser ou malfonctionner
        """
        # permet de figer la graine en convertissant la date en nombre
        np.random.seed(seed=business_date.toordinal())

        proba_malfct = np.random.random()

        nb_visit = self.simulate_visit(business_date)

        if proba_malfct < self.perc_break:
            print("cassé")
            return 0

        if proba_malfct < self.perc_malfunction:
            print("malfonction")
            return np.floor(nb_visit * 0.2)

        return nb_visit


if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day = [int(x) for x in sys.argv[1].split("-")]
    else:
        year, month, day = [2023, 12, 23]

    date_query = date(year=year, month=month, day=day)
    capteur = VisitorSensor(avg_visit=1500, std_visit=150)
    print(capteur.get_visit_count(date_query))

    init_date = date(year=2020, month=1, day=1)
    while init_date <= date(year=2020, month=12, day=31):
        capteur = VisitorSensor(avg_visit=1500, std_visit=150)
        print(capteur.get_visit_count(init_date))
        init_date += timedelta(days=1)

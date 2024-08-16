from datetime import date

import numpy as np


class VisitorSensor():
    """
    Simule le nombre d'entrée d'un centre commercial
    Prend la moyenne et l'écart type comme inputs
    Retourne un nombre de visiteurs
    """
    def __init__(self, avg_visit: int, std_visit: int) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit

    def simulate_visit(self, business_date: date) -> int:
        """
        Simule le nombre de visite à partir de la date choisies
        """
        # permet de figer la graine en convertissant la date en nombre
        np.random.seed(seed=business_date.toordinal())

        #on déduit le jour de la semaine
        week_day = business_date.weekday()

        #on simule le nombre de visite à partir de la loi normale
        visit = np.random.normal(self.avg_visit, self.std_visit)

        # on définit des facteurs multiplicatifs en fonction du jour de la semaine
        visits_factor = {
            2: 1.10,
            4: 1.25,
            5: 1.35,
            6: 0
        }

        visit = visit * visits_factor.get(week_day, 1)

        return np.floor(visit)

if __name__ == "__main__":
    capteur = VisitorSensor(avg_visit=1500, std_visit=150)
    print(capteur.simulate_visit(date(year=2023, month=12, day=23)))
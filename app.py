import logging
from datetime import date

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from fake_data_app import create_app

store_dict = create_app()
app = FastAPI()


@app.get("/")
def visit(
    store_name: str, year: int, month: int, day: int, sensor_id: int | None = None
) -> JSONResponse:

    # on check si le nom de la ville est dans les clés du dictionnaire
    if not (store_name in store_dict.keys()):
        logging.error(f"Ville non disponible : {store_name}")
        return JSONResponse(status_code=404, content="Ville non disponible")

    # on check que le numero du capteurs est entre 0 et 7
    if sensor_id and sensor_id not in range(8):
        logging.error(f"Sensor_id hors range : {sensor_id}")
        return JSONResponse(status_code=404, content="L'id du capteur doit être compris entre 0 et 7")

    # on vérifie que la date est bien au format attendu
    try:
        requested_date = date(year=year, month=month, day=day)
    except ValueError as e:
        logging.error(f"Could not cast date {e}")
        return JSONResponse(status_code=404, content="Veuillez enter une date valide")

    if requested_date > date.today():
        logging.error("Prediction du futur")
        return JSONResponse(status_code=404, content="On ne peut pas prédire le futur")

    # on limite le score à 2015
    if year < 2015:
        logging.error(f"Requete avant 2015 {year}")
        return JSONResponse(status_code=404, content="Pas de données avant 2015")

    # on calcule le nombre de visiteurs
    # si le sensor id est vide on retourne le total pour la magasin
    if sensor_id is None:
        visit_count = store_dict[store_name].get_all_traffic(
            date(year=year, month=month, day=day)
        )
    # sinon, on retourne le nombre de visiteurs pour le capteurs choisi
    else:
        visit_count = store_dict[store_name].get_sensor_traffic(
            sensor_id=sensor_id, business_date=date(year=year, month=month, day=day)
        )

    return JSONResponse(status_code=200, content=visit_count)

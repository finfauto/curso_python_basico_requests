import argparse
import json

import requests


def procesar_args():
    parser = argparse.ArgumentParser(
        prog="carreras_ganadas",
        description="Programa que devuelve el número de carreras ganadas por un piloto en un año dado"
    )
    parser.add_argument(
        "--piloto", required=True, help="Nombre del piloto"
    )
    parser.add_argument(
        "--temporada", required=True, help="Temporada a procesar"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = procesar_args()
    # https://ergast.com/api/f1/{temporada}/results.json

    url = f"https://ergast.com/api/f1/{args.temporada}/results.json?limit=1000"
    response = requests.get(url)

    data = json.loads(response.content.decode("utf-8"))
    for race in data["MRData"]["RaceTable"]["Races"]:
        resultados_carrera = race["Results"]
        ganador_de_la_carrera = resultados_carrera[0]["Driver"]["driverId"]
        print(f"En la carrera {race['round']} ha ganado el piloto {ganador_de_la_carrera}")

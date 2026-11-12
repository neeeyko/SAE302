# Agent de supervision : relève le CPU, la RAM et le disque de la machine
# Responsable : Bilel MEZRARE
import argparse
import os
import time

import psutil


def relever_mesures():
    # Racine du disque principal : C:\ sous Windows, / sous Linux
    racine = os.path.abspath(os.sep)
    # cpu_percent mesure l'utilisation du processeur pendant 1 seconde
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disque = psutil.disk_usage(racine).percent
    return {"cpu": round(cpu, 1), "ram": round(ram, 1), "disque": round(disque, 1)}


def lire_arguments():
    # Lit les réglages donnés sur la ligne de commande
    analyseur = argparse.ArgumentParser(description="Agent de supervision SAÉ 3.02")
    analyseur.add_argument("--serveur", default="127.0.0.1", help="adresse du serveur")
    analyseur.add_argument("--port", type=int, default=9000, help="port TCP du serveur")
    analyseur.add_argument("--id", required=True, help="identifiant de l'agent, par exemple pc-01")
    analyseur.add_argument("--secret", required=True, help="secret de l'agent")
    analyseur.add_argument("--intervalle", type=int, default=10, help="secondes entre deux mesures")
    return analyseur.parse_args()


# Test provisoire de l'étape 2 : affiche les réglages puis les mesures en boucle
if __name__ == "__main__":
    args = lire_arguments()
    print("agent", args.id, "-> serveur", args.serveur, "port", args.port)
    while True:
        print(relever_mesures())
        # cpu_percent a déjà pris 1 s, on attend le reste de l'intervalle
        time.sleep(max(args.intervalle - 1, 0))
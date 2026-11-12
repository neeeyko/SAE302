# Agent de supervision : relève le CPU, la RAM et le disque de la machine
# Responsable : Bilel MEZRARE
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


# Test provisoire de l'étape 1 : affiche les mesures en boucle
if __name__ == "__main__":
    while True:
        print(relever_mesures())
        time.sleep(2)
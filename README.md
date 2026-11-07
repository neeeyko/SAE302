
# SAÉ 3.02 - Supervision d'un parc informatique

Projet de BUT R&T 2e année, IUT de Villetaneuse.
Des agents relèvent l'état des machines (CPU, RAM, disque) et l'envoient
à un serveur central qui stocke les mesures dans PostgreSQL et les affiche
dans une interface, avec des alertes.

## Équipe

| Membre | Pseudo GitHub | Rôle |
|---|---|---|
| BARGHA Aymen | neeeyko | Serveur et protocole |
| DIA Ndeye | Ndeye-DIA | Renfort serveur : authentification des agents, agents silencieux, erreurs |
| MEZRARE Bilel | BilelMZ9 | Agent (psutil) |
| BOUABSA Reda | reda123-hub | Base de données PostgreSQL |
| TALEB Rayane | rayanetlb93-max | Interface |

## Organisation

- Trello : https://trello.com/b/buro2ThZ/sae-302
- Choix techniques : TCP, messages JSON ligne par ligne, un thread par agent, PostgreSQL.

## Installation

À compléter.

## Protocole applicatif

À compléter

# Gestion de l'authentification des agents

def authentifier_agent(identifiant, agents_autorises):
    """Vérifie si l'identifiant de l'agent est autorisé."""
    return identifiant in agents_autorises
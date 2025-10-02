# TODO Fonction qui reçoit une liste de legos et qui il y a combien de blocs de chaque couleur en moyenne


from collections import defaultdict

def moyenne_legos_par_couleur(liste_legos):
    """
    Calcule le nombre moyen de blocs de chaque couleur dans une liste de LEGO.

    Args:
        listée_legos (list): Liste de chaînes représentant les couleurs des LEGO.

    Returns:
        dict: Dictionnaire avec les couleurs comme clés et la moyenne comme valeur.
    """
    if not liste_legos:
        return {}

    compteur = defaultdict(int)
    for couleur in liste_legos:
        compteur[couleur] += 1

    total = len(liste_legos)
    moyenne = {couleur: count / total for couleur, count in compteur.items()}

    return moyenne

# Exemple d'utilisation :
legos = ["rouge", "bleu", "rouge", "vert", "bleu", "rouge"]
print(moyenne_legos_par_couleur(legos))

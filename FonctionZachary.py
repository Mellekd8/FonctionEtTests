def pourcentage_couleur(lego, couleur):
    if len(lego) == 0:
        return 0.0

    nb_couleur = lego.count(couleur)
    total = len(lego)
    pourcentage = (nb_couleur / total ) * 100

    return pourcentage
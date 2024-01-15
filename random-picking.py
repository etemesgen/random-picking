from math import factorial


def calculer_probabilite(k, nb_rouge, nb_blanche, nb_noire):
    total_boules = nb_rouge + nb_blanche + nb_noire

    if k > total_boules:
        raise ValueError("Erreur total de boules à tirer inférieur")

    if nb_rouge < 1 or nb_blanche < 1 or nb_noire < 1:
        raise ValueError("Au moins une boule de chaque couleur")

    combinaisons_rouge = (
        factorial(nb_rouge) / (factorial(1) * factorial(nb_rouge - 1))
    )
    combinaisons_blanche = (
        factorial(nb_blanche) / (factorial(1) * factorial(nb_blanche - 1))
    )
    combinaisons_noire = (
        factorial(nb_noire) / (factorial(1) * factorial(nb_noire - 1))
    )

    probabilite = (
        (combinaisons_rouge * combinaisons_blanche * combinaisons_noire)
        / factorial(k)
    )

    return probabilite


k = 3
nb_rouge = 5
nb_blanche = 4
nb_noire = 3

probabilite_result = calculer_probabilite(k, nb_rouge, nb_blanche, nb_noire)
print(f"La probabilité d'avoir chaque couleur : {probabilite_result:.4f}")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames
# cnames: dictionnaire de toutes les couleurs et de leur valeur hexadécimale
import numpy

# 1
# def list_to_dict(some_list: list) -> dict:
#     # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
#
#     dict = {}
#     i = 0
#     for elem in some_list:
#         dict[elem] = i
#         i += 1
#
#     return dict

# 2
def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    # liste = [(couleur, valeur_hex), (...), ...]

    liste = []
    for color in colors:
        liste.append((color, cnames[color]))

    return liste

# 3
# def create_list() -> list:
#     # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
#     liste = [i for i in range(10000)]
#
#     return liste[:15] + liste[351:]


# 4
#def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    # itérer dans mon dictionnaire
    # itérer dans les valeurs de mon dictionnaire (liste)
    # MSE: ((1/N) Somme i = 1 -> N (Fi - Oi) ** 2) ** 0.5 où Fi = valeurs prédites, Oi = valeurs réelles, N = nombre de données
    # mse = ((valeurs[0][1] - valeurs[0][0]) ** 2 + (valeurs[1][1] - valeurs[1][0]) ** 2 + (valeurs[2][1] - valeurs[2][0]) ** 2...) / len(list)
    # sum = 0
    #
    # sum += (valeurs[0][1] - valeurs[0][0]) ** 2

# Solution:
    # model_mse = {}
    # i = 0
    # for modele, valeur in model_dict.items():
    #     model_mse[modele] = sum(((valeur[i][1] - valeur[i][0]) ** 2)) / len(valeur)
    #     i += 1
    # return model_mse




def main() -> None:
    # some_list = ["a", "b", "z", "patate"]
    # print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    # print(f"La liste des 10000 entiers est: {create_list()}")

    # model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
    #               "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
    #               "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    # print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()

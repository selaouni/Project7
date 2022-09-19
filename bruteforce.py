import csv
from itertools import combinations
from time import time
from tqdm import tqdm


def read_csv_file():
    """
    :return : liste de données à analyser
    Cette fonction permet de convertir le fichier csv en une liste qui contient
    les même informations : nom de l'action, son cout et son bénefice
    """
    with open("dataset3.csv") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = []
        for row in data:
            data_list.append((row[0], float(row[1]), float(row[2])))
        return data_list


def calculate_profit(combination):
    profits = []
    for share in combination:
        profits.append(share[1] * share[2] / 100)
    # retourner la somme des profits de la combinaison passée en paramètre
    return sum(profits)


def calculate_cost(combination):
    cost = []
    for share in combination:
        cost.append(share[1])
    # retourner la somme des cout de la combinaison passée en paramètre
    return sum(cost)


MAX_INVEST = 500


def best_combination(data_list):
    """
    :param data_list: la liste des données à anayser
    :return: le meilleur profit, le Total investissement,
    la liste des actions Cette fonction donne comme résultat
    le meilleur profit et la liste des actions les plus rentables
    tout en respectant le montant total d'investissment de 500 euro,
    ce résultat est basé sur l'analyse de toutes
    les combinaisons possibles d'actions.
    """
    start = time()
    profit = 0
    best_comb = []

    for i in tqdm(range(len(data_list))):
        combs = combinations(data_list, i+1)
        for comb in combs:
            total_cost = calculate_cost(comb)

            if total_cost <= MAX_INVEST:
                total_profit = calculate_profit(comb)

                if total_profit > profit:
                    cost = total_cost
                    profit = total_profit
                    best_comb = comb

    print("Liste des actions les plus rentables : ")
    print(len(best_comb), "actions")
    for i in best_comb:
        print(i)
    print("-- le profil est de : ", profit)
    print("-- Total investissement : ", cost)
    print(f'Temps d execution: {time() - start} seconds')


# -----------------------  Execution du programmes  ------------------------

csv_data = read_csv_file()
best_combination(csv_data)

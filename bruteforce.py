import csv
from itertools import combinations
from time import time

def read_csv_file():
    with open("data_part1.csv") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = []
        for row in data:
            data_list.append((row[0], float(row[1]), float(row[2])))
        #print(data_list)
        return data_list


def calculate_profit(combination):
    profits = []
    for share in combination:
        profits.append(share[1] * share[2] / 100)

    return sum(profits)


def calculate_cost(combination):
    cost = []
    for share in combination:
        cost.append(share[1])


    return sum(cost)


Max_invest = 500
def best_combination(data_list):
    start = time()
    profit = 0
    best_comb = []

    for i in range(len(data_list)):
        combs = combinations(data_list, i+1)
        # print(i+1)
        # print("test de combinaison",list(combs))

        for comb in combs:
            total_cost = calculate_cost(comb)

            if total_cost <= Max_invest:
                total_profit = calculate_profit(comb)

                if total_profit > profit:
                    profit = total_profit
                    best_comb = comb
    print("Liste des actions les plus rentables : ")
    for i in best_comb:
        print(i)
    print("le profil est de : ", profit)
    print(f'Temps d execution: {time() - start} seconds')


#--------------------------------  Execution du programmes  ------------------------

csv_data = read_csv_file()
best_combination(csv_data)



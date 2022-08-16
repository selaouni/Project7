import csv
from tqdm import tqdm
from itertools import combinations



def read_csv_file():
    with open("data_part1.csv") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = []
        for row in data:
            data_list.append((row[0], float(row[1]), float(row[2])))
        #print(data_list)
        return data_list


def calculate_profit(combinaison):
    profits = []
    for i in combinaison:
        profits.append(i[1] * i[2] / 100)
    return sum(profits)


def calculate_cost(combinaison):
    cost = []
    for i in combinaison:
        cost.append(i[1])
    return sum(cost)


Max_invest = 500
def best_combination(data_list):
    profit = 0
    best_combinaison = []

    for i in tqdm(range(20)):
        combs = combinations(data_list, i+1)

        for comb in combs:
            total_cost = calculate_cost(comb)

            if total_cost <= Max_invest:
                total_profit = calculate_profit(comb)

                if total_profit > profit:
                    profit = total_profit
                    best_combinaison = comb
    print(best_combinaison)


#-----------------  Execution ------------------------

csv_data = read_csv_file()
best_combination(csv_data)



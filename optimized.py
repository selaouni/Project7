import csv
from time import time

def read_csv_file(number_file):
    with open("dataset" + number_file +".csv") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = []
        for row in data:
            if float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                data_share = (row[0], float(row[1]), float(row[1]) * float(row[2]) / 100)
                data_list.append(data_share)
        #print(data_list)
        return data_list

Max_invest = 500

def best_investment(data_list):
   start = time()
   matrice = [[0 for x in range(Max_invest + 1)] for x in range(len(data_list)+1)]

   for i in range(1, len(data_list) + 1):
       for w in range(1, Max_invest + 1):
           if data_list[i - 1][1] <= w:
               matrice[i][w] = max(data_list[i - 1][2] + matrice[i - 1][int(w - data_list[i - 1][1])], matrice[i - 1][w])
           else:
               matrice[i][w] = matrice[i - 1][w]

   # Retrouver les éléments en fonction de la somme
   w = Max_invest
   n = len(data_list)
   actions_selection = []

   while w >= 0 and n >= 0:
       e = data_list[n - 1]
       if matrice[n][int(w)] == matrice[n - 1][int(w - e[1])] + e[2]:
           actions_selection.append(e)
           w -= e[1]

       n -= 1

   print("---------------------------- Le meilleur investissement --------------------------- : ")
   print("Actions les plus rentables :\n ")
   print("le cout", matrice[-1][-1])
   for i in actions_selection:
        print (i)
   print(f'Temps d execution: {time() - start} seconds')

#---------------------------------- Execution du programmes -------------------------------------------

x = True
while x == True:

    try:
        for i in range(2):
            number = str(input("Merci de saisir le numéro du dataset à analyser -- Entrez 1 ou 2 : "))
            csv_data = read_csv_file(number)
            best_investment(csv_data)
        x = False

    except :
        pass
        print("Merci de saisir un chiffre 1 ou 2")










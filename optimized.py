import csv
from time import time
import memory_profiler
import line_profiler
profile = line_profiler.LineProfiler()

def read_csv_file(number_file):
    """
    :param number_file: le numéro du fichier dataset à analyser
    :return : liste de données filtrées à analyser
    Cette fonction permet de convertir le fichier csv en une liste qui contient
    le nom de l'action, son cout et le profit qui en decoule.
    """

    with open("dataset" + number_file +".csv") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        data_list = []
        for row in data:
            # Elimination des données négatives ou nulles
            if float(row[1]) <= 0 or float(row[2]) <= 0:
                pass
            else:
                # mettre dans la liste les 3 colones
                data_share = (row[0], float(row[1]),float(row[1]) * float(row[2])/ 100)
                data_list.append(data_share)
        print("Nombre de données analysées",len(data_list))
        return data_list

Max_invest = 500
@profile
def best_investment(data_list):
   """
   :param data_list: la liste des données à analyser
   :return: le meilleur profit, le Total investissement, la liste des actions
   Cette fonction donne comme résultat la solution optimisée en terme de profit et d'actions les plus rentables
   tout en respectant le montant total d'investissment de 500 euro.
   """
   start = time()
   matrice = [[0 for x in range(Max_invest + 1)] for x in range(len(data_list)+1)]

   for i in range(1, len(data_list) + 1):
       for w in range(1,(Max_invest + 1)):
           if data_list[i - 1][1]<= w:
               matrice[i][w] = max(data_list[i - 1][2] + matrice[i - 1][int(w - data_list[i - 1][1])], matrice[i - 1][w])

           else:
               # si max invest depassée prendre la solution optimisée de la ligne d'avant
               matrice[i][w] = matrice[i - 1][int(w)]

   # Retrouver les éléments en fonction de la somme finale obtenue
   w = Max_invest
   n = len(data_list)
   actions_selection = []

   while w >= 0 and n >= 0:
       e = data_list[n - 1]
       if matrice[n][int(w)] == matrice[n - 1][int(w - e[1])] + e[2]:
           actions_selection.append(e)
           w -= e[1]

       n -= 1

   list = []
   for elm in actions_selection:
       list.append(elm[1])
       total_invest = sum(list)

   print("---------------------------- Le meilleur investissement --------------------------- : ")
   print("-- Actions les plus rentables :\n ")
   print(len(actions_selection),'actions')
   for i in actions_selection:
        print (i)
   print("-- le profit est de : ", matrice[-1][-1])
   print("-- Total investissement : ", total_invest)
   print(f'Temps d execution: {time() - start} seconds')

#---------------------------------- Execution du programmes -------------------------------------------

x = True
while x == True:

    try:
        for i in range(3):
            number = str(input("Merci de saisir le numéro du dataset à analyser -- Entrez 1 ou 2 : "))
            csv_data = read_csv_file(number)
            best_investment(csv_data)
        x = False

    except :
        pass
        print("Merci de saisir un chiffre 1 ou 2")









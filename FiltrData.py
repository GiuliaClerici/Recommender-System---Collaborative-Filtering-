import csv
import numpy as np

with open('ratings_small.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    my_list = list(datareader)
    #print(my_list[1])
    #print(my_list[1][0])
    #print(my_list[1][1])
    #print(my_list[1][2])
    #print(my_list[1][3])
    j = 0
    k = 1
    c = 0
    rats = []
    varianza = 0
    vars = []
    for k in range(1, 672):
        for i in range(1, 100005):
            if int(my_list[i][0]) == k:
                rats.append(np.asarray(my_list[i][2]))
                print("SI")
                print(np.asarray(rats).astype(np.float))
        varianza = np.var(np.array(rats).astype(np.float))
        vars.append(varianza)
        rats = []
        varianza = 0

    print("vars:")
    print(vars)

    vars = np.array(vars).astype(np.float)
    varsSort = np.argsort(vars)
    print("indici delle dieci massime varianze, dunque numero utenti:")
    print(varsSort[-10:])

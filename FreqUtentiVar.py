import csv
import numpy as np
import statistics as stat

with open('ratings_small.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    my_list = list(datareader)
    k = 0
    rats = []
    varianza = 0
    vars = []
    for k in range(1, 672):
        for i in range(1, 100005):
            if (int(my_list[i][0])) == k:
                rats.append(np.asarray(my_list[i][2]))
                print("SI")
                print(np.asarray(rats).astype(np.float))
        varianza = stat.variance(np.array(rats).astype(np.float))
        vars.append(varianza)
        rats = []
        varianza = 0

    print("vars:")
    print(vars)

    vars = np.array(vars).astype(np.float)
    varsSort = np.argsort(vars)
    print("indici delle dieci massime varianze, dunque numero utenti:")
    print(varsSort[-10:])



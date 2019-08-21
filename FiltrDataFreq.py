import csv
import numpy as np

with open('ratings_small.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    my_list = list(datareader)
    k = 0
    i = 0
    freq = []
    for k in range(1, 672):
        c = 0
        for i in range(1, 100005):
            if (int(my_list[i][0])) == k:
                print("sì")
                c = c + 1
        freq.append(c)

    freq = np.array(freq).astype(np.float)
    #print(np.sort(freq))
    freqSort = np.argsort(freq)
    print(freqSort)
    print("indici dei dieci utenti maggiormente presenti:")
    print(freqSort[-10:])
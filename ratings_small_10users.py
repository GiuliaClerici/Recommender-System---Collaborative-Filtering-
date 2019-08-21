import csv
import numpy as np
import statistics as stat
import pandas as pd
import surprise as surp

# leggi file csv contenente i ratings filtrati
ratings = pd.read_csv('ratings_smaller.csv')
# crea dictionary basato su ratings
ratings_dict = {'itemID': list(ratings.movieId), 'userID': list(ratings.userId), 'rating': list(ratings.rating)}
# creo una struttura dati che sarà una tabella avente come colonne itemID, userID, rating
df_ratings = pd.DataFrame(ratings_dict)
#print(df_ratings)
# lettura del file contenente i ratings
# specifico che i ratings variano nel range 0.5-5.0
reader = surp.Reader(rating_scale=(0.5, 5.0))
# caricamento del dataset dal dataframe di pandas che ho chiamato df_ratings
data = surp.Dataset.load_from_df(df_ratings[['userID', 'itemID', 'rating']], reader)
print(data)

# suddivido l'insieme dei miei dati in 10 fold
data.split(n_folds=10)
# definisco come algoritmo SVD, Singular Value Decomposition
algo = surp.SVD
# definisco la grid di parametri da cui selezionare i migliori valori per i diversi parametri
param_grid = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005], 'reg_all': [0.4, 0.6]}
# ricerca dei migliori valori per i parametri n_epochs (numero di epoche), lr_all (learning rate), reg_ll ()
gsmodel = surp.model_selection.search.GridSearchCV(algo, param_grid, measures=['RMSE', 'MAE'], cv=10)
# train del modello
gsmodel.fit(data)
# stampa del miglior valore di RMSE
print(gsmodel.best_score['RMSE'])
# stampa della combinazione di parametri che dà il miglior valore di RMSE
print(gsmodel.best_params['RMSE'])
# definisco l'algoritmo SVD avente come valori dei parametri quei valori che mi forniscono il miglior valore di RMSE
algo = surp.SVD(n_epochs=gsmodel.best_params['rmse']['n_epochs'], lr_all=gsmodel.best_params['rmse']['lr_all'], reg_all=gsmodel.best_params['rmse']['reg_all'])
# eseguo una 10-fold cross-validazione utilizzando SVD sui miei dati guardando come misura l'RMSE e il MAE
surp.model_selection.cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=10, verbose=True)

# valuto le prestazioni dell'algoritmo KNN sui miei dati, da confrontare con prestazione SVD
#surp.model_selection.cross_validate(surp.KNNBasic(), data, measures=['RMSE', 'MAE'], cv=10, verbose=True)



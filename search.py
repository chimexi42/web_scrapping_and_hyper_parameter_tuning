import pandas as pd
import numpy as np

from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from sklearn import preprocessing, decomposition, pipeline
from functools import  partial
from skopt import space

def optimize(params,param_names, x,y):
    params = dict(zip(param_names, params))
    model = ensemble.RandomForestClassifier(**params)
    kf= model_selection.StratifiedKFold(n_splits=5)
    accuracies = []
    for idx in kf.n_splits(x=x, y =y):
        train_idx, test_idx = idx[0], idx[1]
        xtrain = x[train_idx]
        ytrain = y[train_idx]

        xtest = x[test_idx]
        ytest = y[test_idx]

        model.fit(xtrain, ytrain)
        preds = model.predict(xtest)
        fold_acc = metrics.accuracy_score(ytest, preds)
        accuracies.append(fold_acc)
    return -1.0 * np.mean(accuracies)


if __name__== "__main__":
    df = pd.read_csv("train.csv")
    x = df.drop('price_range', axis =1).values
    y = df.price_range.values

    optimization_function = partial(
        optimize,
        param_names = ....,
        x = x,
        y = y
    )




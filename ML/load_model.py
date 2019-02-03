import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pickle


def load_model(filename):
    return pickle.load(open(filename, 'rb'))


def save_model(filename, model):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)


pkl_filename = "pickle_model2.pkl"

regr = load_model(pkl_filename)

print(regr.predict(pd.DataFrame(data={"data": [1001], "completion_rate": [1.0]})))

save_model(pkl_filename, regr)

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


pkl_filename = "pickle_model.pkl"
csv_file = 'output1.csv'

regr = load_model(pkl_filename)
dataset = pd.read_csv(csv_file)
train_set, test_set = train_test_split(dataset, test_size=0.2)

train_set_X = train_set.iloc[:, :2]
train_set_Y = train_set.iloc[:, 3]

test_set_X = test_set.iloc[:, :2]
test_set_Y = test_set.iloc[:, 3]

print(train_set_X[:20])
print(train_set_Y[:20])
print(test_set_X[:20])
print(test_set_Y[:20])

regr = linear_model.LinearRegression()
regr.fit(train_set_X, train_set_Y)
pred_y = regr.predict(test_set_X)

print(regr.predict(pd.DataFrame(data={"data": [1001], "object_time": [1]})))
print('Coefficient: \n', regr.coef_)
print("Mean Square Error: %2.f" % mean_squared_error(test_set_Y, pred_y))
print('Variance score: %.2f' % r2_score(test_set_Y, pred_y))


plt.scatter(test_set_X.iloc[:, 0], test_set_Y, color='black')
# plt.plot(test_set_X.iloc[:, 0], pred_y)
# plt.xticks(())
# plt.yticks(())
plt.show()

save_model(pkl_filename, regr)

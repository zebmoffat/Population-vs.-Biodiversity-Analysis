__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import pickle
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import KFold

def train():
    counties_data = list()

    #Retrieve counties data from data_processed/
    with open('./data_processed/counties_data.pkl', 'rb') as file:
        counties_data = pickle.load(file)

    x = [[data[0]] for data in counties_data]
    y = [data[1] for data in counties_data]

    #k fold cross validation
    k = 5
    kf = KFold(n_splits=k, shuffle=True, random_state=42)

    #Linear Regression
    linear_regression = LinearRegression()
    for train_index, test_index in kf.split(x):
        X_train, X_test = [x[i] for i in train_index], [x[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]
        linear_regression.fit(X_train, y_train)
    with open("models/linear_regression.pkl", 'wb') as file:
        pickle.dump(linear_regression, file)

    #Ridge Regression
    ridge_regression = Ridge(alpha=0.01)
    for train_index, test_index in kf.split(x):
        X_train, X_test = [x[i] for i in train_index], [x[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]
        ridge_regression.fit(X_train, y_train)
    with open("models/ridge_regression.pkl", 'wb') as file:
        pickle.dump(ridge_regression, file)

    #Lasso Regression
    lasso_regression = Lasso(alpha=0.01)
    for train_index, test_index in kf.split(x):
        X_train, X_test = [x[i] for i in train_index], [x[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]
        lasso_regression.fit(X_train, y_train)
    with open("models/lasso_regression.pkl", 'wb') as file:
        pickle.dump(lasso_regression, file)

    #Decision Tree Regression
    decision_tree = DecisionTreeRegressor(max_depth=10)
    for train_index, test_index in kf.split(x):
        X_train, X_test = [x[i] for i in train_index], [x[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]
        y_train, y_test = [y[i] for i in train_index], [y[i] for i in test_index]
        decision_tree.fit(X_train, y_train)
    with open("models/decision_tree_regression.pkl", 'wb') as file:
        pickle.dump(decision_tree, file)
__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import wf_core
import wf_ml_training
import wf_ml_prediction
import pickle
import time
from sklearn.metrics import mean_squared_error, mean_absolute_error

#List of each population with each biodiversity score
counties_data = list()

def metrics():
    x = [[data[0]] for data in counties_data]
    y = [data[1] for data in counties_data]

    save = ""

    with (open("models/decision_tree_regression.pkl", 'rb') as file):
        model = pickle.load(file)

        #Predict using the loaded model
        y_pred = model.predict(x)

        #Calculate MSE and MAE
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        #Evaluation metrics
        save += ("Evaluation Metrics for Decision Tree Regression model:" +
               "\n\tMean Squared Error: " + str(mse) +
               "\n\tMean Absolute Error: " + str(mae))

        #print("Evaluation Metrics for Decision Tree Regression model:")
        #print("\tMean Squared Error: " + str(mse))
        #print("\tMean Absolute Error: " + str(mae))

    with (open("models/lasso_regression.pkl", 'rb') as file):
        model = pickle.load(file)

        #Predict using the loaded model
        y_pred = model.predict(x)

        #Calculate MSE and MAE
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        #Evaluation metrics
        save += ("\n\nEvaluation Metrics for Lasso Regression model:" +
               "\n\tMean Squared Error: " + str(mse) +
               "\n\tMean Absolute Error: " + str(mae))

    with (open("models/linear_regression.pkl", 'rb') as file):
        model = pickle.load(file)

        #Predict using the loaded model
        y_pred = model.predict(x)

        #Calculate MSE and MAE
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        #Evaluation metrics
        save += ("\n\nEvaluation Metrics for Linear Regression model:" +
               "\n\tMean Squared Error: " + str(mse) +
               "\n\tMean Absolute Error: " + str(mae))

    with (open("models/ridge_regression.pkl", 'rb') as file):
        model = pickle.load(file)

        #Predict using the loaded model
        y_pred = model.predict(x)

        #Calculate MSE and MAE
        mse = mean_squared_error(y, y_pred)
        mae = mean_absolute_error(y, y_pred)

        #Evaluation metrics
        save += ("\n\nEvaluation Metrics for Ridge Regression model:" +
               "\n\tMean Squared Error: " + str(mse) +
               "\n\tMean Absolute Error: " + str(mae))




    #Write evaluation to evaluations.txt
    with open("./evaluation/evaluation.txt", "w") as file:
        file.write(save)


if __name__ == '__main__':

    print("Attempting to open cleaned data from data_processed/")
    time.sleep(0.5)

    #Dictionaries for cleaned data from earlier
    population_dict = dict()

    biodiversity_dict = dict()

    #Try to open cleaned data. If not present generate with core file
    try:

        with open('./data_processed/cleaned_population_data.pkl', 'rb') as file:
            population_dict = pickle.load(file)

        with open('./data_processed/cleaned_biodiversity_data.pkl', 'rb') as file:
            biodiversity_dict = pickle.load(file)

        print("\tParsed files for cleaned data.\n")

    except FileNotFoundError as e:
        #Not present so run core to then have the files present for opening.
        print("\tFiles were not found. Creating them now.\n")
        wf_core.run()

        with open('./data_processed/cleaned_population_data.pkl', 'rb') as file:
            population_dict = pickle.load(file)

        with open('./data_processed/cleaned_biodiversity_data.pkl', 'rb') as file:
            biodiversity_dict = pickle.load(file)

    for county in population_dict:
        #For each county, add its population and biodiversity score to the list together without county name.
        counties_data.append((population_dict[county], len(biodiversity_dict[county])))

    with open("./data_processed/counties_data.pkl", 'wb') as file:
        pickle.dump(counties_data, file)

    #Train Tree model
    wf_ml_training.train()

    #Predict with model
    wf_ml_prediction.prediction()

    metrics()

    print(counties_data)
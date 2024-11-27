__author__ = "Zeb Moffat"
__date__ = "10/22/2024"

import pickle

def prediction():

    population = input("Enter a desired population size to predict: ")

    population = (int(population))

    with open("models/linear_regression.pkl", 'rb') as file:
        model = pickle.load(file)

        print("\nThe model predicts a biodiversity score of: " + str(model.predict([[population]])[0]) + "\n")
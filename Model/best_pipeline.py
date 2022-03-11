import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('ModelSaving_Test_10/Model/prepared_data.csv')
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: 0.975
exported_pipeline = MLPClassifier(alpha=0.001, learning_rate_init=0.01)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)

# For Basic Operations
import pandas as pd
import numpy as np
from sklearn.externals.six import StringIO  
from sklearn.model_selection import train_test_split
# Forest Regressor for analysing the dataset
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from numpy import array
from sklearn.model_selection import cross_val_predict
# Uploads the jaipur weather data file
features = pd.read_csv('weather_data.csv')
features = pd.get_dummies(features)
features.iloc[:,5:].head(5)
# Filter out the features and data cleaning
labels = np.array(features['precipm'])
features = features.drop('minpressurem', axis = 1)
features = features.drop('maxpressurem', axis = 1)
features = features.drop('meandewptm', axis=1)
features = features.drop('maxdewptm', axis=1)
features = features.drop('mindewptm', axis=1)
feature_list = list(features.columns)
features = np.array(features)
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.30, random_state = 42)
('Training Features Shape:', train_features.shape)
('Training Labels Shape:', train_labels.shape)
('Testing Features Shape:', test_features.shape)
('Testing Labels Shape:', test_labels.shape)
# Run the random forest regressor on the filtered dataset
rf = RandomForestRegressor(n_estimators = 1000,random_state = 42)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)
# Calculate the error in prediction (about 0.17 mm)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'mm of rainfall.')
result=np.mean(predictions)
#Normalize the result for 30 minutes probability
new_res=(result/24)*10
probability_of_no_rainfall=(new_res*0.5)
print(1-probability_of_no_rainfall)

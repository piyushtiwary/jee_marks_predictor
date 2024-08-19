import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load the dataset from a CSV file
data = pd.read_csv('data.csv')

# Separate the features (x) and target variable (y)
# Assuming the target variable is in the first column and features are in the remaining columns
x = data.iloc[:, 1:].values
y = data.iloc[:, 0].values

# Split the data into training and testing sets
# 80% of the data is used for training, and 20% is used for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Initialize the Random Forest Regressor model
# Setting random_state ensures that the results are reproducible
regressor = RandomForestRegressor(random_state=0)

# Train the model using the training data
regressor.fit(x_train, y_train)

# Predict the target variable using the test data
predict = regressor.predict(x_test)

# Print the actual values and the predicted values for comparison
print("Actual values:")
print(y_test)
print("Predicted values:")
print(predict)

# Uncomment the lines below to test the model with your own values
# # Replace `Value` with the percentile and rank you want to test

# your_percentile = Value
# your_rank = Value

# # Create a test array with the values you want to predict
# # Ensure the array is in the same format as the training data (i.e., 2D array)
# test = np.array([your_percentile, your_rank])

# # Reshape the test array to have shape (1, 2), as the model expects a 2D array
# test = test.reshape(1, -1)

# # Predict the value for the provided percentile and rank
# prediction = regressor.predict(test)
# print("Prediction for the provided values:")
# print(prediction)

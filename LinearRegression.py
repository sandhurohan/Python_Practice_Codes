# Linear Regression In Python

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes=datasets.load_diabetes()

# To Print Keys of Dataset & Description
print(diabetes.keys())
print(diabetes.DESCR)

diabetes_X=diabetes.data[:,np.newaxis,2]

# Training Datasets OR Features

diabetes_X_train=diabetes_X[:30]
diabetes_X_test=diabetes_X[-20:]

# Labels Of Dataset
diabetes_Y_train=diabetes.target[:30]
diabetes_Y_test=diabetes.target[-20:]

# Importing & Using Linear Regression
model=linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_Y_train)    #Training

diabetes_y_predicted=model.predict(diabetes_X_test) #Testing

print(f" \n Mean Squared Error Is : {mean_squared_error(diabetes_Y_test,diabetes_y_predicted)}")

# Weights & Intercepts
print(f"Weights : {model.coef_}")
print(f"Weights : {model.intercept_}")

# Making Plots Using Pyplot
plt.scatter(diabetes_X_test,diabetes_Y_test)
plt.plot(diabetes_X_test,diabetes_y_predicted)
plt.show()
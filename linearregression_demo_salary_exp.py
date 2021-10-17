

# Importing the libraries 
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

"""## load file"""

# Importing the dataset
dataset = pd.read_csv('/content/salary-experience-dataset.csv') 
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

print(X)
print(X.shape)
print(y, y.shape)
X = np.reshape(X,(-1,1))
y = np.reshape(y,(-1,1))
print(X.shape)
print(y.shape)

"""## Visualizing the dataset"""

# Visualising the dataset results
plt.scatter(X, y, color = 'red') 
plt.title('Salary vs Experience (dataset)') 
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Creating Linear Reg. model and visualizing


"""

# Fitting Simple Linear Regression to the dataset 
from sklearn.linear_model import LinearRegression 
regressor_1 = LinearRegression()
regressor_1.fit(X, y)

# Visualising the trained model
plt.scatter(X, y, color = 'red') 
plt.plot(X, regressor_1.predict(X), color = 'blue') 
plt.title('Salary vs Experience (dataset)') 
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""But how do we test our model?

## Train Test Split
"""

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

print(X_train.shape)
print(X_test.shape)

# Visualising the train and test dataset results
plt.scatter(X_train, y_train, color = 'red')
plt.scatter(X_test, y_test, color = 'blue') 
plt.title('Salary vs Experience (dataset)') 
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Train using training split"""

regressor_2 = LinearRegression()
regressor_2.fit(X_train, y_train)

y_pred = regressor_2.predict(X_test)

"""Plot y_test and y_pred"""

# Visualising the y_test and y_pred results
plt.scatter(X_test, y_test, color = 'red')
plt.scatter(X_test, y_pred, color = 'blue')
plt.plot(X_test, y_pred, color='black') 
plt.title('Salary vs Experience (dataset)') 
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

"""## Evaluate the performance of our model - MSE and MAE"""

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print('MSE', mean_squared_error(y_test, y_pred))
print('MAE', mean_absolute_error(y_test, y_pred))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn import neighbors
from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score

def train_test_split_and_scale(df):
    y = df['pm']
    x = df.drop('pm',axis=1)
    features = list(x.columns)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state = 0)
    scaler = MinMaxScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    return x_train, x_test, y_train, y_test,features

def fit_and_evaluate_model(x_train, x_test, y_train, y_test):
    model = neighbors.KNeighborsRegressor(n_neighbors = 2)
    model.fit(x_train, y_train)    
    y_test_pred=model.predict(x_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,y_test_pred)) #calculate rmse
    r2_val = r2_score(y_test, y_test_pred)
    print('RMSE value for k= 2'  , 'is:', error)
    print("R-squared score: ", r2_val)
    return model
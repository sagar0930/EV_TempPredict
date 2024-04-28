import joblib
import sqlite3
import pandas as pd
from data_processing_and_features import convert_dtpye,null_value_imputation
from model_building import train_test_split_and_scale,fit_and_evaluate_model
import os
os.chdir("C://Users/Admin/Downloads/Data Science/Session_41_DS_Project_Structure/DS1/")

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
conn.close()
conn = sqlite3.connect('Database.db')
df = pd.read_sql_query('Select * from Electric_cars' , conn)

df = convert_dtpye(df)
df = null_value_imputation(df)

x_train, x_test, y_train, y_test, features = train_test_split_and_scale(df)

model = fit_and_evaluate_model(x_train, x_test, y_train, y_test)

joblib.dump(model , 'ev_temp_regression.pkl')


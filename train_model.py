import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import joblib

# import dataset
df = pd.read_csv('diabetes (1).csv')
df.head()

X_train,X_test,y_train,y_test = train_test_split(df.drop(columns='Outcome'),df['Outcome'])

gbc = GradientBoostingClassifier()
gbc.fit(X_train,y_train)
y_pred = gbc.predict(X_test)
print(accuracy_score(y_test,y_pred))
joblib.dump(gbc,'model.pkl')
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix,accuracy_score
dataset = pd.read_csv('practice.csv')
dataset.head()
X = dataset.iloc[:, 4:].values
Y = dataset.iloc[:, 3].values

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size =0.2, random_state =0)

from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(X_train,Y_train)
y_pred=classifier.predict(X_test)
accuracy = accuracy_score(Y_test, y_pred)
cm=confusion_matrix(Y_test,y_pred)
print(cm)
print("accuracy")
print("%.3f"%accuracy)
accuracy = accuracy_score(Y_test, y_pred)
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(X_train,Y_train)
y_pred=classifier.predict(X_test)
cm=confusion_matrix(Y_test,y_pred)
print(cm)
print("accuracy")
print("%.3f" %accuracy)

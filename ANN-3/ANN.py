import json

with open("data.json") as f:
    data=json.load(f)
    
import numpy as np
import matplotlib.pyplot as plt 

X=[data["X1"],data["X2"],data["X3"],data["X4"],data["X5"],data["X6"],data["X7"],data["X8"],data["X9"],data["X10"],]
for i in range(len(X)):
    X[i]=[int(obj) for obj in X[i]]
X=(np.array(X))
X=X.transpose()
y=data["X11"]
y=np.array(y).transpose()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
y=le.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)

from sklearn.preprocessing import StandardScaler
scx= StandardScaler()
X_train=scx.fit_transform(X_train)
X_test=scx.transform(X_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

classifier=Sequential()
#adding firsthidden layer
classifier.add(Dense(units=15, activation='relu',input_dim=10))

classifier.add(Dense(units=10, activation='relu'))
#adding the output layer
classifier.add(Dense(units=1, activation='sigmoid'))
#compiling the layers
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])#adam is for stochastic gradient descend
#fitting the ANN model
classifier.fit(X_train,y_train,batch_size=10,epochs=500)

y_pred=classifier.predict(X_test)
y_pred=(y_pred>0.5)
y_pred_train=classifier.predict(X_train)
y_pred_train=(y_pred_train>0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
accuracy2=accuracy_score(y_train,y_pred_train)
print("Accuracy of model on test set: " ,accuracy)
print("Accuracy of model on training set: " ,accuracy2)

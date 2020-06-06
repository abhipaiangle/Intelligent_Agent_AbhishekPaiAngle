import json

with open("data.json") as f:
    data=json.load(f)
with open("data_test.json") as g:
    data_test=json.load(g)
    
import numpy as np
import matplotlib.pyplot as plt

X_train=[data["input1"],data["input2"]]
X_train=np.array(X_train)
X_train=X_train.transpose()
y_train=data["flag"]
y_train=np.array(y_train).reshape(-1,1)

X_test=[data_test["input1"],data_test["input2"]]
X_test=np.array(X_test)
X_test=X_test.transpose()
y_test=data_test["flag"]
y_test=np.array(y_test).reshape(-1,1)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

classifier=Sequential()
#adding firsthidden layer
classifier.add(Dense(units=20, activation='relu',input_dim=2))

classifier.add(Dense(units=10, activation='relu'))
#adding the output layer
classifier.add(Dense(units=1, activation='sigmoid'))
#compiling the layers
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])#adam is for stochastic gradient descend
#fitting the ANN model
classifier.fit(X_train,y_train,batch_size=None,epochs=100)

y_pred=classifier.predict(X_test)
y_pred=(y_pred>0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
cm=confusion_matrix(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)

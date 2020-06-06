import json

with open("data.json") as f:
    data=json.load(f)

import numpy as np
import matplotlib.pyplot as plt

X=[data["input1"],data["input2"]]
X=np.array(X)
X=X.reshape(-1,2)
y=data["flag"]
y=np.array(y).reshape(-1,1)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=0)
'''
from sklearn.preprocessing import StandardScaler
scx= StandardScaler()
X_train=scx.fit_transform(X_train)
X_test=scx.fit_transform(X_test)'''

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()
#adding firsthidden layer
classifier.add(Dense(output_dim=2, init='uniform', activation='relu',input_dim=2)) #relu is the curve which NN will follow
#adding another hidden layer
#classifier.add(Dense(output_dim=2, init='uniform', activation='relu'))
#adding the output layer
classifier.add(Dense(output_dim=1, init='uniform', activation='sigmoid'))
#compiling the layers
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])#adam is for stochastic gradient descend
#fitting the ANN model
classifier.fit(X_train,y_train,batch_size=None,epochs=400)

y_pred=classifier.predict(X_test)
y_pred=(y_pred>0.5)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

    
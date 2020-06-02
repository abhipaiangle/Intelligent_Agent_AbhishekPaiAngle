import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
import sys

def getfile(file):
  df = pd.read_csv(file)
  df.columns = [c.replace(' ', '_') for c in df.columns]
  return df

def result(model, test):
  output = model.predict(test)
  return output.astype('int64')

def makemodel(train_x, train_y):
  model = linear_model.LinearRegression()
  model.fit(train_x, train_y)
  return model

def get_data(df):
  feature_x = np.array(df['GREScore'])
  feature_x = feature_x.reshape(-1, 1)
  poly = PolynomialFeatures(degree=2)
  Xpoly = poly.fit_transform(feature_x)

  return Xpoly


if __name__ == '__main__':
  train_file = str(sys.argv[1])
  test_file = str(sys.argv[2])
  train_df = getfile(train_file)
  test_df = getfile(test_file)
  train_x = get_data(train_df)
  test_x = get_data(test_df)
  train_y = np.array(train_df['TOEFLScore'])
  test_y = np.array(test_df['TOEFLScore'])
  model = makemodel(train_x, train_y)
  output = result(model, test_x)
  print(output)
  outframe = pd.DataFrame(data = output, columns = ['Prdct_TOEFL_Score'])
  outframe.to_csv(str(sys.argv[3]))
  print("The score of the model was ", model.score(test_x, test_y))

  

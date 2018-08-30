import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import linear_model
import pandas as pd
import numpy as np

data = pd.read_csv('/Users/ashukumar/Desktop/SAT.CSV')
data2 =pd.read_csv('/Users/ashukumar/Desktop/test.csv')

data = np.array(data)

temp = data[:,6]
p = data[:,7]
p0 = data[:,8]
a = data[:,9]
uv = data[:,10]
y=data[:,11]
X = [list(temp), list(p), list(p0), list(a), list(uv)]
regr = linear_model.LinearRegression()
regr.fit(np.array(X).transpose(), uv)
data2 = np.array(data2)
temp2=data2[:,6]
p2 = data2[:,7]
p02 = data2[:,8]
a2 = data2[:,9]
uv2 = data2[:,10]
y2=data2[:,11]
X_new = [list(temp2), list(p2), list(p02), list(a2), list(uv2)]
Y_new = regr.predict(np.array(X_new).transpose())
a = np.array(y2)
b = np.array(np.round(Y_new))
c = np.array(temp2)
d=np.array(p2)
e=np.array(a2)
p = [a,b,c,d,e]
pd.DataFrame(p).transpose().to_csv("/Users/ashukumar/Desktop/my_solution.csv", index = 0)



import numpy as np
from sklearn.model_selection import train_test_split #train_test_split to split the data
from sklearn.neighbors import KNeighborsClassifier #this library is to implement kNN

#Given

f = [1,2,3,6,6,7,10,11]
label = [1,1,2,2,2,1,1,2]
data = []

for i in range (0,len(f)):
    data.append([f[i],label[i]])
    
#classes as per given question

y = np.array([0,0,1,1,1,0,0,0])
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.5, random_state= 0, shuffle = False)


print(x_train) 
print(y_train)

#given to implement KNN with k=3

neighbor = KNeighborsClassifier(n_neighbors = 3)  
neighbor.fit(x_train,y_train) 
y_pred = neighbor.predict(x_test) 
print(y_test)
y_pred
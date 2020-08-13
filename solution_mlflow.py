import json
import plotly.express as px
import mlflow
import requests
import pandas as pd    

########################################################
#                Log image height x width
########################################################

# Setting a place for mlflow to store tracking and artifacts
mlflow.set_tracking_uri('/home/ajinkya/Documents/pixxel/mlruns')
# Set an experiment name
exp_name = "Mumbai_tile"
mlflow.set_experiment(exp_name)

mlflow.start_run()

import rasterio
src = rasterio.open('01.TIF')
array = src.read(1)

height = array.shape[0]
width =  array.shape[1]

print(height,width)

mlflow.log_param("Image height",height)
mlflow.log_param("Image width",width)

# Extract non zero values from image and note the 
# index of pixel having non zero values







########################################################
#                Log Principle components 
########################################################

from non_zero_dataframe import sort_tif
final = sort_tif()
# final.to_csv("non_zero_bands.csv")
mlflow.log_artifact("./non_zero.csv")


print("generated final dataframe")

from matplotlib import pyplot as plt

n=[]
ind=[]
for i in range(242):     # 242 = number of bands
    n.append(i+1)
for i in range(242):
    ind.append('band'+str(n[i]))

features = ind
x = final.loc[:, features].values
from sklearn.preprocessing import MinMaxScaler
scaler_model = MinMaxScaler()
scaler_model.fit(x.astype(float))
x=scaler_model.transform(x)
from sklearn.decomposition import PCA


## Finding the principle components
pca = PCA(n_components=10)
principalComponents = pca.fit_transform(x)
ev=pca.explained_variance_ratio_


print("all principle components = ", ev[0],ev[1],ev[2],ev[3],ev[4],ev[5],ev[6],ev[7],ev[8],ev[9])

selected_PC=[]
for elem in ev:
    comp = elem * 100
    mlflow.log_metric("PCA_all",comp)
    
    if comp > 1:
        selected_PC.append(comp)
        

        
print("selected", selected_PC)

from pandas import DataFrame
df = DataFrame (ev,columns=['PC'])
df2 = DataFrame (selected_PC, columns=['selected PC'])
# print (df)
df.to_csv('all_principle_components.csv')
df2.to_csv('selected_principle_components.csv')


# mlflow.log_artifact("./all_principle_components.csv")
mlflow.log_artifact("./selected_principle_components.csv")




########################################################
#                Log Principle components 
########################################################

from sklearn.decomposition import PCA
pca = PCA(n_components = 3)
dt = pca.fit_transform(final.iloc[:, :-1].values)
q = pd.concat([pd.DataFrame(data = dt)] )
q.to_csv('pca_output.csv')
mlflow.log_artifact("./pca_output.csv")


import numpy as np
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)
kmeans = kmeans.fit(q)
labels = kmeans.predict(q)

mlflow.log_metric("PCA", 3)
mlflow.log_metric("Knn_clusters",4)

index = final.index.tolist() 
a= np.array(index)
dataset = pd.DataFrame({'count': a, 'labels': labels})
dataset.set_index('count', inplace = True)
res = dataset['labels'].value_counts()

def reshaped_coords(a):
    '''
        reshaped_coords takes in index of a label and outputs
        its pixel location on orignal image
    '''
    q,r = divmod(a,width)
    y_coord = q
    x_coord = r
    return (x_coord, y_coord)

Index_label_class1 = dataset[dataset['labels']==0].index.tolist()  
Index_label_class2 = dataset[dataset['labels']==1].index.tolist() 
Index_label_class3 = dataset[dataset['labels']==2].index.tolist() 
Index_label_class4 = dataset[dataset['labels']==3].index.tolist() 


class_1_list=[]
for values in Index_label_class1:
  coords = reshaped_coords(values)
  class_1_list.append(coords)

class_2_list=[]
for values in Index_label_class2:
  coords = reshaped_coords(values)
  class_2_list.append(coords)

class_3_list=[]
for values in Index_label_class3:
  coords = reshaped_coords(values)
  class_3_list.append(coords)
    
class_4_list=[]
for values in Index_label_class4:
  coords = reshaped_coords(values)
  class_4_list.append(coords)



import cv2
import numpy as np

# width = 1021
# height = 3481
#3481, 1021
# Make empty black image of size (100,100)
img = np.zeros((height, width, 3), np.uint8)

red = [0,0,255]
green = [0,255,0]
blue = [255,0,0]
darkgreen = [0,51,0]
for values in class_1_list:
#   print(values[1], values[0])

  img[values[1],values[0]] = blue

cv2.imwrite('img1.png', img)

for values in class_2_list:
#   print(values[1], values[0])

  img[values[1],values[0]] = darkgreen

cv2.imwrite('img2.png', img)


for values in class_3_list:
#   print(values[1], values[0])

  img[values[1],values[0]] = red

cv2.imwrite('img3.png', img)


for values in class_4_list:
#   print(values[1], values[0])

  img[values[1],values[0]] = green

cv2.imwrite('img4.png', img)


mlflow.log_artifact("./img4.png")

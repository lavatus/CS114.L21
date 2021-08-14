import pickle
import numpy as np 
import cv2
from numpy.lib.shape_base import split
from scipy.sparse import dia
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier

diadiem=dict()
diachi=dict()
mota=dict()
hinhanh=dict()

with open('diadiem.txt',encoding='utf8') as f:
    file1 = f.readlines()
for i in file1:
    i=(i.replace("\n","")).split(":")
    diadiem[int(i[0])]=i[1]


with open('diachi.txt',encoding='utf8') as f:
    file2 = f.readlines()
for i in file2:
    i=(i.replace("\n","")).split(":")
    diachi[int(i[0])]=i[1]

with open('description.txt',encoding='utf8') as f:
    file3 = f.read().split('\n')

for i in file3:
    i=i.split(":")
    temp=i[1].split("+")
    mota[int(i[0])]=[temp[1],temp[2]]

with open('linkanh.txt',encoding='utf8') as f:
    file4 = f.read().split('\n')
for i in file4:
    i=i.split("+")
    hinhanh[int(i[0])]=i[1]

data = pickle.load(open('save_data100.d','rb'))
label  = pickle.load(open('save_label.d','rb'))


X, y = shuffle(data,label,random_state=42)

clf =  KNeighborsClassifier(n_neighbors=1,leaf_size= 20, metric= 'minkowski', p= 1, weights= 'uniform')
clf.fit(X, y)

def prediction_Img(path):

    size = (80,60)
    img = cv2.imread(path,1)
    img  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_blur = cv2.GaussianBlur(img,(5,5),0)
    img_resize = cv2.resize(img_blur, dsize=size, interpolation = cv2.INTER_AREA)
    img_resize =  np.array(img_resize.reshape(-1))
    result=clf.predict([img_resize])[0]
    return diadiem[result],diachi[result],mota[result],hinhanh[result]



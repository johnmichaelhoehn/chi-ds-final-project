# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 19:23:18 2016

@author: johnhoehn
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split


df = pd.read_csv('frog_data.csv')
df = df[df.Species != 'Location Skipped']
df['RunDate'] = pd.to_datetime(df['RunDate'])
df['Month'] = df['RunDate'].apply(lambda x: x.month)
df_complete = df.dropna()

predictors = ['Longitude','Latitude','Temp','Month','Wind_Code','Sky_Code','Cloud_Cover']
X = df_complete[predictors]
y = df_complete['Species']

scaler = preprocessing.StandardScaler().fit(X)
scaler.transform(X) 

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=0)

model = RandomForestClassifier(n_estimators = 7)
model.fit(X_train,y_train)

features = predictors
feature_importances = model.feature_importances_

features_df = pd.DataFrame({'Features': features, 'Importance Score': feature_importances})
features_df.sort_values('Importance Score', inplace=True, ascending=False)

print features_df.head()

predictions = list(model.predict(df[predictors])) 

cm = confusion_matrix(df['Species'],predictions,labels = ['Chorus Frog', 'N.Leopard Frog', 'Green Frog', 'E. Gray Treefrog','American Toad', 'Bullfrog', 'Spring Peeper', 'Wood Frog','Copes Gray Treefrog', 'Plains Leopard Frog', 'Cricket Frog','Pickerel Frog', 'Fowlers Toad', 'None seen nor heard'])
print(cm)

labels = ['Chorus Frog', 'N.Leopard Frog', 'Green Frog', 'E. Gray Treefrog','American Toad', 'Bullfrog', 'Spring Peeper', 'Wood Frog','Copes Gray Treefrog', 'Plains Leopard Frog', 'Cricket Frog','Pickerel Frog', 'Fowlers Toad', 'None seen nor heard']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(labels))
    plt.xticks(tick_marks,labels,rotation=80)
    plt.yticks(tick_marks,labels)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
print plot_confusion_matrix(cm)
print(classification_report(df['Species'],predictions, target_names=labels))

# -*- coding: utf-8 -*-
"""PROJECT NEW ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q389frfMaevNGlLHq_j4wM3GK1KAOlhP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data=pd.read_csv('/content/drive/MyDrive/credit_card_fraud_balanced.csv')

data.head()

data.info()

data.isnull().sum()

#labelencoding

le=LabelEncoder()
data['TransactionType']=le.fit_transform(data['TransactionType'])
data['Location']=le.fit_transform(data['Location'])

data['TransactionDate'] = pd.to_datetime(data['TransactionDate'])

data['TransactionHour'] = data['TransactionDate'].dt.hour
data['TransactionDay'] = data['TransactionDate'].dt.day
data['TransactionMonth'] = data['TransactionDate'].dt.month

data = data.drop(columns=['TransactionDate'])

#EDA
sns.scatterplot(x='Amount', y='TransactionHour', hue='IsFraud', data=data)

#Check the class distribution (fraud vs non-fraud)
class_counts = data['IsFraud'].value_counts()

# Print the class distribution
print("Class Distribution:")
print(class_counts)

# Plot the class distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='IsFraud', data=data, palette='Set2')
plt.title('Class Distribution (Fraud vs Non-Fraud)', fontsize=14)
plt.xlabel('IsFraud', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks([0, 1], ['Non-Fraud', 'Fraud'])
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data['Amount'], bins=50, kde=True)
plt.title('Distribution of Transaction Amount')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

#seprate the data set to x,y
X=data.drop(columns=['IsFraud'])
y=data['IsFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling (Standardization)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#smote
from imblearn.over_sampling import SMOTE
smote = SMOTE(sampling_strategy=0.5, random_state=42)  # Adjust ratio if needed
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Check new class distribution
print("Before SMOTE:\n", y_train.value_counts(normalize=True))
print("\nAfter SMOTE:\n", y_train_resampled.value_counts(normalize=True)) # Change y_train_smote to y_train_resampled

#logistic regrresion
model = LogisticRegression(solver='lbfgs', max_iter=10000, class_weight='balanced')
model.fit(X_train_resampled, y_train_resampled)

y_pred = model.predict(X_test)

model.score(X_train_resampled, y_train_resampled)

model.score(X_test,y_test)

#randomforest
model2 = RandomForestClassifier(class_weight="balanced", random_state=42)
model2.fit(X_train_resampled, y_train_resampled) # Fit the model to your training data
y_pred = model2.predict(X_test)

model2.score(X_train_resampled, y_train_resampled)

model2.score(X_test,y_test)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_train_resampled, y_train_resampled)

y_pred = model3.predict(X_test)

model3.score(X_train_resampled, y_train_resampled)

model3.score(X_test,y_test)

#svm
model4=SVC
svm=SVC(kernel='linear')
svm.fit(X_train_resampled, y_train_resampled)

svm.score(X_train_resampled, y_train_resampled)

svm.score(X_test,y_test)

#poly
svm1=SVC(kernel='poly')
svm1.fit(X_train_resampled, y_train_resampled)
svm1.score(X_train_resampled, y_train_resampled)

svm1.score(X_test,y_test)

#sigmoid
svm2=SVC(kernel='sigmoid')
svm2.fit(X_train_resampled, y_train_resampled)
svm2.score(X_train_resampled, y_train_resampled)

svm2.score(X_test,y_test)

#rbf
svm3=SVC(kernel='rbf')
svm3.fit(X_train_resampled, y_train_resampled)
svm3.score(X_train_resampled, y_train_resampled)

svm3.score(X_test,y_test)

#knn
model5=KNeighborsClassifier(n_neighbors=5)
model5.fit(X_train_resampled, y_train_resampled)
y_pred = model5.predict(X_test)
model5.score(X_train_resampled, y_train_resampled)

model5.score(X_test,y_test)

#gradient boosting machine
from sklearn.ensemble import GradientBoostingClassifier
model6 = GradientBoostingClassifier()
model6.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)
model6.score(X_train_resampled, y_train_resampled)

model6.score(X_test,y_test)

#xg boosting
from xgboost import XGBClassifier
model7 = XGBClassifier()
model7.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)
model7.score(X_train_resampled, y_train_resampled)

model7.score(X_test,y_test)

#naive bias
from sklearn.naive_bayes import GaussianNB # Import GaussianNB from sklearn.naive_bayes
model8=GaussianNB()
model8.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)
model8.score(X_train_resampled, y_train_resampled)

model8.score(X_test,y_test)

ensemble_model = RandomForestClassifier()
ensemble_model.fit(X_train, y_train)
y_pred_ensemble = ensemble_model.predict(X_test)
accuracy_ensemble = accuracy_score(y_test, y_pred_ensemble)
print("Ensemble Model Accuracy:", accuracy_ensemble)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(ensemble_model, X, y, cv=5, scoring='accuracy')

# Print the cross-validation scores
print("Cross-validation scores:", scores)
print("Average cross-validation score:", scores.mean())

#gridsearchcv
from sklearn.model_selection import GridSearchCV
ensemble_model = RandomForestClassifier(random_state=42)

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30]
}


grid_search = GridSearchCV(ensemble_model, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)
print("Best hyperparameters:", grid_search.best_params_)

best_model = grid_search.best_estimator_

y_pred_best = best_model.predict(X_test)
accuracy_best = accuracy_score(y_test, y_pred_best)
print("Best model accuracy:", accuracy_best)

#features importence
rf = best_model # best_model is already the RandomForestClassifier
importances = rf.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
sns.barplot(x=importances, y=feature_names)
plt.title("Feature Importance")
plt.show()

#joblib
import joblib
#joblib
import joblib
joblib.dump(best_model,'project.pkl')
joblib.dump(scaler,'scaler.pkl')
joblib.dump(model2,'C:\\Users\\USER\\Desktop\\Project 24\\project.pkl')


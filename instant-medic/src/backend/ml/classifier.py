
import csv, numpy as np
from sklearn.naive_bayes import MultinomialNB

data_matrix = None
X = None
y = None

with open(file='../data/DiseaseSymptomKB.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(next(csvreader))
    data_matrix = np.asarray(a=[row for row in csvreader])
    X = data_matrix[:, 1]
    y = data_matrix[:, 0]

print(data_matrix)
print(X)
print(y)
mnb_model = MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)
mnb_model.fit(X, y)

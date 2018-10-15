# Solution Exercise 1.1
from sklearn.svm import SVC
clfs = []
Cs = [0.1, 1, 10, 25]
for C in Cs:
    clf = SVC(gamma=1, C=C)
    clf.fit(X_train, y_train)
    clf.name = 'C = {}'.format(C)
    clfs.append(clf)
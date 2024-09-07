import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_auc_score
import xgboost as xgb

from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
clf_path = 'svm_norm_pv_wv_af2.model'

X = []
# for l in open('/home/bill/location/doc2vec/5000.norm.pv_wv').read().split('\n'):
#     ls = l.strip().split(' ')
#     # print len(ls)
#     if len(ls) == 200:
#         X.append(map(float, ls[100:200]))
y = []
for l in open('/home/frank/relation/dependency/data/label5000.txt').read().split('\n'):
    ls = l.strip().split('\t')
    # print ls
    if len(ls) >=4:
        # print ls
        y.append(int(ls[4]))


y = np.array(y)

# add_fs0 = []
# for l in open('/home/frank/relation/dependency/data/label5000.af').read().split('\n'):
#     ls = l.strip().split('\t')
#     # if len(ls) == 17:
#     if(len(ls)>=10):
#         add_fs0.append(map(int, ls[1:]))
# add_fs0 = np.array(add_fs0)
#
#
# add_fs = []
# for l in open('/home/frank/relation/dependency/data/label5000.af2').read().split('\n'):
#     ls = l.strip().split('\t')
#     # if len(ls) == 17:
#     if(len(ls)>=10):
#         add_fs.append(map(int, ls[1:]))
# add_fs = np.array(add_fs)


for l in open('/home/frank/relation/dependency/data/label5000.af3').read().split('\n'):
    ls = l.strip().split('\t')
    # if len(ls) == 17:
    if(len(ls)>=10):
        ls = ls[1:]
        X.append(map(float, ls[0:260]))
X = np.array(X)

# X = preprocessing.minmax_scale(X,feature_range=(-1,1))

# X = preprocessing.scale(X)
# X = preprocessing.normalize(X, norm='l2')
#
# X = preprocessing.scale(X)
# X = preprocessing.normalize(X, norm='l2')


# X = np.c_[X,add_fs]
# X = np.c_[add_fs,add_fs0]
# X = np.zeros((5000,100))
# print(X[0])
TEST_SPLIT = 0.2
# RNG_SEED = 233213
RNG_SEED = 1337

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=1000, random_state=RNG_SEED)
print X_train.shape , y_train.shape
print X_test.shape , y_test.shape


tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},]
                    # {'kernel': ['linear'], 'C': [1, 10, 100]}]
score="precision" #_macro
# clf = LogisticRegression(penalty='l2',tol=0.01)
parameters = {
        'n_estimators': [100, 250, 500],
        'learning_rate': [0.05, 0.1, 0.3],
        'max_depth': [6, 9, 12],
        'subsample': [0.9, 1.0],
        'colsample_bytree': [0.9, 1.0],
    }

# clf = GridSearchCV(xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, subsample=0.8, colsample_bytree=0.7),parameters,n_jobs=10,cv=10,verbose=1)
clf = GridSearchCV(SVC(C=1,probability=True), tuned_parameters, cv=5, scoring='%s' % score, n_jobs=30 , verbose=5)
# clf = xgb.XGBClassifier(n_estimators=100, learning_rate=0.01, max_depth=3, subsample=0.6, colsample_bytree=0.6)
print 'begin training'

# clf = GridSearchCV(SVC(C=1,probability=True), tuned_parameters, cv=5, scoring='%s' % score, n_jobs=30 , verbose=5)
# clf = SVC(C=1000, kernel='rbf', gamma=1e-3, probability=True, random_state=1,verbose=0)
# clf = SVC()
# print(X_train[0])
clf.fit(X_train, y_train)
# print((sum(y)+0.0) / len(y))
# print((sum(y_train)+0.0) / len(y_train))
# print((sum(y_test)+0.0) / len(y_test))
print clf.best_params_
# {'kernel': 'rbf', 'C': 1000, 'gamma': 0.001}


print '--------------------------'
#
# print 'training result '
# y_train_pred = clf.predict(X_train)
# print 'accuracy',accuracy_score(y_train, y_train_pred)
# print 'precision', precision_score(y_train, y_train_pred)
# print 'recall_score',recall_score(y_train, y_train_pred)
# print 'f1_score', f1_score(y_train, y_train_pred)
# print '--------------------------'

#
# print 'tuning result '
# y_tuing_pred = clf.predict(X_tuning)
# print 'accuracy',accuracy_score(y_tuning, y_tuing_pred)
# print 'precision', precision_score(y_tuning, y_tuing_pred)
# print 'recall_score',recall_score(y_tuning, y_tuing_pred)
# print 'f1_score', f1_score(y_tuning, y_tuing_pred)
# print '--------------------------'
print 'training result '
y_train_pred = clf.predict(X_train)
y_train_prob = [x[1] for x in clf.predict_proba(X_train)]
print 'auc_score', roc_auc_score(y_train, y_train_prob)
print 'accuracy',accuracy_score(y_train, y_train_pred)
print 'precision', precision_score(y_train, y_train_pred)
print 'recall_score', recall_score(y_train, y_train_pred)
print 'f1_score', f1_score(y_train, y_train_pred)


print '--------------------------'
y_pred = clf.predict(X_test)
y_prob = [x[1] for x in clf.predict_proba(X_test)]
# print(y_pred)
# print(y_test)
print 'test result '
print 'auc_score', roc_auc_score(y_test, y_prob)
print 'accuracy',accuracy_score(y_test, y_pred)
print 'precision', precision_score(y_test, y_pred)
print 'recall_score', recall_score(y_test, y_pred)
print 'f1_score', f1_score(y_test, y_pred)

# print y_test
# print y_pred
print '--------------------------'




# y_pred_prob = clf.predict_proba(X_test)
# res = []
# # print y_pred_prob
# import math
# for i in range(len(y_test)):
#     e = y_pred[i]==y_test[i]
#     res.append((math.fabs(y_pred_prob[i][1]-0.5),e,i))
# res.sort(reverse=True)

from sklearn.externals import joblib
joblib.dump(clf,clf_path)
print 'done saving'
#
# y_5w_pred_prob = clf.predict_proba()
# y_5w_pred_prob =
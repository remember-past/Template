from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
X, y = load_breast_cancer(return_X_y=True)
clf = LogisticRegression(solver="liblinear", random_state=0).fit(X, y)

y_prd=clf.predict_proba(X)[:, 1]
roc_auc_score(y, y_prd)
y_prd_2=clf.decision_function(X)
roc_auc_score(y,y_prd_2 )

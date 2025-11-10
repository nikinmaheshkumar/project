from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd

iris = load_iris()
X, y, fn, tn = iris.data, iris.target, iris.feature_names, iris.target_names
df = pd.DataFrame(X, columns=fn); df["target"] = y
print("Dataset Shape:", df.shape, "\n\nFirst 5 rows:\n", df.head(), sep="")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42).fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=tn), sep="")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred), sep="")
print("\nFeature Importance:"); [print(f"{n}: {imp:.4f}") for n, imp in zip(fn, clf.feature_importances_)]
print("\nDecision Tree Structure:\n", export_text(clf, feature_names=fn), sep="")

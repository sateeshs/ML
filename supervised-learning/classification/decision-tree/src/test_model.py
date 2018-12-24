##https://www.datascience.com/blog/random-forests-decision-trees-ensemble-methods
import pandas as pd
from pandas import DataFrame,read_csv
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import graphviz
from decision_tree import DecisionTree


training_file = f'./data/train_preprocessed.csv'
testing_file = f'./data/test_preprocessed.csv'

train = pd.read_csv(training_file)
test = pd.read_csv(testing_file)
#print(train)
model = DecisionTree()
model.fit(data=train, target="Survived")
preditions = model.predict(test)
dot = export_graphviz(model,
                        out_file=None,
                        feature_names="feature_names",
                        class_names="target_names",
                        filled=True,
                        impurity=None,
                        )

graph = graphviz.Source(dot)
graph.render("titanic_decision_tree")




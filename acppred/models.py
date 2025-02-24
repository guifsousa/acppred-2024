from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from typing import Any
import pickle

class Model:
    def __init__(self, estimator:str):
        if estimator == 'random_forest':
            self.estimator = RandomForestClassifier()
        elif estimator == 'logistic_regression':
            self.estimator = LogisticRegression()
        else:
            raise Exception (f'{estimator} is not a valid estimator')

       
    
    def fit(self, X:Any, y:Any): 
        """
        Fits the underlying estimator.

        Args:
        - X (Any): training features in scikit-learn-compatible format.
        - y (Any): training labels in scikit-learn-compatible format.

        Return:
        -None
        """       
        self.estimator.fit(X, y)

    def predict(self, X:Any):
        """
        Predicts labels based on the underlying estimator.

        Args:
        - X (any): features in scikit-learn-compatible format.

        Return:
        - y_pred (Any): label probabilities in a scikit-learn-compatible format.
        """
        return self.estimator.predict(X)

    def predict_proba(self, X:Any):
        """
        Predicts labels based on the underlying estimator.

        Args:
        - X (any): features in scikit-learn-compatible format.

        Return:
        - y_pred (Any): label probabilities in a scikit-learn-compatible format.
        """
        return self.estimator.predict_proba(X)

    def save(self, filename:str):
        with open(filename, 'wb') as writer:
            writer.write(pickle.dumps(self))

    @staticmethod   
    def load(filename:str):
        """
        Loads model from a file.
        """
        with open(filename,'rb') as reader:
            return pickle.loads(reader.read())







from acppred.models import Model
from sklearn.metrics import classification_report
from sklearn.base import BaseEstimator
from argparse import ArgumentParser
import pickle
import pandas as pd

def train_model(csv_file:str, output_file:str, estimator:str) -> BaseEstimator:
    """
    Trains a classification model for anticancer peptide
    prediction from a amino acid composition CSV file and
    saves the model on a .pickel file. The trained model is
    returned by the function.

    Args:

    - csv_file (str): input file containing aa composition of anticancer
                    and non anticancer peptides.
    - output-file (str): output .pickle file with the trained model
    - estimator(str):type of the estimator to be tarined(logistic regression 
                    or random forest)

    Returns:

    - model (BaseEstimator): trained model.
    """

    df = pd.read_csv(csv_file)
    X_train = df.drop(['activity'], axis=1)
    y_train = df ['activity'] 

    model = Model(estimator= estimator)
    model.fit(X_train, y_train)
    model.save(output_file)

    return model

def evaluate_model(model:BaseEstimator, csv_file:str) -> str:
    """
    Evaluates a classification model using a testdataset and returns
    a classificatinon report

    Args:

    - model(BaseEstimator): a scikit-learn classifier
    - csv_file (str): a CSV file containing the test dataset

    Returns:

    - report (str) a classification report for the model
    """
    df = pd.read_csv(csv_file)
    X_test = df.drop(['activity'], axis=1)
    y_test = df['activity']
    y_pred = model.predict(X_test)
    report =classification_report(y_test, y_pred)
    return report

def main():

    argument_parser = ArgumentParser()
    argument_parser.add_argument('input_directory', help='directory containing the processed files.')
    argument_parser.add_argument('output', help='path to save the trained model')
    argument_parser.add_argument(
        '-e', '--estimator',
        help= 'type of the estimator to be trained',
        choices= ['random_forest', 'logistic_regression'],
        default='random_forest'
    )

    arguments = argument_parser.parse_args()
    model = train_model(f'{arguments.input_directory}/train.csv', arguments.output, arguments.estimator)
    report = evaluate_model(model, f'{arguments.input_directory}/test.csv')
    print(report)

if __name__ == '__main__':  
    main()
    

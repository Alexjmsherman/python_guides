# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:22:40 2017

@author: alsherman
"""

from sklearn.metrics import f1_score, precision_score, recall_score

def evaluate_f1(y_true, y_pred, average='binary'):
    print('precision: {}'.format(precision_score(y_true, y_pred, average=average)))
    print('recall: {}'.format(recall_score(y_true, y_pred, average=average)))
    print('f1_macro: {}'.format(f1_score(y_true, y_pred, average='macro')))
    print('f1_micro: {}'.format(f1_score(y_true, y_pred, average='micro')))
    print('f1_weighted: {}'.format(f1_score(y_true, y_pred, average='weighted')))
    print('f1_none: {}'.format(f1_score(y_true, y_pred, average=None)))

y_true = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
y_pred = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
evaluate_f1(y_true, y_pred)


# Imbalanced classes
y_true = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]

y_pred = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
evaluate_f1(y_true, y_pred)

y_pred = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
evaluate_f1(y_true, y_pred)


# Multiple classes
y_true = [0, 0, 0, 1, 1, 1, 2, 2, 2]

y_pred = [0, 0, 0, 1, 1, 1, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

y_pred = [1, 0, 0, 2, 1, 1, 0, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

y_pred = [0, 0, 0, 1, 1, 1, 1, 1, 2]
evaluate_f1(y_true, y_pred, average=None)


# Multiple classes - imbalanced classes
y_true = [0, 0, 1, 1, 1, 2, 2, 2, 2]

# one mistake in each class
y_pred = [1, 0, 2, 1, 1, 0, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

# mistake in least frequent class
# mistake is from most frequent class
y_pred = [2, 0, 1, 1, 1, 2, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

# mistake in least frequent class
# mistake is from 2nd most frequent class 
y_pred = [1, 0, 1, 1, 1, 2, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

# mistake in most frequent class
# mistake is from least frequent class
y_pred = [0, 0, 1, 1, 1, 0, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)

# mistake in most frequent class
# mistake is from 2nd most frequent class
y_pred = [0, 0, 1, 1, 1, 1, 2, 2, 2]
evaluate_f1(y_true, y_pred, average=None)





from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_squared_log_error

def evaluate_squared_error(y_true, y_pred):
    print('mae: {}'.format(mean_absolute_error(y_true, y_pred)))
    print('mse: {}'.format(mean_squared_error(y_true, y_pred)))
    print('msle: {}'.format(mean_squared_log_error(y_true, y_pred)))

y_true = [1, 1, 0, 0]

y_pred = [.1, 1, 0, 0]
evaluate_squared_error(y_true, y_pred)

y_pred = [.5, 1, 0, 0]
evaluate_squared_error(y_true, y_pred)

y_pred = [1, 0, 0, 0]
evaluate_squared_error(y_true, y_pred)

y_pred = [10, 1, 0, 0]
evaluate_squared_error(y_true, y_pred)

y_pred = [100, 1, 0, 0]
evaluate_squared_error(y_true, y_pred)

y_pred = [1000, 1, 0, 0]
evaluate_squared_error(y_true, y_pred)

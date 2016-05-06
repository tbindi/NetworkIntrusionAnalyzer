from sklearn.linear_model import LogisticRegression
from LogisticRegression import MultiLogistic
from InputData import get_plain, get_test, get_plain_text
from numpy import array, zeros, int as Int
import warnings


def fxn():
    warnings.warn("DeprecationWarning", DeprecationWarning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


def test_LR():
    file_train = '../kddcup.data_10_percent.out'
    file_test = '../corrected.out'
    print "------------ READING TRAIN ------------------"
    data, target = get_plain(file_train)
    print "------------ END TRAIN ------------------"
    print "------------ READING TEST ------------------"
    test_data, test_target = get_test(file_test)
    print "------------ END TEST ------------------"
    print " Logistic Regression Fitting: "
    classify = LogisticRegression(max_iter=100, multi_class='ovr')
    classify.fit(X=data, y=target)
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    predicted = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    actual = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    confusion_matrix = zeros((5,5), dtype=Int)
    print " Predicting class with TEST data: "
    for i, value in enumerate(array(test_data)):
        res = classify.predict(value)
        if res[0] == test_target[i]:
            TP += 1
            TN += 1
        else:
            FN += 1
            FP += 1
        predicted[int(res)] += 1
        actual[int(test_target[i])] += 1
        confusion_matrix[int(test_target[i])][int(res)] += 1
    print " ---- **** ------  ---- **** ------ "
    for key, value in predicted.iteritems():
        print key, ": ", value
    print " ---- **** ------  ---- **** ------ "
    for key, value in actual.iteritems():
        print key, ": ", value
    print " ---- **** ------  ---- **** ------ "
    print "  :  0 1 2 3 4"
    for i, value in enumerate(confusion_matrix):
        print i, ":", value
    print " ---- **** ------  ---- **** ------ "
    print "Accuracy: "
    print float(TP + TN) * 100/float(TP + TN + FP + FN)
    print "True Positive:", TP
    print "True Negative:", TN
    print "False Positive:", FP
    print "False Negative:", FN


def test_multi():
    x = array([[1, 1, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 0]])
    y = array([[1, 0, 0],
                 [1, 0, 0],
                 [1, 0, 0],
                 [0, 1, 0],
                 [0, 1, 0],
                 [0, 0, 1],
                 [0, 0, 1]])
    # data, target, features, classes
    classify = MultiLogistic(inp=x, clas=y, m=6, n=3)
    lr = 0.1
    cost_list = list()
    for i in xrange(300):
        classify.learn(lr=lr)
        cost = classify.neg_log_like()
        cost_list.append(cost)
        lr *= 0.95
    test = array([[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]])
    print classify.predict(test[0])


def test_logis():
    x = array([[1, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0],
               [1, 1, 1, 0, 0, 0],
               [0, 0, 1, 1, 1, 0],
               [0, 0, 1, 1, 0, 0],
               [0, 0, 1, 1, 1, 0],
               [0, 0, 1, 1, 1, 0]])
    y = array([0, 0, 1, 1, 2, 2, 2])
    classify = LogisticRegression(max_iter=300, multi_class='ovr')
    classify.fit(X=x, y=y)
    test = array([[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]])
    print classify.predict_proba(test[1])


def test_MLR():
    data, target = get_plain_text('../kddcup.data_10_percent.out')
    test_data, test_target = get_test('../test.data.out')
    classify = MultiLogistic(inp=data, clas=array(target), m=len(data[0]), n=5)
    lr = 0.1
    cost_list = list()
    for i in xrange(100):
        classify.learn(lr=lr)
        cost_list.append(classify.neg_log_like())
        lr *= 0.95
    for i in test_data:
        print classify.predict(i)


if __name__ == "__main__":
    test_LR()
    # test_MLR()
    # test_multi()
    # test_logis()



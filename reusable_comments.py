
# #
# iris = load_iris()
# # data = array(get_plain('../kddcup.data_10_percent.out'))
# X, y = iris.data[:-1,:], iris.target[:-1]
# logistic = LogisticRegression()
# logistic.fit(X, y)
# # print 'Predicted class %s, real class %s' % (logistic.predict(data.data[-1,\
# #         :]),data.target[-1])
# # print 'Probabilities for each class from 0 to 2: %s' % \
# #       logistic.predict_proba(data.data[-1,:])
#
# data = array(get_plain('../kddcup.data_10_percent.out'))


    # lr = 0.1
    # cost_list = list()
    # for i in xrange(100):
    #     classify.learn(lr=lr)
    #     # cost = classify.neg_log_like()
    #     # cost_list.append(cost)
    #     lr *= 0.95

# classify = MultiLogistic(data, target, features, classes)


# features = len(data[0])
# classes = 5


# x = array(get_data('../kddcup.data_10_percent.out'))
    # data, target = get_plain('../kddcup.data_10_percent.out')
    # test_data, test_target = get_test('../test.data.out')
    # logistic = LogisticRegression(max_iter=300, multi_class='ovr')
    # logistic.fit(X=data, y=target)
    # logistic.max_iter = 300
    # logistic.predict_proba(test_data)
    # """
    # samples = len(test_data)
    # features = len(test_data[0])
    # classify = MultiLogistic(test_data, test_target, samples, features)
    #
    # lr = 0.1
    # cost_list = list()
    # for i in xrange(300):
    #     classify.learn(lr=lr)
    #     cost = classify.neg_log_like()
    #     cost_list.append(cost)
    #     lr *= 0.95
    #
    # for i in test_data:
    #     print classify.predict(i)
    # """
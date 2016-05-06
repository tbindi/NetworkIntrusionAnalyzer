from numpy import zeros, dot, mean, array, asarray
from sklearn.metrics import log_loss
from Helper import softmax, entropy_mlr
from InputData import get_plain, target_names


class MultiLogistic:

    def __init__(self, inp, clas, m, n):
        self.x = array(inp)
        self.y = clas
        self.W = zeros((m, n))
        self.b = zeros(n)

    def neg_log_like(self):
        return log_loss(self.y, dot(self.x, self.W))
        # sig_act = softmax(dot(self.x, self.W) + self.b)
        # return entropy_mlr(self.y, sig_act)

    def learn(self, lr=0.1, inp=None, l2=0.0):
        if inp is not None:
            self.x = inp

        p_y_x = softmax(dot(self.x, self.W) + self.b)
        d_y = self.y - p_y_x

        self.W += lr * dot(self.x.T, d_y) - lr * l2 * self.W
        self.b += lr * mean(d_y, axis=0)

    def predict(self, a):
        # Softmax for Multinomial Logistic Regression
        return softmax(dot(a, self.W) + self.b)


if __name__ == "__main__":
    # x = array(get_data('../kddcup.data_10_percent.out'))
    data, target = get_plain('../kddcup.data_10_percent.out')
    logistic = MultiLogistic(data, target, len(data), len(data[0]))

    # y = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    # x = array([[1, 1, 1, 0, 0, 0],
    #             [1, 0, 1, 0, 0, 0],
    #             [1, 1, 1, 0, 0, 0],
    #             [0, 0, 1, 1, 1, 0],
    #             [0, 0, 1, 1, 0, 0],
    #             [0, 0, 1, 1, 1, 0]])
    # y = array([[1, 0],
    #              [1, 0],
    #              [1, 0],
    #              [0, 1],
    #              [0, 1],
    #              [0, 1]])
    # m = x.shape[0]
    # n = len(x[0])
    # classify = MultiLogistic(inp=x, clas=y, m=m, n=n)
    # lr = 0.1
    # cost_list = list()
    # for i in xrange(300):
    #     classify.learn(lr=lr)
    #     cost = classify.neg_log_like()
    #     cost_list.append(cost)
    #     lr *= 0.95
    #
    # # model = LogisticRegression(class_weight='balanced')
    # # model = model.fit(x, y)
    # x = array([1,1,0,0,'smtp',0,0,1,0,1234,386,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
    #            1,2,
    #            0.00,
    #            0.00,0.00,0.00,1.00,0.00,1.00,255,11,0.04,0.02,0.00,0.00,0.89,0.00,0.00,0.00,'normal'])
    # print classify.predict(x)


import sys
import time
import math

class Gradient_descent:
    def __init__(self):
        self.fname = {"train": "train.csv",
                        "test": "test.csv",
                        "result": "result.csv"}
        self.dim = 3
        self.thetas = [0.0 for _ in range(self.dim)]
        self.cost = None
        self.N = None
        self.speed = 0.1
        self.T = 5000

        self.h_func = lambda xs, thetas: sum([x * thetas[i] for i, x in enumerate(xs)])
        #self.slope_func = lambda X, Y, i, thetas: (1 / len(X)) * sum()
        self.cost_func = lambda X, Y, hf, thetas: (1.0 / len(X)) * sum([(hf(xs, thetas) - Y[r])**2 for r, xs in enumerate(X)])

    def run(self):
        self.train()
        self.test()

    def train(self):
        X, Y = self.readData(self.fname["train"])
        self.gradient_descent(X, Y)

    def test(self):
        X, Y = self.readData(self.fname["test"])
        self.predict(X, Y)

    def readData(self, fname):
        print "Reading data...\n"
        data = [[float(x) for x in xs.strip().split(',')] for xs in open(fname)]
        X, Y = [row[:-1] for row in data], [row[-1] for row in data]

        self.N = len(data)

        return X, Y

    def gradient_descent(self, X, Y):
        for t in xrange(self.T):
            for i in xrange(self.dim):
                self.thetas[i] -= self.speed * self.slope_func(X, Y, i)
            
            self.cost = self.cost_func(X, Y, self.h_func, self.thetas)
            print self.cost

    # avoid closure
    def slope_func(self, X, Y, idx):
        return (1.0 / len(X)) * sum([xs[idx] * (self.h_func(xs, self.thetas) - Y[r]) for r, xs in enumerate(X)])
        
    def predict(self, X, Y):
        with open(self.fname["result"], "w") as fd:
            for r, xs in enumerate(X):
                fd.write(str(self.h_func(xs, self.thetas)) + "\t==>\t" + str(Y[r]) + "\n")


if __name__ == "__main__":
    Gradient_descent().run()


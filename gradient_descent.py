
import sys
import time
import math

class Gradient_descent:
    def __init__(self):
        self.fname = {"train": "train.csv",
                        "test": "test.csv"}
        self.thetas = None
        self.cost = None
        self.h_func = lambda xs, thetas: sum([x * thetas[i] for i, x in enumerate(xs)])
        self.N = None
        self.dim = None
        self.speed = 0.1

    def run(self):
        self.train()
        self.test()

    def train(self):
        X, _ = self.readData(self.fname["train"])
        self.gradient_descent(X)

    def test(self):
        pass

    def readData(self, fname):
        print "Reading data...\n"
        return ()

    def gradient_descent(X):
        pass

    def predict(self):
        pass


if __name__ == "__main__":
    Gradient_descent().run()


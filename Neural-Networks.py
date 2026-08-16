import numpy as np

print("Rohit Nyaupane 4th sem CSIT")

def perceptron(X, y, epochs=10, lr=0.1):
    weights = np.zeros(X.shape[1])
    bias = 0

    for _ in range(epochs):
        for i in range(len(X)):
            output = 1 if np.dot(X[i], weights) + bias >= 0 else 0
            error = y[i] - output

            weights += lr * error * X[i]
            bias += lr * error

    return weights, bias


def predict(X, weights, bias):
    return [1 if np.dot(x, weights) + bias >= 0 else 0 for x in X]


# Input
X = np.array([[0,0], [0,1], [1,0], [1,1]])

# AND gate
AND = np.array([0, 0, 0, 1])
w, b = perceptron(X, AND)
print("AND:", predict(X, w, b))

# OR gate
OR = np.array([0, 1, 1, 1])
w, b = perceptron(X, OR)
print("OR :", predict(X, w, b))
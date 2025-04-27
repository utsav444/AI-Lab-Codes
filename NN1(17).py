import numpy as np

np.random.seed(42)

N = 3
hidden_layer1_neurons = 4
hidden_layer2_neurons = 3
output_neurons = 1
steps = 1000

X = np.random.randint(0, 2, (10, N))
Y = np.random.randint(0, 2, (10, 1))

W1 = np.random.randn(N, hidden_layer1_neurons)
b1 = np.random.randn(hidden_layer1_neurons)

W2 = np.random.randn(hidden_layer1_neurons, hidden_layer2_neurons)
b2 = np.random.randn(hidden_layer2_neurons)

W3 = np.random.randn(hidden_layer2_neurons, output_neurons)
b3 = np.random.randn(output_neurons)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for step in range(steps):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    Z3 = np.dot(A2, W3) + b3
    A3 = sigmoid(Z3)


print("W1:\n", W1)
print("b1:\n", b1)
print("W2:\n", W2)
print("b2:\n", b2)
print("W3:\n", W3)
print("b3:\n", b3)
print("Steps:\n", steps)
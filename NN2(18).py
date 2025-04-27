import numpy as np

np.random.seed(42)

N = 4
hidden_layer1_neurons = 5
output_neurons = 2
steps = 1000

X = np.random.randint(0, 2, (10, N))
Y = np.random.randint(0, 2, (10, output_neurons))

W1 = np.random.randn(N, hidden_layer1_neurons)
b1 = np.random.rand(hidden_layer1_neurons)

W2 = np.random.rand(hidden_layer1_neurons, output_neurons)
b2 = np.random.rand(output_neurons)

def sigmoid(x):
    return 1 / 1 + np.exp(-x)

for step in range(steps):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

print("W1:\n", W1)
print("b1:\n", b1)
print("W2:\n", W2)
print("b2:\n", b2)
print("Steps:\n", steps)
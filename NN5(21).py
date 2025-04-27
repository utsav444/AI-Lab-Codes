import numpy as np

np.random.seed(42)

N = 4
hidden_layer1_neurons = 5
hidden_layer2_neurons = 4
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

def tanh(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x) ** 2

learning_rate = 0.1
epochs = 1000

for epoch in range(epochs):
    Z1 = np.dot(X, W1) + b1
    A1 = tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = tanh(Z2)
    Z3 = np.dot(A2, W3) + b3
    A3 = tanh(Z3)

loss = np.mean(np.square(Y - A3))

d_output = (Y - A3) * tanh_derivative(Z3)
d_hidden2 = np.dot(d_output, W3.T) * tanh_derivative(Z2)
d_hidden = np.dot(d_hidden2, W2.T) * tanh_derivative(Z1)

W1 -= learning_rate * np.dot(X.T, d_hidden)
b1 -= learning_rate * np.sum(d_hidden, axis=0)
W2 -= learning_rate * np.dot(A1.T, d_hidden2)
b2 -= learning_rate * np.sum(d_hidden2, axis=0)
W3 -= learning_rate * np.dot(A2.T, d_output)
b3 -= learning_rate * np.sum(d_output, axis=0)

print("W1:\n", W1)
print("b1:\n", b1)
print("W2:\n", W2)
print("b2:\n", b2)
print("W3:\n", W3)
print("b3:\n", b3)
print("Loss:\n", loss)
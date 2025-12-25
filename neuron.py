import numpy as np
import math

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Example: one output neuron for letter "A"
def neuron(inputs, weights, bias):
    z = np.dot(inputs, weights) + bias
    return sigmoid(z)

# Imagine your image is 4 pixels (super simplified!)
image = np.array([0, 0, 255, 255, 255, 255, 0, 0])  # input vector
weights = np.array([0, 0, 1, 1, 0, 1, 0, 0])
bias = -0.1

output = neuron(image, weights, bias)
print("Probability letter is 'A':", output)


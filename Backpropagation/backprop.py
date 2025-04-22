import numpy as np

# Activation function and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)

# -----------------------
# USER INPUT
# -----------------------
print("🔢 Enter the XOR input (two binary values - 0 or 1):")
inp1 = int(input("Input 1: "))
inp2 = int(input("Input 2: "))
expected = int(input("Expected Output (0 or 1): "))

X = np.array([[inp1, inp2]])
y = np.array([[expected]])

# Initialize weights and biases
wh = np.array([[0.4, 0.2],   # input → hidden weights
               [0.3, 0.7]])
bh = np.array([[0.1, 0.1]])  # hidden bias

wo = np.array([[0.6],        # hidden → output weights
               [0.9]])
bo = np.array([[0.05]])      # output bias

# -----------------------
# FORWARD PROPAGATION
# -----------------------
hidden_input = np.dot(X, wh) + bh
hidden_output = sigmoid(hidden_input)

output_input = np.dot(hidden_output, wo) + bo
predicted_output = sigmoid(output_input)

print("\n🔄 Forward Propagation Results:")
print("Hidden layer input:", hidden_input)
print("Hidden layer output:", hidden_output)
print("Output layer input:", output_input)
print("Predicted output:", predicted_output)

# -----------------------
# CALCULATE ERROR
# -----------------------
error = y - predicted_output
print("\n❌ Error:", error)

# -----------------------
# BACKWARD PROPAGATION
# -----------------------
d_output = error * sigmoid_derivative(predicted_output)

error_hidden = d_output.dot(wo.T)
d_hidden = error_hidden * sigmoid_derivative(hidden_output)

# -----------------------
# UPDATE WEIGHTS & BIASES
# -----------------------
learning_rate = 0.1

wo += hidden_output.T.dot(d_output) * learning_rate
bo += d_output * learning_rate

wh += X.T.dot(d_hidden) * learning_rate
bh += d_hidden * learning_rate

# -----------------------
# Show updated parameters
# -----------------------
print("\n✅ Updated Weights and Biases After Backpropagation:")
print("Updated input → hidden weights:\n", wh)
print("Updated hidden biases:\n", bh)
print("Updated hidden → output weights:\n", wo)
print("Updated output bias:\n", bo)

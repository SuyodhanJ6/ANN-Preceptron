# ANN-Preceptron
Perceptrons are the building blocks of neural networks. It is typically used for supervised learning of binary classifiers.

# Preceptron : 
In the modern sense, the perceptron is an algorithm for learning a binary classifier called a threshold function: a function that maps its input  {x}  (a real-valued vector) to an output value f(x) (a single binary value):


![function](https://user-images.githubusercontent.com/59029708/205625381-65c0ad04-3857-4c83-b9d4-fe35450affd2.png)

The Network Looks Like : 


![netwok](https://user-images.githubusercontent.com/59029708/205625717-f7ee71e4-6762-40da-9e06-f94706865d78.png)

# The Perceptron Algorithm:
# 1. Input: 
All the features of the model we want to train the neural network will be passed as the input to it, Like the set of features [X1, X2, X3…..Xn]. Where n represents the total number of features and X represents the value of the feature.

# 2. Weights: 
Initially, we have to pass some random values as values to the weights and these values get automatically updated after each training error that is the values are generated during the training of the model. In some cases, weights can also be called as weight coefficients.

# 3. Weights Sum:
Each input value will be first multiplied with the weight assigned to it and the sum of all the multiplied values is known as a weighted sum.

# 4. Activation Function:
Activation function applies step rule which converts the numerical value to 0 or 1 so that it will be easy for data set to classify. Based on the type of value we need as output we can change the activation function.

# 4.1 Bias
If you notice, we have passed value one as input in the starting and W0 in the weights section W0 is an element that adjusts the boundary away from origin to move the activation function left, right, up or down. since we want this to be independent of the input features, we add constant one in the statement so the features will not get affected by this and this value is known as Bias.

# Features added with perceptron make in deep neural networks. Back Propagation is the most important feature in these.

# 5. Backpropagation :
After performing the first pass (based on the input and randomly given inputs) error will be calculated and the back propagation algorithm performs an iterative backward pass and try to find the optimal values for weights so that the error value will be minimized. To minimize the error back propagation algorithm will calculate partial derivatives from the error function till each neuron’s specific weight, this process will give us complete transparency from total error value to a specific weight that is responsible for the error.

### Okay
First we Run Create Preceptron1.py
Then prepare_data.py
Then we crate sepreate file for or gate, and gate and xor gate --> run it.
in above file we are saving model 
then last we plot the gate 
# eg.or gate
![or](https://user-images.githubusercontent.com/59029708/205628889-526455c3-e118-41fa-8640-12bc9f7b162b.png)

# requirments.txt
matplotlib
seaborn
numpy
pandas



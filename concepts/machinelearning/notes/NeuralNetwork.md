<p>Consider a neural network with 5 hidden layers. Choose the options that are correct for feedforward propagation.</p>
<b>Ans :</b>
<ul>
<li>The output of the third hidden layer can be calculated only after the output of the second hidden layer is computed in one feed forward pass.<br>
In feed forward, the output of the layer 'l' can be calculated only after the calculation of the output of all the 'l-1' layers.
<li>The output of the fifth hidden layer can be calculated only after the output of the second hidden layer is computed in one feed forward pass.<br>
In feed forward, the output of the layer 'l' can be calculated only after the calculation of the output of all the 'l-1' layers.
</ul>
<hr>

<p>Consider a neural network with 5 hidden layers. You feed an input batch of 20 data points into the network. How will you denote the weight matrix between the hidden layers 4 and 5?</p>
<b>Ans :</b>W^5<br>
<b>Explaination :</b>W^l is the weight matrix between the layers l and l-1.
<hr>

<p>Consider a neural network with 5 hidden layers. You feed an input batch of 20 data points into the network. The weight matrix W^3 has the dimensions (18,12). How many neurons are present in the hidden layer 2?</p>
<b>Ans :</b>12<br>
<b>Explaination :</b>Weight matrix dimensions = (Number of neurons in the layer l, Number of neurons in layer 'l-1')
<hr>

<h3>Basic Hyperparameters of Neural Network</h3>
<p>The hyperparameters in a neural network are ________. (Note: More than one option may be correct.)</p>
<b>Ans :</b>
<ul>
<li>The number of layers<br>
Weights and biases are parameters to be found by training the learning algorithm. The number of layers is one of the predefined hyperparameters.
<li>The number of neurons in each layer<br>
Weights and biases are parameters to be found by training the learning algorithm. The number of neurons is one of the predefined hyperparameters.
</ul>
<hr>

<h3>Inputs</h3>
<p>Suppose you want to classify an RGB image with an input of 32 x 32 pixels as ‘dog’, ‘cat’, ‘bird’ or ‘none of the above’. How many neurons will the input layer have?</p>
<b>Ans :</b>3072<br>
<b>Explaination :</b>A black-and-white 32 x 32 image will have 32 x 32 input neurons. However, since an RGB image has 3 channels, the network will have 32 * 32 * 3 = 3072 input neurons.
<hr>

<h3>Outputs</h3>
<p>Suppose you want to classify an RGB image with an input of 32 x 32 pixels as ‘dog’, ‘cat’, ‘bird’ or ‘none of the above’. How many neurons will the output layer have?</p>
<b>Ans :</b>4<br>
<b>Explaination :</b>Since there are 4 classes,i.e., ‘dog’, ‘cat’, ‘bird’ and ‘none of the above’, we will have 4 output neurons.
<hr>

<h3>Output layer</h3>
<p>Suppose you want to classify an RGB image with an input of 32 x 32 pixels as ‘dog’, ‘cat’, ‘bird’ or ‘none of the above’. Would you use a sigmoid/ softmax layer as the output layer?</p>
<b>Ans :</b>Softmax<br>
<b>Explaination :</b>Since there are 4 classes, we would use a softmax function in the output layer.
<hr>

<h3>Notations</h3>
<p>How would you denote the output of the third hidden layer?</p>
<b>Ans :</b>h^3<br>
<b>Explaination :</b>The output of a hidden layer is denoted by h. The superscript denotes the layer number. Hence h^3 is the correct answer. Note: Since a specific neuron is not mentioned, we do not have a subscript.
<hr>

<p>How would you denote the weight that connects the sixth neuron of the hidden layer 3 to the eighth neuron of the hidden layer 4?</p>
<b>Ans :</b>w^4v86<br>
<b>Explaination :</b>Here, the notation w^4
 indicates the weights for the fourth hidden layer because the superscript is 4. Also, in the subscript, we have the neuron of the 
lth layer, i.e., 8 as the first number and the neuron of the (l−1)th layer, i.e., 6 as the second number. Since this is the case, the answer is correct.
<hr>

<h3>Number of Interconnections</h3>
<p>We have the hidden layer number 3 with 11 neurons and the hidden layer number 4 with 18 neurons. Also, these hidden layers are densely connected. How many connections will be there between the two hidden layers?</p>
<b>Ans :</b>198<br>
<b>Explaination :</b>Number of interconnections = Number of neurons in layer l x Number of neurons in layer (l−1)
                                                                   = 11 * 18 = 198
<hr>

<h3>Assumptions of Neural Network</h3>
<p>State whether the following statement is true or false.<br>

According to the assumptions of neural networks, the activation function of all the neurons in one particular layer is the same.</p>
<b>Ans :</b>True<br>
<b>Explaination :</b>All neurons in a particular hidden layer use the same activation function. Hence, this answer is correct.
<hr>
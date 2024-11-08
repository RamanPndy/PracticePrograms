<p>Which of the following is the correct order if you arrange RNNs according to the network training time?</p>
<b>Ans :</b>Bidirectional LSTM > LSTM > GRU > Vanilla RNN<br>
<b>Explaination :</b>The time it takes to train an RNN corresponds to the number of parameters present an architecture. If a vanilla RNN has 'n' number of parameters then the number of parameters a GRU, LSTM and bidirectional LSTM are 3n, 4n and 8n, respectively.
<hr>

<p>Keras accepts batch dimensions of the input data in which of the following formats?</p>
<b>Ans :</b>(#samples, #timesteps, #features)
<hr>

<p>In which of the following RNN types, you don't use a TimeDistributed() layer at the output?</p>
<b>Ans :</b>Many-to-one<br>
<b>Explaination :</b>You only use a TimeDistributed() layer when the RNN outputs output a sequence. Therefore, you don't use it in a many-to-one RNN model.
<hr>

<h3>Bidirectional RNNs</h3>
<p>Which of the following applications can bidirectional RNNs be used for? More than one options may be correct.</p>
<b>Ans :</b>
<ul>
<li>Speech recognition - given a set of audio files, transcribing them into text in the same language<br>
The entire audio file is given to the network, so it can look ahead in time and use both the forward and backward contexts.
<li>Machine translation - given a set of English sentence, translating it to another language such as French or Hindi.<br>
The entire sentence is given to the network, so it can look ahead.
</ul>
<hr>

<p>Which of the following is not a feature of an LSTM cell?</p>
<b>Ans :</b>An LSTM cell replaces an entire RNN layer<br>
<b>Explaination :</b>An LSTM is similar to an RNN layer except that the RNN cells are replaced with LSTM cells.
<hr>

<p>Which of the following functions are present in the update gate of an LSTM cell?</p>
<b>Ans :</b>A sigmoid and a tanh function<br>
<b>Explaination :</b>The update gate in an LSTM cell has one sigmoid function and one tanh function.<br>
LSTM cell has more parameters than a vanilla RNN cell<br>
You can build an RNN network with multiple LSTM layers.<br>
Only the forget and the update gate are responsible for the new cell state ct of a cell in an LSTM cell.<br>
Bidirectional RNNs can only be built in case of offline sequences where the sequences are already available.
<hr>

<h3>The LSTM Cell</h3>
<p>The LSTM cell is able to solve the problem of vanishing gradients because (only one option is correct):</p>
<b>Ans :</b>The gradient is propagated from the cell state ct to the previous cell state ct−1 without any weights involved directly between ct and ct−1 which ensures that at least some gradient is always propagated backwards in time<br>
<hr>

<p>Suppose you’re building a sentiment classifier based on users’ reviews on a product. The model is expected to predict a numeric ‘sentiment score’ for each review. Which of the following RNN architectures will be most suitable for this kind of problem?</p>
<b>Ans :</b>Many-to-one architecture<br>
<b>Explaination :</b>The input, a review, is a sequence of words and the output, the sentiment label, is a single entity. Hence, this architecture will be most suitable in this case.
<hr>

<h3>A Many-to- One RNN</h3>
<p>Consider a many-to-one recurrent neural network with 20 timesteps and a batch size of 32 (batch size refers to the number of sequences fed into the network in one iteration). The network architecture is as follows:</p>

![Alt text](images/rnn.png)

<p>What is the size of W^2vR?</p>
<b>Ans :</b>(8, 8)<br>
<b>Explaination :</b>We know that the W^lvR is of size (#neurons at layer l, #neurons at layer l). The second hidden layer has 8 neurons. Therefore, its dimension is (8, 8).
<hr>

<p>What is the size of a^1v8?</p>
<b>Ans :</b>(5, 32)<br>
<b>Explaination :</b>We know that the a^lvt is (#neurons at layer l, #batch_size). The first hidden layer has 5 neurons and the batch size is 32. Therefore, its dimension is (5, 32)<br>
The size of a^2v3 is larger than the size of a^2v10. Size of both a^2v3 and a^2v10 is (8, 32).
<hr>

<p>Suppose you change the batch size from 32 to 128. Which of the following matrix sizes will be affected by this change?</p>
<b>Ans :</b>a^2v20<br>
<b>Explaination :</b>The size of a^2v20 will change to (8, 128) from (8, 32) after changing the batch size.
<hr>
<p>In a knowledge graph, what do edges represent?</p>
<b>Ans :</b>Semantic relations<br>
<b>Explaination :</b>Nodes represent entities, and edges represent the semantic relations between them.
<hr>

Hyponym is a relation between a concept and its subordinate

To compute the cosine similarity between two points \( A(x_1, y_1) \) and \( B(x_2, y_2) \), we use the formula:

\[
\text{Cosine Similarity} = \frac{A \cdot B}{\|A\| \cdot \|B\|}
\]

Where:
- \( A \cdot B = x_1x_2 + y_1y_2 \) is the dot product.
- \( \|A\| = \sqrt{x_1^2 + y_1^2} \) is the magnitude of \( A \).
- \( \|B\| = \sqrt{x_2^2 + y_2^2} \) is the magnitude of \( B \).

### Points:
- \( \text{King} = (8, 5) \)
- \( \text{Queen} = (8, 11) \)

#### 1. Dot Product:
\[
A \cdot B = (8 \cdot 8) + (5 \cdot 11) = 64 + 55 = 119
\]

#### 2. Magnitudes:
\[
\|A\| = \sqrt{8^2 + 5^2} = \sqrt{64 + 25} = \sqrt{89}
\]
\[
\|B\| = \sqrt{8^2 + 11^2} = \sqrt{64 + 121} = \sqrt{185}
\]

#### 3. Cosine Similarity:
\[
\text{Cosine Similarity} = \frac{119}{\sqrt{89} \cdot \sqrt{185}}
\]

Let me calculate this explicitly.

The cosine similarity between \( \text{King}(8,5) \) and \( \text{Queen}(8,11) \) is approximately **0.9274**.

Cosine Similarity of unrelated words is zero,S(Q,R) = 0

Which of the following is true about negative sampling?
The pairs chosen for negative sampling are random and frequent.
The pairs chosen for negative sampling are random and infrequent.
The correct statement about negative sampling is:


The pairs chosen for negative sampling are random and infrequent.

Which of the following is the correct training sample for the following corpus with a context window of 2?

‘The quick brown fox jumps over the lazy dog’

X = (quick, fox) Y = 1
X = (jumps, the) Y = 1
The pairs that occur in the context size of 2 will have an output of 1; the output will be 0 for all the other cases.

What input do you give to a Topic Model? 
Tfidf matrix
Document topic matrix
Topic term matrix
Ans: Tfidf matrix 
We provide tfidf as an input to topic modelling algorithm
The input to a topic model is typically a **term-document matrix**, such as a bag-of-words (BoW) matrix or a **TF-IDF matrix**. These matrices represent the frequency or weighted importance of terms across a set of documents and form the basis for identifying topics through unsupervised learning techniques like Latent Dirichlet Allocation (LDA). 

### Correct Answer: **Tfidf matrix**

Let’s consider the input matrix of NMF algorithm,X that has a size of (100,289). 
X is decomposed into W and H using the NMF algorithm.
Number of topics = 10
What will be the size of the H matrix (topic term matrix)?
Ans: (10,289)
H is of the size (number of topics X number of terms) = (10,289)
In the Non-Negative Matrix Factorization (NMF) algorithm, the input matrix \( X \) of size \( (100, 289) \) is factorized into two matrices \( W \) and \( H \), such that:  
\[ X \approx W \times H \]

Where:  
- \( W \) is the document-topic matrix, sized \( (100, \text{Number of Topics}) \).  
- \( H \) is the topic-term matrix, sized \( (\text{Number of Topics}, 289) \).  

Given that the number of topics is 10, the size of the \( H \) matrix will be:  
**(10, 289)**.

The Frobenius norm of a matrix \( A \) is calculated as the square root of the sum of the squares of all its elements. For the given matrix:

\[
A = 
\begin{bmatrix}
1 & 3 & 1 \\
3 & 2 & 1 \\
4 & 3 & 2
\end{bmatrix}
\]

1. Compute the sum of squares of all elements:
   \[
   1^2 + 3^2 + 1^2 + 3^2 + 2^2 + 1^2 + 4^2 + 3^2 + 2^2 = 1 + 9 + 1 + 9 + 4 + 1 + 16 + 9 + 4 = 54
   \]

2. Take the square root:
   \[
   \text{Frobenius norm} = \sqrt{54} \approx 7.35
   \]

So, the Frobenius norm is approximately **7.35**.

Given an input matrix X with the dimensions (16,18) and the number of topics is 4.
NMF decomposes a matrix X such that X ≈ WxH, W ≥ 0, H ≥ 0

What is the dimension of matrix W?
Ans:(16,4)
The size of W is (document,topics) = (16,4)
In Non-Negative Matrix Factorization (NMF), the input matrix \( X \) of size (16, 18) is decomposed into two matrices \( W \) and \( H \) such that:

\[
X \approx W \times H
\]

Where:
- \( W \) represents the matrix of document-topic associations.
- \( H \) represents the matrix of topic-term associations.
- The number of topics is given as 4.

The dimension of matrix \( W \) will be \( (16, 4) \), where:
- 16 is the number of documents (rows in \( X \)),
- 4 is the number of topics (number of columns in \( W \)).

So, the dimension of matrix \( W \) is **(16, 4)**.

What are the different methods of semantic processing covered in this course? (Multiple options can be correct)
POS tagging
Word2vec
Topic Modelling
All of the above
Ans: Word2vec, Topic Modelling
The correct answer is **All of the above**. 

- **POS tagging** (Part-of-Speech tagging) involves classifying words into categories such as nouns, verbs, adjectives, etc.
- **Word2vec** is a technique used for converting words into vector representations that capture semantic meanings.
- **Topic Modeling** is used to discover the topics present in a collection of texts.

All of these are methods of semantic processing.

State whether the following statement is true or false.
Topic Modelling algorithms explicitly give the labels of the topics as the output
Ans: False
This is the job of a data scientist to give relevant labels to the topics as the topic modelling algorithm would not explicitly give you the topics.

Which of the following is the correct sequence of the code to produce the W and H matrices?
A. N_TOPICS = 15
nmf = NMF(n_components=N_TOPICS)
W = nmf.fit_transform(X)  
H = nmf.components_  

B. N_TOPICS = 15
nmf = NMF(n_components=N_TOPICS)
W = nmf.components_ 
H =nmf.fit_transform(X) 

C.nmf = NMF(n_components=N_TOPICS)
H = nmf.transform(X)  
W = nmf.components_

Ans: N_TOPICS = 15
nmf = NMF(n_components=N_TOPICS)
W = nmf.fit_transform(X)  
H = nmf.components_  

Define semantic processing and list the different methods involved in it.
Semantic processing refers to the analysis of the meaning and context of text data to understand the underlying concepts and relationships. It is a critical step in natural language processing (NLP) that helps machines comprehend the nuances of human language.

Methods involved in semantic processing include:
- **POS tagging**: Identifying parts of speech in sentences.
- **Word2Vec**: Mapping words to vector representations based on context.
- **Topic Modeling**: Identifying hidden topics in a collection of documents (e.g., LDA, NMF).
- **Named Entity Recognition (NER)**: Detecting entities like names, dates, locations.

What is the difference between semantic and syntactic natural language processing?
The key difference between semantic and syntactic natural language processing (NLP) lies in their focus:

- **Syntactic NLP** focuses on the structure of sentences, including grammar rules, sentence parsing, and word relationships based on syntax.
- **Semantic NLP**, on the other hand, deals with the meaning behind words, sentences, and phrases, capturing context, concepts, and relationships to interpret the intended message.

Syntactic processing analyzes form, while semantic processing interprets content and meaning.

What are the real-life applications of semantic processing?
Real-life applications of semantic processing include:

1. **Sentiment Analysis**: Determining opinions, emotions, or sentiments from text (e.g., social media posts, reviews).
2. **Machine Translation**: Translating content while preserving the meaning across languages.
3. **Chatbots and Virtual Assistants**: Enabling conversations by understanding intent and context.
4. **Recommendation Systems**: Suggesting items by interpreting user preferences and behaviors.
5. **Information Retrieval**: Enhancing search engines to return more relevant results based on the meaning of queries.
6. **Question Answering Systems**: Providing direct answers based on the context of the question.

What are some of the algorithms used in topic modelling?
Some common algorithms used in topic modeling include:

1. **Latent Dirichlet Allocation (LDA)**: A probabilistic model that assumes documents are mixtures of topics and that topics are mixtures of words.
2. **Non-negative Matrix Factorization (NMF)**: Decomposes the term-document matrix into two non-negative matrices to identify hidden patterns.
3. **Latent Semantic Analysis (LSA)**: Uses singular value decomposition to reduce dimensionality and capture latent semantic structures in text.
4. **Correlated Topic Model (CTM)**: Extends LDA by allowing correlation between topics.

What are the different algorithms in Word2vec? List their similarities and differences.
Word2Vec offers two primary algorithms:

1. **Continuous Bag of Words (CBOW)**: Predicts the target word based on a context of surrounding words. It is faster and works well with smaller datasets.
   
2. **Skip-gram**: Predicts the context words from a given target word. It performs better for larger datasets and is particularly useful for rare words.

**Similarities**: Both aim to learn word embeddings and represent words in a continuous vector space.

**Differences**: CBOW focuses on predicting a word from its context, while Skip-gram predicts context words from a given word.
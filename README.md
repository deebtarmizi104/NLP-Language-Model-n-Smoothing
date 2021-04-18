# NLP-Language-Model-n-Smoothing

Write a Python program (modify the file ngram_test.py) that calculates the
probability of the following sentence using a trigram model (ignore the
start <s> and end <s/> marker for now) :

“Most mental disorders can is treatable through early detection of signs or symptoms”

Use the training data set in the file “text-gram.dat” provided.

Steps:
1. Create a python dictionary that stores trigrams and its counts for all possible
trigrams of the sentences in the training file.
2. Create a python dictionary that stores bigrams and its counts for all possible
bigrams of the sentences in the training file.
3. Create a python dictionary of all trigrams and its counts in the testing
sentence (above)
4. Calculate probability of each trigram in test sentence and apply smoothing
using the formula :

no. of times the trigram in test sentence is found in training/no. of times the bigram in test sentence is found in training

Example: [C(is treatable through) + 1]/[C(is treatable) + V] = (0+1)/(1+81) = 0.0122

Calculate the probability of the whole sentence by summing all prob. of
trigrams together using log likehood.

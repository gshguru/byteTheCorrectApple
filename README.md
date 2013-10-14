Byte The Correct Apple
======================

This code was actually written for competition held by hackerrank.com.
Link to problem statement: https://www.hackerrank.com/contests/october-data-science/challenges/byte-the-correct-apple

**Problem Statement:**

*You are provided a text file, with a number of lines. Each line contains either a sentence or a paragraph or a text snippet which could either be related to Apple, the computer company, or the apple, the fruit. Your task is to perform disambiguation between these two groups and identify which one is being referred to. It is possible that the plural or the possessive form of Apple might exist in some of the tests (apples, Apple’s).*

**Training Data:** Text from wiki pages for both apple, the fruit and Apple, the company. 

**Input Format:** An Integer N, followed by N text snippets

**Output Format:** N lines of output  

**Sample Input**

2

Apple already plans to buy back $100 billion in shares, including $16 billion worth last quarter. Icahn probably pounded the dinner table he and Cook shared recently for their much-reported bread-breaking at Icahn's New York apartment. Apple's cash stash currently sits at a whopping $145 billion but only $43 billion is in the U.S., which is why Icahn wants to float bonds to cover a buy back.

Fortunately, there are “low-chill” apple varieties for temperate climates. (Chilling hours are defined as nonconsecutive hours of winter temperatures below 45 degrees.) As a general guide, if you live on or near the coast, your garden gets only 100 to 200 chilling hours. Inland San Diego gardens get about 400 to 500 chilling hours — still considered “low chill.”

**Sample Output**

computer-company

fruit


**My Approach:**

I used simple text processing utilities provided by scikit learn to get >90% accuracy on hidden data set. 
Model used was Bernoulli’s Naïve Bayes.

Intelligent data preprocessing can actually pull accuracy towards 100%. Probably the model is failing in case of multiple occurrences of word apple (like eating apple at Apple headquarters).

**Possible Developments:**

Accuracy can be increased by further preprocessing which require nlp libraries like  NLTK. 


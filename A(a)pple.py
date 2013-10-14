# Author    : Gurupad Hegde, gshguru@gmail.com
# Descrition: Determine whether a text snippet which could either be related to 
# 			  Apple, the computer company, or the apple, the fruit
# Date		: 13th Oct 2013
# Link      : https://www.hackerrank.com/contests/october-data-science/challenges/byte-the-correct-apple

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
count_vect = CountVectorizer(lowercase = False, ngram_range = (1,2), max_df=0.95)
tfidf_transformer = TfidfTransformer(use_idf=False)

train_data = []			# data store for training data, list of strings
test_data = []			# data store for test data, list of strings
train_y = []			# data store for target variables for training, list of A(a)pples

def predict():
	# training set text processing
	X_train_counts = count_vect.fit_transform(train_data)	
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	# training set text processing
	X_new_counts = count_vect.transform(test_data)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)

	# initializing model
	from sklearn.naive_bayes import BernoulliNB
	clf = BernoulliNB(alpha=.06)  #94

	# model fitting
	clf = clf.fit(X_train_tfidf, train_y)

	# predicting answers for test set
	predicted = clf.predict(X_new_tfidf)
	for results in predicted: print results

# reading trainig data from text files
for line in open('apple-computers.txt'):
	if len(line.strip())>0:				#skip empty lines
		train_data.append(line.strip().strip('. '))
		train_y.append('computer-company')
for line in open('apple-fruit.txt'):
	if len(line.strip())>0:				#skip empty lines
		train_data.append(line.strip('. '))
		train_y.append('fruit')

# reading test data from STDIN
N = int(raw_input())
for n in range(N):
	inp = raw_input()
	test_data.append(inp)

predict()

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:47:51 2020

@author: Shraddha
"""
import nltk


paragraph = """ In brief, the mummification process may be summarized as follows: 
    extract, sterilize, dehydrate, perfume, seal, tag, and stock. 
    All were done ceremoniously and with due respect to the dead body. 
    The viscera were extracted through an incision about 10 inches long, 
    usually made in the left side of the abdomen. 
    Through this incision, all the “floating” contents of the abdominal cavity, 
    namely, the stomach, the liver, the spleen, and the intestines, 
    were removed but the kidneys were left in place. 
    The diaphragm was then cut and the thoracic contents removed through 
    the abdominal incision. The heart, which was considered the center of
    emotions and the seat of conscience, was left in place. 
    The ancient Egyptians seem to have attached no importance to the brain, 
    which was removed through the ethmoid bone. Following these extractions began 
    the slow process of sterilization and dehydration of the body, accomplished by 
    osmosis with dry natron. Resterilization of the cavities, perfuming, closing the 
    incision, and wrapping the body with linen and with beeswax completed the process.
    Molten resin was used to seal the body and its wrappings, providing a barrier against 
    insects and anaerobes. """
    
#cleaning the texts
import re  #re means regular expressions
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wordnet=WordNetLemmatizer()
sentences = nltk.sent_tokenize(paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()




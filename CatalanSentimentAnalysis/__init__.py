#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk, nltk.classify.util
from nltk.metrics import *
from nltk.classify import NaiveBayesClassifier

import sys
from tweetCleaner import TweetCleaner

reload(sys)
sys.setdefaultencoding('utf-8')
cleaner = TweetCleaner()

def make_full_dict(words):
    return dict([(word, True) for word in words])

def evaluate_features(feature_select, trainingFile):

    #reading pre-labeled input and splitting into lines
    posSentences = []
    negSentences = []

    with open(trainingFile, 'r') as f:
        for line in f.readlines():
            if line.startswith('1'):
                posSentences.append(cleaner.clean(line[2:]))
            elif line.startswith('0'):
                negSentences.append(cleaner.clean(line[2:]))

    posFeatures = get_features(posSentences, 'pos', feature_select)
    negFeatures = get_features(negSentences, 'neg', feature_select)

    #selects 3/4 of the features to be used for training and 1/4 to be used for testing
    return posFeatures + negFeatures


def get_features(sentences, pol, feature_select):
    #http://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
    #breaks up the sentences into lists of individual words (as selected by the input mechanism) and appends 'pos' or 'neg' after each list
    features = []
    for i in sentences:
        words = unicode(i).split()
        words = [feature_select(words), pol]
        features.append(words)
    return features

trainFeatures = evaluate_features(make_full_dict, './CatalanSentimentAnalysis/data/corpus.txt')
classifier = NaiveBayesClassifier.train(trainFeatures)

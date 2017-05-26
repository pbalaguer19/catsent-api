#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pickle
from tweetCleaner import TweetCleaner

reload(sys)
sys.setdefaultencoding('utf-8')
cleaner = TweetCleaner()

f = open ('nVClassifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

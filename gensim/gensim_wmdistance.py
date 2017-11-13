# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:32:08 2017

@author: alsherman
"""

# Train word2vec model.
model = Word2Vec(sentences)

# Some sentences to test.
sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
sentence_president = 'The president greets the press in Chicago'.lower().split()

# Remove their stopwords.
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stopwords]
sentence_president = [w for w in sentence_president if w not in stopwords]

# Compute WMD.
distance = model.wmdistance(sentence_obama, sentence_president)


### TEST DATA
import configparser
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Documents, Sections
config = configparser.ConfigParser()
config.read('config.ini')
DB_CONNECTION = config['USER']['DB_CONNECTION']

engine = create_engine(DB_CONNECTION)

sections = pd.read_sql('SELECT * FROM Sections', con=engine)
all_sections = sections.section_text.head(10)

sentences = []
for section in all_sections:
    sentence = [w.lower() for w in section.split(' ') if w not in stopwords]
    sentences.append(sentence)    

model = Word2Vec(sentences,)
model.vocabulary
model.most_similar('fashion')
model.wmdistance(sentences[3][-4:-1], sentences[2][-5:])
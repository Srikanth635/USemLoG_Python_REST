import whisper
import torch
import time
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import sent_tokenize
from datetime import datetime,timedelta
import rasa

# import spacy
# sp = spacy.load('en_core_web_lg')
# sen = sp(u"Move the cup from the table")
# verbs = []
# for word in sen:
#     print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
#     if word.pos_ == "VERB":
#         verbs.append((word.text,word.pos_))
#
# print("VERBS: ",verbs)
#
# for entity in sen.ents:
#     print("FIRST ENTS : ",entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))
#
# from spacy.tokens import Span
#
# ORG = sen.vocab.strings[u'PRODUCT']
# new_entity = Span(sen, 2, 3, label=ORG)
# sen.ents = list(sen.ents) + [new_entity]
#
# for entity in sen.ents:
#     print("Second ENTS : ",entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))


#####################################################     RASA      ####################################################
# rasa run --enable-api --debug

import requests
# text = requests.form.get('query')
payload = {"sender": "Rasa", "text": "pour water"}
headers = {'content-type': 'application/json'}
response = requests.post('http://localhost:5005/model/parse', json=payload, headers=headers)
result = response.json()
print(result)

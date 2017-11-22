# -*- coding=utf-8 -*-
import nltk
import random


def segment(text, segments):
    words = []
    begin = 0
    for i in range(len(segments)):
        if segments[i] == "1":
            words.append(text[begin:i+1])
            begin = i+1
    words.append(text[begin:])
    return words


saying = ['no', 'more', 'tear', 'as', 'it', 'no', 'more', 'compensation', 'tear']
tokens = set(saying)
tokens = sorted(tokens)
fdist = nltk.FreqDist(saying)
print fdist[4]
print fdist.most_common(5)
thai = u'การตัดคำภาษาไทยช่างยากเหลือเกิน'
seg1 = [random.choice(['0', '1']) for i in thai]
x = segment(thai, seg1)
print thai[3:7]
print type(x)
for i in x:
    print i
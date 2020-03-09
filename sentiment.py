import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import re

def sentiment_value(title, para):

    sentiment_text = TextBlob(title + " " + para)

    para_words = []
    '''for word in para.lower().split():
        if 'https' in word:
            continue
        if '.' in word:
            for item in word.split('.'):
                if item != '':
                    if (item == '(') or (item == ')') or (item == '“') or (item == '”') or (item == ':') or (item == '-'):
                        continue
                    else:
                        para_words.append(re.sub("[()“”:…]+", "", item.replace("’","'")))
        elif ',' in word:
            for item in word.split(','):
                if item != '':
                    if (item == '(') or (item == ')') or (item == '“') or (item == '”') or (item == ':') or (item == '-'):
                        continue
                    else:
                        para_words.append(re.sub("[()“”:…]+", "", item.replace("’","'")))
        elif '-' in word:
            for item in word.split('-'):
                if item != '':
                    if (item == '(') or (item == ')') or (item == '“') or (item == '”') or (item == ':') or (item == '-'):
                        continue
                    else:
                        para_words.append(re.sub("[()“”:…]+", "", item.replace("’","'")))
        else:
            para_words.append(re.sub("[()“”:…]+", "", word.replace("’","'")))'''

    for word in para.lower().split():
        if 'https' in word:
            continue
        ###words_list = re.split("\. |, |/ |\-|\n",word)
        words_list = re.findall(r"[\w']+", word)
        for item in words_list:
            if item == '—':
                continue
            else:
                para_words.append(re.sub("[()“”:…]+", "", item.replace("’","'").replace('.','').replace(',','').replace('—','')))

    clean_words = para_words[:]
    
    stop_words = stopwords.words('english')

    for word in para_words:
        if word.lower() in stop_words:
            clean_words.remove(word)

    word_count = {}

    for word in clean_words:
        if (word == '\-') or (word == ''):
            continue
        if word not in word_count:
            word_count[word] = 1
        
        if word in word_count:
            word_count[word] += 1

    return sentiment_text.sentiment.polarity, word_count

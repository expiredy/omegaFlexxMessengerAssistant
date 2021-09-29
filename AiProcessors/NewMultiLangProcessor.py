import re
import pymorphy2
from pprint import pprint

import nltk
import spacy
from pymorphy2 import MorphAnalyzer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from langdetect import detect
from sentimental import Sentimental

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    "wordnet",
])


# written_text_by_user = передача текста из мессенджера
def get_messege_processing_info(written_text_by_user: str):
     # = "привет, я глупый"
    # written_text_by_user_for_connection = written_text_by_user ### Если надо будет проверять на связность

    # en = english

    # Определяем язык для дальнейшей работы с текстом

    language = detect(written_text_by_user)
    print(language)

    written_text_by_user = nltk.word_tokenize(written_text_by_user)

    if language == 'en':

        # Удаление stopwords на английском
        filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('english')]

        # Соединяем в текст целиком для леммы на английском
        filtered_written_text_by_user = " ".join(filtered_written_text_by_user)

        # Лемматизация для английского
        nlp = spacy.load('en', disable=['parser', 'ner'])
        sentence = filtered_written_text_by_user
        doc = nlp(sentence)
        full_ready_text_by_user = " ".join([token.lemma_ for token in doc])

    ### Тут вся предобработка для русского
    else:

        # Удаление stopwords на русском
        filtered_written_text_by_user = [word for word in written_text_by_user if word not in stopwords.words('russian')]

        # Лемматизация для русского
        morph = pymorphy2.MorphAnalyzer()
        full_ready_text_by_user = []
        for word in filtered_written_text_by_user:
            russian_normalized = morph.parse(word)[0]
            full_ready_text_by_user.append(russian_normalized.normal_form)

        # Соединяем в целый текст для дальнейшей работы
        full_ready_text_by_user = " ".join(full_ready_text_by_user)

    full_ready_text_by_user = nltk.sent_tokenize(full_ready_text_by_user)
    print('Результат предобработки =', full_ready_text_by_user)

    if language == 'en' :
        sia = SentimentIntensityAnalyzer()

        dict_of_results = []
        list_of_dicts = []

        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sia.polarity_scores(full_ready_text_by_user[number])
            list_of_dicts.append(dict_of_results)

        #results_for_connection = sia.polarity_scores(written_text_by_user_for_connection) ### В начале тоже закомментил, если понадобится потом допилю

    else:
        sent = Sentimental()

        dict_of_results = []
        list_of_dicts = []

        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sent.analyze(full_ready_text_by_user[number])
            list_of_dicts.append(dict_of_results)

    return list_of_dicts # То что выведет "comparative" это среднее значение негатива/позитива, сентимента короче, его можно и брать
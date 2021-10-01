import time

import pymorphy2
from multiprocessing.pool import ThreadPool

import nltk
import spacy
from detoxify import Detoxify
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from sentimental import Sentimental

from DictKeyConfig import *

ENGLISH_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"

nltk.download([
    "names",
    "stopwords",
    "state_union",
    "twitter_samples",
    "movie_reviews",
    "averaged_perceptron_tagger",
    "vader_lexicon",
    "punkt",
    "wordnet", ])

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

all_session_message_data = []
new_server_callback_data = []


def get_language_key_code(message: str) -> str:
    for symbol in message.split()[0]:
        if symbol.lower() not in ENGLISH_ALPHABET:
            return "ru"
    return "en"


def get_message_preprocessed_data_list(written_text_by_user: str) -> dict:
    written_text_by_user_for_toxic = written_text_by_user  ### Если надо будет проверять на связность
    # en = english
    language = get_language_key_code(written_text_by_user)
    # Определяем язык для дальнейшей работы с текстом
    print(language)

    written_text_by_user = nltk.word_tokenize(written_text_by_user)
    # Тут вся предобработка для английского
    if language == 'en':
        # Удаление stopwords на английском
        filtered_written_text_by_user = [word for word in written_text_by_user
                                         if word not in stopwords.words('english')]
        filtered_written_text_by_user = written_text_by_user

        # Соединяем в текст целиком для леммы на английском
        filtered_written_text_by_user = " ".join(filtered_written_text_by_user)

        # Лемматизация для английского
        sentence = filtered_written_text_by_user
        doc = nlp(sentence)
        full_ready_text_by_user = " ".join([token.lemma_ for token in doc])

    # Тут вся предобработка для русского
    else:
        # Удаление stopwords на русском
        filtered_written_text_by_user = [word for word in written_text_by_user
                                         if word not in stopwords.words('russian')]

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

    written_text_by_user_for_toxic = nltk.sent_tokenize(written_text_by_user_for_toxic)
    print('Результат для токсичности in English=', written_text_by_user_for_toxic)
    # Модель предсказывания для английского
    dict_of_results = []
    list_of_dicts = []
    if language == 'en':
        sia = SentimentIntensityAnalyzer()
        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sia.polarity_scores(full_ready_text_by_user[number])
    # Модель для русского языка
    else:
        sent = Sentimental()
        for number in range(len(full_ready_text_by_user)):
            dict_of_results = sent.analyze(full_ready_text_by_user[number])
    list_of_dicts.append(dict_of_results)
    return {LIST_OF_PROCESSED_DATA_DICTS_KEY: list_of_dicts,
            FULL_PROCESSED_USER_TEXT_KEY: full_ready_text_by_user,
            DICT_OF_RESULTS_KEY: dict_of_results,
            TEXT_FOR_TOXIC_PROCESSING_KEY: written_text_by_user_for_toxic}


# written_text_by_user = input()
def get_messege_processing_info(written_text_by_user: str) -> list:
    # written_text_by_user = "Hello, i love cats and dogs. I like to play football!"

    list_of_dicts = get_message_preprocessed_data_list(written_text_by_user)[LIST_OF_PROCESSED_DATA_DICTS_KEY]

    for dict_ in list_of_dicts:
        for key in list(dict_.keys()):
            print(key + ": " + str(dict_[key]))
    return list_of_dicts


def full_message_analyze(message: str):
    language = get_language_key_code(message)
    processed_data_dict = get_message_preprocessed_data_list(message)

    dict_of_results = processed_data_dict[DICT_OF_RESULTS_KEY]
    list_of_dicts = processed_data_dict[LIST_OF_PROCESSED_DATA_DICTS_KEY]
    full_ready_text_by_user = processed_data_dict[FULL_PROCESSED_USER_TEXT_KEY]
    written_text_by_user_for_toxic = processed_data_dict[TEXT_FOR_TOXIC_PROCESSING_KEY]

    toxic = 0
    bad_words = 0
    rasizm = 0
    threat = 0
    comparative = 0
    negative = 0

    # Данные для диаграмм рус.

    if language != 'en':
        for dict_ in list_of_dicts:
            comparative = comparative + dict_['comparative']  # Негативность/токсичность

        comparative = round(comparative, 1) // 2
        print('comparative =', comparative)

    ###########################################
    ###########################################
    ###### доп. тема для диаграмм англ.
    if language == 'en':
        for number in range(len(full_ready_text_by_user)):
            # Токсичность текста (надо отдельно а то работает долго слишком)......................
            dict_of_results_tox = Detoxify('original').predict(written_text_by_user_for_toxic[number])
            dict_of_results.update(dict_of_results_tox)
            list_of_dicts.append(dict_of_results)

            # Данные для диаграмм англ.
        for dict_ in list_of_dicts:
            negative = negative + dict_['neg'] - dict_['pos']  # Негативность
            toxic = toxic + dict_['toxicity'] + dict_['severe_toxicity']  # Токсичность
            bad_words = bad_words + dict_['insult'] + dict_['obscene']  # Плохие слова
            rasizm = rasizm + dict_['identity_hate']  # Расизм и т.д.
            threat = threat + dict_['threat']  # Угрозы

    # Округление всех до норм состояния

    negative = round(negative, 1)
    toxic = round(toxic, 1)
    bad_words = round(bad_words, 1)
    rasizm = round(rasizm, 1)
    threat = round(threat, 1)
    return negative, toxic, bad_words, rasizm, threat


def async_manager_preprocessor(pool_thread_parameter):
    global all_session_message_data, new_server_callback_data

    while all_session_message_data:
        message_for_processing = all_session_message_data.pop()
        new_server_callback_data.append(full_message_analyze(message_for_processing))


def get_diagram_data(all_message_data: list,):
    global all_session_message_data, new_server_callback_data

    all_session_message_data = all_message_data
    # with Pool(processes=len(all_message_data)) as getter_pool:
    #     getter_pool.map(async_manager_preprocessor, range(len(all_message_data)))
    ThreadPool(processes=len(all_message_data)).map(async_manager_preprocessor, range(len(all_message_data)))
    return new_server_callback_data


if __name__ == "__main__":
    work_time = time.time()
    print(get_diagram_data(["Hello world", "You are sucker", "hate russian niggers"]))
    print(work_time)